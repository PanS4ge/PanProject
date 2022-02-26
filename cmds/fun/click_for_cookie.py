#{}click_for_cookie - Don't ask questions
import glob
import json
import os

import utils

import discord

from discord_components import Select, SelectOption

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

rickroll = [
"Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you"
]

async def Cmd(language, serverlang, message, client):
    #try:
        embedVar = discord.Embed(title="Click for cookie", description="for Pan-Project Bot.", color=0x00ff00)
        ar = []
        embedVar.add_field(name="Select from dropdown menu below", value="OK?", inline=False)
        for x in rickroll:
            ar.append(SelectOption(label=x, value=x))
        await message.channel.send(embed=embedVar, components=[Select(placeholder='This dropdown menu', options=ar), ])
    #except Exception as e:
    #    await utils.save_error(str(message.content), os.path.basename(__file__), e)
    #    await message.channel.send("Error. I saved error in my error database, my creator will check out.")