#{}dis - Get a random "Dis" picture (there is a chance that sends non-dis pic)
import glob

import discord
import random

async def Cmd(language, serverlang, message, client):
    dislink = random.choice(glob.glob("cmds\\fun\\dis\\*.*"))

    backslash = "\\"
    embedVar = discord.Embed(title=f"Here's Dis", description=f"ID: {dislink.split(backslash)[-1]}",
                             color=0x00ff00)
    file = discord.File(dislink, filename="output.png")
    embedVar.set_image(url="attachment://output.png")
    msg = await message.channel.send(file=file, embed=embedVar)
    await msg.add_reaction("🖕")