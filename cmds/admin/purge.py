#{}purge (number) - Clears (number) of messages
import discord
import requests
import json
import utils

async def Cmd(language, serverlang, message, client):
    if (not (utils.has_permission(message.author, "manage_messages"))):
        return await message.channel.send("You need `MANAGE_MESSAGES` permission")
    #print(message.content.split(" ")[1])
    yee = await message.channel.history(limit=int(message.content.split(" ")[1])).flatten()
    countt = 0
    for x in yee:
        try:
            await x.delete()
        except:
            countt = countt + 1
    await message.channel.send(f"Deleted {message.content.split(' ')[1]} messages (didn't delete {countt})", delete_after=5)