#{}currency_table (count) - See currency table (in EURO)
import discord
import requests
import random
import json
import math

url = "https://api.exchangerate.host/latest"

async def Cmd(language, serverlang, message, client):
    try:
        cnt = int(message.content.split(" ")[1])
    except:
        cnt = 1
    req = requests.request("GET", url)
    reqj = req.json()
    desc = ""
    for d in reqj['rates'].keys():
        desc = desc + f"{(math.floor((reqj['rates'][d] * cnt) * 100) / 100)} {d} - "
    embedVar = discord.Embed(title=f"{cnt} EURO =", description=desc, color=0x00ff00)
    await message.channel.send(embed=embedVar)