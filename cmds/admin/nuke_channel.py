#{}nuke_channel - "Nukes" channel by removing all messages
import asyncio

import discord
import requests
import json
import utils

async def Cmd(language, serverlang, message, client):
    if (not (utils.has_permission(message.author, "manage_messages"))):
        return await message.channel.send("You need `MANAGE_MESSAGES` permission")
    msgedit = await message.channel.send("<a:loading:936978619639668787> Fetching all messages")
    msgs = await message.channel.history(limit=None).flatten()
    await msgedit.edit(content=f"<a:loading:936978619639668787> Fetched {str(len(msgs))} messages, deleting...")
    for x in msgs:
        await x.delete()
    await message.channel.send(content=f"Nuked channel with {str(len(msgs))} messages!")
    await message.channel.send(content=f"https://c.tenor.com/giN2CZ60D70AAAAC/explosion-mushroom-cloud.gif")