import discord
import aiohttp
import asyncio

from .exceptions import *
from asyncio.tasks import Task
from dateutil import parser

class Client:
    def __init__(self, bot: discord.Client, api_key: str, auto_post: bool = False, **kwargs):
        self.base_url = "https://api.voidbots.net/"
        self.bot = bot
        self.api_key = api_key
        self.auto_post = auto_post
        self.loop = kwargs.get("loop", bot.loop)
        self.session = aiohttp.ClientSession(loop=self.loop)

        self.auto_post_task = Task
        self.auto_post_interval = kwargs.get("auto_post_interval", 180)

        self.user_fetch = kwargs.get("user_fetch", False)
        self.headers = {"Authorization": self.api_key}

        if self.auto_post is True:
            self.auto_post_task = self.loop.create_task(self.auto_post_stats())

    async def auto_post_stats(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            try:
                await self.post_stats(self.bot.user.id, len(self.bot.guilds), self.bot.shard_count)
            except Exception:
                pass
            await asyncio.sleep(self.auto_post_interval)


    async def get_request(self, url: str, **kwargs):
        async with self.session.get(url, **kwargs) as resp:
            return await resp.json()

    async def post_request(self, url: str, **kwargs):
        async with self.session.get(url, **kwargs) as resp:
            return await resp.json()

    async def post_stats(self, bot_id: int, server_count: int, shard_count: int = None):
        data = {"server_count": server_count, "shard_count": shard_count or 0}
        resp = await self.get_request(self.base_url + f"bot/stats/{bot_id}", headers=self.headers, json=data)

        if "error" in resp:
            raise NotFound("Authorization header not found.")

        return resp

    async def check_voted(self, bot_id: int, user_id: int):
        resp = await self.get_request(self.base_url + f"bot/voted/{bot_id}/{user_id}", headers=self.headers)
        
        if "error" in resp:
            raise NotFound("I could not find any votes with that info!")
        return CheckVoted(self, resp)

    async def bot_info(self, bot_id: int):
        resp = await self.get_request(self.base_url + f"bot/info/{bot_id}", headers=self.headers)

        if "message" in resp:
            raise UnAuthorized("Invalid authorization key provided")

        if "error" in resp:
            raise NotFound("No bot found")

        return BotInfo(self, resp)

    async def bot_analytics(self, bot_id: int):
        resp = await self.get_request(self.base_url + f"bot/analytics/{bot_id}", headers=self.headers)
        
        if "message" in resp:
            raise UnAuthorized("Invalid authorization key provided")
            
        if "error" in resp:
            raise NotFound("No bot found")

        return BotAnalytics(self, resp)

    async def bot_reviews(self, bot_id: int):
        resp = await self.get_request(self.base_url + f"bot/reviews/{bot_id}", headers=self.headers)

        if "message" in resp:
            raise UnAuthorized("Invalid authorization key provided")
            
        if "error" in resp:
            raise NotFound("No reviews found")

        return BotReviews(self, resp)

    async def search_bot(self, query: str=None):
        if query is None:
            resp = await self.post_request(self.base_url + f"bot/search", headers=self.headers)
            for bots in resp["bots"]:
                bots["botid"] = int(bots["botid"])
            return resp

        else:
            resp = await self.post_request(self.base_url + f"bot/search/{query}", headers=self.headers)
            return resp

    async def bot_votes(self, bot_id: int):
        resp = await self.get_request(self.base_url + f"bot/votes/{bot_id}", headers=self.headers)
        resp["votes"] = [int(i) for i in resp["votes"]]

        return resp

    async def user_info(self, user_id: int):
        resp = await self.get_request(self.base_url + f"user/info/{user_id}", headers=self.headers)

        if "message" in resp:
            raise UnAuthorized("Invalid authorization key provided")
            
        if "error" in resp:
            raise NotFound("No bot found")

        return UserInfo(self, resp)

    async def pack_info(self, pack_id: str):
        resp = await self.get_request(self.base_url + f"pack/info/{pack_id}", headers=self.headers)

        if "message" in resp:
            raise UnAuthorized("Invalid authorization key provided")
            
        if "error" in resp:
            raise NotFound("No pack found")

        return PackInfo(self, resp)

    def format_time(self, time:str):
        return parser.isoparse(time)

class CheckVoted:
    def __init__(self, main: Client, response: dict):
        self.bot = main.bot
        self.main = main
        self.response = response

        self.bot_id = int(response['botid'])
        
        self.voter_id = int(self.response['voter'])
        
        self.voted = response['voted']

        if self.voted is True:        
            self.vote_time = parser.isoparse(self.response['votedAt'])
            self.next_vote = parser.isoparse(self.response['nextVote']["date"])

class BotInfo:
    def __init__(self, main: Client, response: dict):
        self.bot = main.bot
        self.main = main
        self.response = response

        self.bot_id = int(response['botid'])
        self.servers = response['servers']
        self.owners = [int(i) for i in response['owners']]

        self.votes = response['votes']
        self.monthly_votes = response['monthly_votes']
        self.total_votes = response['total_votes']
        self.blurb = response['blurb']
        self.description = response['description']
        self.certified = response['certified']
        self.links = response['links']
        self.tags = response['tags']

class BotAnalytics:
    def __init__(self, main: Client, response: dict):
        self.bot = main.bot
        self.main = main
        self.response = response

        self.bot_id = int(response['botid'])

        self.analytics = response['analytics']

class BotReviews:
    def __init__(self, main: Client, response: dict):
        self.bot = main.bot
        self.main = main
        self.response = response


    @property
    async def reviews(self):
        reviews = self.response["reviews"]
            
        for rev in reviews:
            rev["rating"] = int(rev["rating"])
            rev["userid"] = int(rev["userid"])
            rev["botid"] = int(rev["botid"])

        self.reviews = reviews

class UserInfo:
    def __init__(self, main: Client, response: dict):
        self.bot = main.bot
        self.main = main
        self.response = response

        self.user_id = int(response["userid"])
        self.blurb = response['blurb']
        self.description = response['description']
        self.theme = response['theme']
        self.bots = [int(i) for i in response['bots']]
        self.packs = response['packs']
        self.achievements = response['achievements']
        self.blacklist = response['blacklist']
        self.first_login = parser.isoparse(response['login']["first"])
        self.last_login = parser.isoparse(response['login']["last"])
        self.links = response['links']

class PackInfo:
    def __init__(self, main: Client, response: dict):
        self.bot = main.bot
        self.main = main
        self.response = response

        self.pack_id = response['pack_id']
        self.name = response['name']
        self.description = response['description']
        self.bots = [int(i) for i in response['bots']]
        self.owners = [int(i) for i in response['owners']]
        self.tags = response['tags']
        self.created_at = parser.isoparse(response['created_at'])