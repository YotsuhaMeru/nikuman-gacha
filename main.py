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
    f = open("./images.txt")
    items = f.readlines()
    f.close()
    embed = discord.Embed(title="肉まんガチャ 🥟", color=0xF38BA8)
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
