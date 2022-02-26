#{}lyrics (Author (space as *_*)) (Name (space as *_*)) - Sends you lyrics of song
import asyncio

import discord
import requests

import discord
import json

import utils


async def Cmd(language, serverlang, message, client):
    headers = {
        "Content-Type": "application/json"
    }
    if(3>2):
        url = f"https://private-anon-71041c8a04-lyricsovh.apiary-proxy.com/v1/{message.content.split(' ')[1].replace('_', '%20')}/{message.content.split(' ')[2].replace('_', '%20')}"
        req = requests.request("GET", url, headers=headers)
        try:
            embedVar = discord.Embed(title=f"Lyrics of {message.content.split(' ')[1].replace('_', ' ')}'s {message.content.split(' ')[2].replace('_', ' ')}", description=f"{req.json()['lyrics']}", color=0x00ff00)
            await message.author.send(embed=embedVar)
            await message.channel.send("Sent you on dm!\nWanted on channel and you have `MANAGE MESSAGES`, write after all args - add \"chan\" to send here!")
        except:
            await message.author.send(req['error'])
    elif(message.content.split(" ")[3] == "chan" and utils.has_permission(message.author, "manage_messages")):
        url = f"https://private-anon-71041c8a04-lyricsovh.apiary-proxy.com/v1/{message.content.split(' ')[1].replace('_', '%20')}/{message.content.split(' ')[2].replace('_', '%20')}"
        req = requests.request("GET", url, headers=headers)
        try:
            embedVar = discord.Embed(title=f"Lyrics of {message.content.split(' ')[1].replace('_', ' ')}'s {message.content.split(' ')[2].replace('_', ' ')}", description=f"{req.json()['lyrics']}", color=0x00ff00)
            await message.channel.send(embed=embedVar)
        except:
            await message.channel.send(req['error'])
    #except:
    #    await message.channel.send("You didn't give any args")