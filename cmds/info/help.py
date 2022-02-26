#{}help - Gives help about bot
import glob
import json
import os

import utils

import discord

from discord_components import Select, SelectOption
from discord_components import Button, ButtonStyle

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

async def Cmd(language, serverlang, message, client):
    #try:
        embedVar = discord.Embed(title="Help", description="for Pan-Project Bot.", color=0x00ff00)
        ar = []
        embedVar.add_field(name="Select from dropdown menu below", value="OK?", inline=False)
        eeeteee = 0
        for x in glob.glob("cmds/*/"):
            taaataaa = 0
            if(int(len(glob.glob(f"{x}/*/"))) > 2):
                for xer in glob.glob(f"{x}/*/"):
                    for yer in glob.glob(f"{xer}/*.py"):
                        with open(yer, "r", encoding="utf8") as hfdhd:
                            #print(len(hfdhd.readline(1).split("||")))
                            #print(hfdhd.readline(1).split("||"))
                            array = hfdhd.readline().split("||")
                            #print("array - " + str(array))
                            #print("len(array) - " + str(len(array)))
                            eeeteee = eeeteee + len(array)
                            taaataaa = taaataaa + len(array)
                            #print(f"--> {str(taaataaa)}")
            else:
                for y in glob.glob(f"{x}/*.py"):
                    with open(y, "r", encoding="utf8") as hfdhd:
                        #print(len(hfdhd.readline(1).split("||")))
                        #print(hfdhd.readline(1).split("||"))
                        array = hfdhd.readline().split("||")
                        #print("array - " + str(array))
                        #print("len(array) - " + str(len(array)))
                        eeeteee = eeeteee + len(array)
                        taaataaa = taaataaa + len(array)
                        #print(f"--> {str(taaataaa)}")
            #print("-------------------")
            try:
                with open(x + "info", "r", encoding="utf8") as info:
                    ar.append(SelectOption(label=x.replace("cmds", "").replace("\\", "") + " -> " + info.read() + " (" + str(taaataaa) + " cmds)", value=x.replace("cmds", "").replace("\\", "")))
            except:
                pass

        linecount = 0
        for x in glob.glob("C:/Users/User/PycharmProjects/discord.py/*/", recursive=True):
            #print(f"{x}")
            for y in glob.glob(x + "*.py"):
                #print(f"{x} {y}")
                with open(y, "r", encoding="utf8", errors="ignore") as f:
                    for z in f.readlines():
                        #print(f"{x} {y} - {z}")
                        linecount = linecount + 1
        embedVar.add_field(name=f"We have {eeeteee} commands with over {linecount} lines of code!", value="And more on the way!", inline=False)
        #print(ar)
        #print(type(ar))
        await message.channel.send(embed=embedVar, components=[Select(placeholder='This dropdown menu', options=ar), ])
    #except Exception as e:
    #    await utils.save_error(str(message.content), os.path.basename(__file__), e)
    #    await message.channel.send("Error. I saved error in my error database, my creator will check out.")