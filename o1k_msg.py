import glob
import json
import os

import discord
from discord.ext import commands

from discord_components import Button, ButtonStyle

import utils

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

async def Cmd(message):
    try:
        embedVar = discord.Embed(title="Get your 1,000 :fries: **on every server you're in** and exclusive badge (:man_gesturing_ok:)", description="Don't be shy, click it!", color=0x00ffff)
        ar = [[]]
        ar[0].append(Button(style=ButtonStyle.blue, label="CLAIM 🍟", custom_id="claimfries"))
        await message.channel.send(embed=embedVar, components=ar)

        #interaction = await botClient.wait_for("button_click", check=lambda i: i.component.label == "Error Check")
        #await interaction.send(content="Here you go!", embed=errorcheck.ReturnCmd())

    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")


