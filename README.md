# Void API | Docs

  

An Python wrapper for the https://voidbots.net/

  

# Requirements 

 - Pythin 3.6 or above
 - aiohttp (`python -m pip install aiohttp`)
 - discord.py (`python -m pip install discord.py`)
 - python-dateutil (`python -m pip install python-dateutil`)

# Installation
Install via pip (recommended)
```py
soon
```
Install from source
```
pip install git+https://github.com/ggashish/voidapi/
```
# Documentation
Documentation can be found [here](https://docs.voidbots.net/)

# Features

 - POST bot stats
 - GET check voted
 - GET bot info
 - GET bot analytics
 - GET bot reviews
 - GET search bot
 - GET bot votes
 - GET user info
 - GET pack info

# Support 
You can get support be either joining our [Support Server](https://discord.gg/QbnZMCP8MY) or contact me on [ggashish#6132](https://discord.com/users/711043296025378856)

# Usage
```py
import voidapi

client = voidapi.Client(bot, api_key)
```
# Funtions
## `await client.check_voted(bot_id, user_id)`
Check if a user has voted for a bot.
`Parameters:`

 - bot_id ([int](https://docs.python.org/3/library/functions.html#int)) - ID of bot to check for.
 - user_id ([int](https://docs.python.org/3/library/functions.html#int)) -   ID of user to check for.

 **`Returns CheckVoted (class):`**
`attributes`:
 - `bot_id` ([int](https://docs.python.org/3/library/functions.html#int)) - ID of the bot
 - `voter_id` ([int](https://docs.python.org/3/library/functions.html#int)) - ID of the voter
 - `voted` ([bool](https://docs.python.org/3/library/functions.html#bool)) - Voted for the bot or not.
 - `vote_time` ([datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)) - Time of vote if voted.
  - `next_vote` ([datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)) - Time of the next vote if voted.

## `await client.bot_info(bot_id)`
Get a specific bot's information.
`Parameters:`

 - bot_id ([int](https://docs.python.org/3/library/functions.html#int)) - ID of bot to check for.

 **`Returns BotInfo (class):`**
`attributes`:
 - `bot_id`([int](https://docs.python.org/3/library/functions.html#int)) - ID of the bot.
 - `servers`([int](https://docs.python.org/3/library/functions.html#int)) - Server count if available.
 - `owners`(List([int](https://docs.python.org/3/library/functions.html#int))) - IDs of the bot's owner.
 - `votes`([int](https://docs.python.org/3/library/functions.html#int)) - Number of votes bot received.
 - `monthly_votes`([int](https://docs.python.org/3/library/functions.html#int)) - Total monthly vote received.
 - `total_votes`([int](https://docs.python.org/3/library/functions.html#int)) - Total bot's votes.
 - `blurb`([str](https://docs.python.org/3/library/stdtypes.html#str)) - Short description of the bot.
 - `description`([str](https://docs.python.org/3/library/stdtypes.html#str)) - Long bot's description.
 - `certified`([bool](https://docs.python.org/3/library/functions.html#bool)) - Bot is certified.
 - `links`([dict](https://docs.python.org/3/library/stdtypes.html#dict)) - Dict of all the links.
 - `tags`(List([str](https://docs.python.org/3/library/stdtypes.html#str))) - List of all the bot tags.

## `await client.bot_analytics(bot_id)`
Get the analytics that we store for your bot.
`Parameters:`

 - bot_id ([int](https://docs.python.org/3/library/functions.html#int)) - ID of bot to check for.

 **`Returns CheckVoted (class):`**
`attributes`:
 - `bot_id`([int](https://docs.python.org/3/library/functions.html#int)) - ID of the bot.
 - `analytics`(List([dict](https://docs.python.org/3/library/stdtypes.html#dict))) - List of dicts of analytics.
 
 ## `await client.bot_reviews(bot_id)`
Get the reviews are stored for your bot.
`Parameters:`

 - bot_id ([int](https://docs.python.org/3/library/functions.html#int)) - ID of bot to check for.

 **`Returns BotReviews (class):`**
`attributes`:
 - `analytics`(List([dict](https://docs.python.org/3/library/stdtypes.html#dict))) - List of dicts of reviews if available.

 ## `await client.search_bot(query)`
Search our list of bots using a json api.
`Parameters:`

 - bot_id ([str](https://docs.python.org/3/library/stdtypes.html#str)) - Query to search bot.

 **`Returs Dict`:**
 

 - Returns a dict of bots is available.

 ## `await client.bot_votes(bot_id)`
Get an array of users who have voted for your bot.
`Parameters:`

 - bot_id ([int](https://docs.python.org/3/library/functions.html#int)) - ID of bot to check for.


 **`Returs List`:**
 

 - Returns a list of users who voted the bot if available.

## `await client.user_info(user_id)`
Get a specific user's information.
`Parameters:`

 - user_id ([int](https://docs.python.org/3/library/functions.html#int)) - The ID of the user to check for.

 **`Returns UserInfo (class):`**
`attributes`:
 - `user_id`([int](https://docs.python.org/3/library/functions.html#int)) - ID of the user.
 - `blurb`([str](https://docs.python.org/3/library/stdtypes.html#str)) - Short description of the user.
 - `description`([str](https://docs.python.org/3/library/stdtypes.html#str)) - Long description of the user.
 - `theme`([str](https://docs.python.org/3/library/stdtypes.html#str)) - Theme of the user.
 - `bots`(List([int](https://docs.python.org/3/library/functions.html#int))) - List of bots user owns if any.
 - `packs`(List([str](https://docs.python.org/3/library/stdtypes.html#str))) - List of pack user own if any.
 - `achievements`(List([str](https://docs.python.org/3/library/stdtypes.html#str))) - List of achievement of users if any.
 - `blacklist`(List([str](https://docs.python.org/3/library/stdtypes.html#str))) - 
 - `first_login`([datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)) - First time user logged in.
 - `last_login`([datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)) - Last time user logged in.
 - `links`(List([str](https://docs.python.org/3/library/stdtypes.html#str))) - List of links of users if any.

## `await client.pack_info(pack_id)`
Get a specific user's information.
`Parameters:`

 - pack_id ([str](https://docs.python.org/3/library/stdtypes.html#str)) - The ID of the pack to check for.

 **`Returns PackInfo (class):`**
`attributes`:
 - `pack_id`([str](https://docs.python.org/3/library/stdtypes.html#str)) - ID of the pack.
 - `name`([str](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the pack.
 - `description`([str](https://docs.python.org/3/library/stdtypes.html#str)) - Description of the pack.
 - `bots`(List([int](https://docs.python.org/3/library/functions.html#int))) - List of bots the pack have.
 - `owners`(List([int](https://docs.python.org/3/library/functions.html#int))) - List of owner the pack.
 - `tags`(List([str](https://docs.python.org/3/library/stdtypes.html#str))) - List of tags the pack have.
 - `created_at`([datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)) - Time of pack creating