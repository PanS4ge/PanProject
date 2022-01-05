#{}gunban - global unban this user from using the bot (Only owner)
import glob
import json
import os

import utils

import discord

async def Cmd(message):
    config = {}
    with open(f"config.json", encoding='utf8') as data:
        config = json.load(data)
    try:
        array = []
        array = message.content.split(" ")
        try:
            ping = array[1]
            config['gbans'].remove(ping)
            await message.channel.send("Global unbanned!")
            with open("config.json", "w") as c:
                c.write(json.dumps(config))
        except Exception:
            await message.channel.send("Invalid id")
    except Exception:
        await message.channel.send("Invalid args")