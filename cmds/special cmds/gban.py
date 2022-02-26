#{}gban (member id) (reason (space as *_*)) - gbans member
import discord
import requests
import json

import BadgesManager
import utils

async def Cmd(language, serverlang, message, client):
    if(utils.has_sc_perms(message.author.id)):
        try:
            Gban_user(message.content.split(" ")[1], message.content.split(" ")[2].replace("_", " "))
            await message.channel.send("Gbanned!")
        except:
            await message.channel.send("Too less args")
    else:
        await message.channel.send("Impossible for u!")

def Gban_user(memid, reason):
    with open("gbans.json", "r") as gb:
        peepee = json.loads(gb.read())
        for y in peepee:
            if(y['id'] == memid):
                return "This man is already GBANNED."
        peepee.append({"id": memid, "reason": reason})
    with open("gbans.json", "w") as gb:
        gb.write(json.dumps(peepee))
    return "Gbanned this bitch!"