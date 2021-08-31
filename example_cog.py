import discord
import voidapi
from discord.ext import commands


class VoidApi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = "API KEY HERE"
        self.client = voidapi.Client(self.bot, self.api_key)

    def discord_timestamp(self, time, mode="R"):
        formated_strftime = f"<t:{int(time.timestamp())}:{mode}>"
        return formated_strftime

    def avatar_url(self, user: discord.User):
        if discord.__version__[:1] <= 2:
            return user.avatar.url
        else:
            return user.avatar_url

    def format_links(self, link: dict):
        my_list = []
        for name, value in link.items():
            if value:
                    my_list.append(f"[{name}]({value})")

        return ", ".join(my_list) if my_list else "No links"



    @commands.command(aliases=["cv"])
    @commands.is_owner()
    async def check_voted(self, ctx: commands.Context, bot: discord.User, user: discord.User):
        "Check if a user has voted for a bot."

        data = await self.client.check_voted(bot.id, user.id)
        
        embed_colour = discord.Colour.red() if data.voted is False else discord.Colour.green()
        voted = "has not voted" if data.voted is False else "has voted"

        embed = discord.Embed(colour=embed_colour)
        embed.description = f"{user.mention} (ID: {user.id}) {voted} for {bot.mention} (ID: {bot.id})"
        embed.set_footer(text="Wapper by ggashish#6132")

        if data.voted:
            embed.add_field(name="Voted", value=f"{self.discord_timestamp(data.vote_time, 'F')} ({self.discord_timestamp(data.next_vote)})")

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=["bi"])
    @commands.is_owner()
    async def bot_info(self, ctx: commands.Context, bot: discord.User):
        "Get a specific bot's information."

        try:
            data = await self.client.bot_info(bot.id)
        except voidapi.exceptions.NotFound:
            return await ctx.reply("I couldn't find any bot'", mention_author=False)

        embed = discord.Embed(colour=discord.Colour.og_blurple())
        embed.set_author(name=str(bot), url=f"https://voidbots.net/bot/{bot.id}", icon_url=self.avatar_url(bot))
        embed.description = data.blurb
        embed.set_thumbnail(url=self.avatar_url(bot))

        embed.add_field(name="Prefix", value=data.prefix)
        embed.add_field(name="Total Votes", value=data.total_votes)
        embed.add_field(name="Monthly Votes", value=data.monthly_votes)
        embed.add_field(name="Certified", value="Yes" if data.certified else "No")
        embed.add_field(name="Server Count", value=data.servers)
        embed.add_field(name="Owners", value=", ".join(str(self.bot.get_user(i)) for i in data.owners))
        embed.add_field(name="Links", value=self.format_links(data.links))
        embed.add_field(name="Tags", value=", ".join(data.tags))

        await ctx.reply(embed=embed, mention_author=False)


    ####################################################################
    ################## MORE WILL BE ADDED SOON #########################
    ####################################################################
    

def setup(bot):
    bot.add_cog(VoidApi(bot))
