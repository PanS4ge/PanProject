#{}mc_server (server id) (port (default: 25565)) - Sends you mc server data
import asyncio
import math

import discord
import requests

import discord
import json

import utils


async def Cmd(language, serverlang, message, client):
    try:
        headers = {
            "Content-Type": "application/json"
        }
        ping = 0
        try:
            ping = int(message.content.split(' ')[2])
        except:
            ping = 25565
        url = f"https://minecraft-api.com/api/ping/{message.content.split(' ')[1]}/{ping}/json"
        req = requests.request("GET", url, headers=headers)
        data = req.json()

        url2 = f"https://minecraft-api.com/api/ping/motd/{message.content.split(' ')[1]}/{ping}"
        req2 = requests.request("GET", url2, headers=headers)
        motd = req2.text

        embedVar = discord.Embed(title=f"{message.content.split(' ')[1]}:{ping}", description=f"{motd}", color=0x00ff00)
        embedVar.add_field(name=f"Server version: ", value=f"*{data['version']['name']}*")
        embedVar.add_field(name=f"Protocol", value=f"*{data['version']['protocol']}*")
        embedVar.add_field(name=f"Players", value=f"*{data['players']['online']} / {data['players']['max']}* ({math.ceil((data['players']['online'] / data['players']['max']) * 100)}%)")
        embedVar.set_thumbnail(url=f"https://eu.mc-api.net/v3/server/favicon/{message.content.split(' ')[1]}")
        await message.channel.send(embed=embedVar)
    except json.decoder.JSONDecodeError:
        await message.channel.send("This server does not exist.")
    except Exception as exexe:
        await message.channel.send(f"Well there was an error.\n{exexe}")