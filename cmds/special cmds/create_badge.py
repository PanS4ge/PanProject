#{}create_badge (emote) (name (spaces marked as *_*)) (description (spaces marked as *_*))  - Creates Badge
import discord
import requests
import json

import utils


async def Cmd(language, serverlang, message, client):
    try:
        if(utils.has_sc_perms(message.author.id)):
            await message.channel.send(f"Creating...")
            await Create_Badge(message.content.split(' ')[1], message.content.split(' ')[2].replace("_", ""), message.content.split(' ')[3].replace("_", ""), message)
            await message.channel.send("Created!")
    except:
        await message.channel.send("Too less args")

async def Create_Badge(emoji, name, desc, message):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    addthis = {"id": len(badge['badge']), "emoji": emoji, "name": name, "description": desc}
    badge['badge'].append(addthis)
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge, indent=4))
        cny.close()