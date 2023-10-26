#!/usr/bin/env python
import json
import os
import random

import discord
import discord.ext
from discord import Interaction

# setting up the bot
intents = discord.Intents.all()
# if you don't want all intents you can do discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# directory that has the images
images = os.path.join(os.getcwd(), "images")

with open("./config.json") as config:
    configData = json.load(config)
token = configData["Token"]
guildid = configData["Guild ID"]


# make the slash command
@tree.command(name="nikuman", description="肉まんをランダムで送信します")
async def ping(ctx: Interaction):
    items = [
        "https://t3.ftcdn.net/jpg/04/76/51/98/360_F_476519833_OQ4EBIpAbwOFEqauoXaEaBs3W2YGOHiO.jpg",
        "https://t3.ftcdn.net/jpg/01/34/53/42/240_F_134534278_rS4evkjrMtEDNIT0w478Hzn3AVB6t6Sb.jpg",
        "https://t4.ftcdn.net/jpg/04/83/87/53/240_F_483875334_eFzUBYCypQquibe6CrbXQDAuvuE79F3O.jpg",
        "https://media.gettyimages.com/id/140000263/ja/%E3%82%B9%E3%83%88%E3%83%83%E3%82%AF%E3%83%95%E3%82%A9%E3%83%88/steamed-bun-with-meat.jpg?s=612x612&w=0&k=20&c=SgroIbpBDY4bgIx875hSSFJibmklCL0GxkY5c68ravQ=",
        "https://media.gettyimages.com/id/140000263/ja/%E3%82%B9%E3%83%88%E3%83%83%E3%82%AF%E3%83%95%E3%82%A9%E3%83%88/steamed-bun-with-meat.jpg?s=612x612&w=0&k=20&c=SgroIbpBDY4bgIx875hSSFJibmklCL0GxkY5c68ravQ=",
        "https://media.gettyimages.com/id/1429698761/ja/%E3%82%B9%E3%83%88%E3%83%83%E3%82%AF%E3%83%95%E3%82%A9%E3%83%88/%E8%AA%BF%E7%90%86%E3%81%95%E3%82%8C%E3%81%9F%E3%82%B7%E3%83%A3%E3%82%AA%E3%83%AD%E3%83%B3%E3%83%90%E3%82%AA.jpg?s=612x612&w=0&k=20&c=9PQGhuKFmo-DVyLqYfZx0EFQ9U0YkuAB8JiqxjqckrE=",
        "https://t4.ftcdn.net/jpg/04/68/08/39/240_F_468083943_VcaLCjk9fcQWAOjle9RSH5lGnoFAIC9b.jpg",
        "https://t3.ftcdn.net/jpg/02/93/59/08/240_F_293590859_fFnOo5nmrgTCygfUTUs7FLm2RNU2XHD3.jpg",
        "https://t3.ftcdn.net/jpg/02/93/59/08/240_F_293590859_fFnOo5nmrgTCygfUTUs7FLm2RNU2XHD3.jpg",
        "https://t4.ftcdn.net/jpg/04/68/08/39/240_F_468083940_PX1YGBgxebs21Cfvlcsw0Ao6NSs5TIzX.jpg",
        "https://t4.ftcdn.net/jpg/03/90/76/65/240_F_390766569_HwljdoKOA6g0KVXRKlYb8AvzsavHJEmR.jpg",
        "https://t3.ftcdn.net/jpg/06/45/29/50/240_F_645295091_fiaEVxYE1ycG05ldQkMN3We8bvF8R6VQ.jpg",
        "https://t4.ftcdn.net/jpg/04/08/78/73/240_F_408787334_Om8Ye4i8j64dnnwXiKla04MZfajfPRfd.jpg",
        "https://t3.ftcdn.net/jpg/04/00/66/90/240_F_400669083_8KUrTh05ZOqNr02PWYWLO4az2wy0GdAF.jpg",
        "https://t3.ftcdn.net/jpg/04/63/24/26/240_F_463242673_ihG0C2wqnKOFzdXujWrW676No0Qy4YDn.jpg",
        "https://t4.ftcdn.net/jpg/04/68/08/39/240_F_468083931_rJXR8tQm45bPy9bOVpjwDdUV2U4UiVBd.jpg",
        "https://t3.ftcdn.net/jpg/04/81/36/16/240_F_481361607_ea2eoGSzRxAqLtIGtKMQKF2V292cVgKw.jpg",
        "https://t3.ftcdn.net/jpg/04/01/24/04/240_F_401240462_p7pX0Kd1BCoJVYybD66weMSUBLKdujUa.jpg",
        "https://t4.ftcdn.net/jpg/06/50/17/65/240_F_650176563_fJ1Rp6rDurobgl48rIVweIsO5plnRSDL.jpg",
        "https://t3.ftcdn.net/jpg/00/84/85/32/240_F_84853268_5HrByJ1ylGVYFeZ5EEoZ3KqqQMyYpIck.jpg",
        "https://t4.ftcdn.net/jpg/05/09/28/07/240_F_509280783_mqwF9xAQpLrtVDvXdzgzuVlbbqVn3wF8.jpg",
        "https://t4.ftcdn.net/jpg/04/81/49/01/240_F_481490193_fKCLbCA1giw6CowcpM4iPeWlXQzNDDH7.jpg",
    ]
    embed = discord.Embed(title="肉まんガチャ", color=0xFF0000)
    embed.set_image(url=random.choice(items))
    await ctx.response.send_message(embed=embed)


# sync the slash command to your server
@client.event
async def on_ready():
    await tree.sync()
    # print "ready" in the console when the bot is ready to work
    print("ready")


# run the bot
client.run(token)
