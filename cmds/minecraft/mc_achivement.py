#{}mc_achivement (block (in `...`)) (title (in `...`)) (description (in `...`)) - Generates you minecraft achievement
import asyncio
import math

import discord
import requests

import discord
import json

import utils


async def Cmd(language, serverlang, message, client):
    try:
        eee = str(message.content)
        yes = eee.split("`")
        #print(yes)
        for x in yes:
            if (x == "" or x == " "):
                yes.remove(x)
        embedVar = discord.Embed(title="Achievement get!", description="Congrats!", color=0x000000)
        embedVar.set_image(url=f"https://minecraft-api.com/api/achivements/{yes[1].encode('ascii', 'ignore').decode().replace(' ', '..')}/{yes[2].encode('ascii', 'ignore').decode().replace(' ', '..')}/{yes[3][:28].encode('ascii', 'ignore').decode().replace(' ', '..')}/{yes[3].encode('ascii', 'ignore').decode().replace(yes[3][:28].encode('ascii', 'ignore').decode(), '').replace(' ', '..')}")
        await message.channel.send(embed=embedVar)
    except:
        await message.channel.send("Well there was an error, maybe you didn't put arguments in \` \`?")