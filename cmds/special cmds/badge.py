#{}badge (add/rem/reset) (member id / *) (badge id) - Adds/Removes badge to member
import discord
import requests
import json

import BadgesManager
import utils


async def Cmd(language, serverlang, message, client):
    try:
        if(utils.has_sc_perms(message.author.id)):
            if(message.content.split(" ")[1] == "rem"):
                await BadgesManager.Remove_Badge(message.content.split(" ")[3], message.content.split(" ")[2], client)
            elif(message.content.split(" ")[1] == "add"):
                if(message.content.split(" ")[2] == "*"):
                    await message.channel.send("Forbidden")
                else:
                    await BadgesManager.Add_Badge(message.content.split(" ")[3], message.content.split(" ")[2], client)
        else:
            await message.channel.send("Impossible for u!")
    except:
        await message.channel.send("Too less args")