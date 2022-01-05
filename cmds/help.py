#{}help - Gives help about bot
import glob
import json
import os

import discord

def GetFiles():
    file = []
    for x in glob.glob("cmds/*.py"):
        file.append(x)
    return file

async def Cmd(message, botvar):
    try:
        config = {}
        with open(f"config.json", encoding='utf8') as data:
            config = json.load(data)

        embedVar = discord.Embed(title="Help", description="for Pan-Project Bot.", color=0x00ff00)
        for x in GetFiles():
            with open(x, "r") as f:
                t = f.readline().replace("#", "")
                t = t.replace("{}", config[f'prefix_{botvar}'])
                t = t.replace("{HASH}", "#")
                if("||" in t):
                    for c in t.split("||"):
                        embedVar.add_field(name=c.split("-")[0], value=c.split("-")[1], inline=False)
                else:
                    embedVar.add_field(name=t.split("-")[0], value=t.split("-")[1], inline=False)
        await message.channel.send(embed=embedVar)
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")