#{}serialkey - Get Serial Key.
import json
import os

import discord
from discord.ext import commands

from discord_components import Button, ButtonStyle, SelectOption, Select

import utils

SysKeys=["Windows 11",
        "Windows 10",
        "Windows 7",
        "Windows 8",
        "Windows 8.1",
        "Windows Server",
        "Microsoft Hyper-V",
        "Windows MultiPoint",
        "Windows SBS",
        "Windows Home Server"]

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

keys = {}
with open('serialkey.json', encoding='utf8') as data:
    keys = json.load(data)

async def Cmd(message):
    try:
        if(not(utils.is_owner_of_bot(message.author.id))):
            return False
        embedVar = discord.Embed(title="Serial Keys", description="for Pansage Bot.", color=0x00ffff)
        ar = [[]]
        embedVar.add_field(name="Select one, and you will get key", value="Select on drop menu\n***PIRACY IS NO GOOD***", inline=False)
        yee = 0
        for x in SysKeys:
            if(len(ar[yee]) == 5):
                ar.append([])
                yee = yee + 1
            ar[yee].append(Button(style=ButtonStyle.blue, label=f"🔑{x}", custom_id=f"{x}"))
            #print(ar)
        await message.channel.send(embed=embedVar, components=ar)

        #interaction = await botClient.wait_for("button_click", check=lambda i: i.component.label == "Error Check")
        #await interaction.send(content="Here you go!", embed=errorcheck.ReturnCmd())

    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")



