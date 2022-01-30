#{}help - Gives help about bot
import glob
import json
import os

import utils

import discord

from discord_components import Select, SelectOption

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

async def Cmd(language, serverlang, message, client):
    #try:
        embedVar = discord.Embed(title="Help", description="for Pan-Project Bot.", color=0x00ff00)
        ar = []
        embedVar.add_field(name="Select from dropdown menu below", value="OK?", inline=False)
        for x in glob.glob("cmds/*/"):
            taaataaa = 0
            for y in glob.glob(f"{x}/*.py"):
                with open(y, "r", encoding="utf8") as hfdhd:
                    #print(len(hfdhd.readline(1).split("||")))
                    #print(hfdhd.readline(1).split("||"))
                    taaataaa = taaataaa + int(len(hfdhd.readline().split("||")))
                    #print(f"--> {str(taaataaa)}")
            #print("-------------------")
            try:
                with open(x + "info", "r") as info:
                    ar.append(SelectOption(label=x.replace("cmds", "").replace("\\", "") + " -> " + info.read() + " (" + str(taaataaa) + ")", value=x.replace("cmds", "").replace("\\", "")))
            except:
                pass
        await message.channel.send(embed=embedVar, components=[Select(placeholder='This dropdown menu', options=ar), ])
    #except Exception as e:
    #    await utils.save_error(str(message.content), os.path.basename(__file__), e)
    #    await message.channel.send("Error. I saved error in my error database, my creator will check out.")