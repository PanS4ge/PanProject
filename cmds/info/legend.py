#{}legend - Get information of badges
import glob
import json
import os
import math

import utils

import discord

async def Cmd(language, serverlang, message, client):
    try:
        allmemcnt = 0
        fetched_guilds = client.guilds
        for x in fetched_guilds:
            #print(x.name + " -/- " + str(len(x.members)))
            allmemcnt = allmemcnt + len(x.members)

        config = {}
        with open(f"config.json", encoding='utf8') as data:
            config = json.load(data)

        badge = {}
        with open(f"badges.json", "r") as cny:
            badge = json.loads(cny.read())
            cny.close()

        embedVar = discord.Embed(title="Legend", description="for Pan-Project Bot.", color=0x00ff00)
        for x in badge["badge"]:
            embedVar.add_field(name=f"{x['emoji']} - {x['name']} / {math.floor((len(x['owners']) / allmemcnt)*10000)/100}% has this badge", value=f"{x['description']}")
        await message.channel.send(embed=embedVar)
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")