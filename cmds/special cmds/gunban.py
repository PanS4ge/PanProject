#{}gunban (member id) - gunbans member
import discord
import requests
import json

import BadgesManager
import utils

async def Cmd(language, serverlang, message, client):
    try:
        if(utils.has_sc_perms(message.author.id)):
            Gunban_user(message.content.split(" ")[1])
            await message.channel.send("Gunbanned!")
        else:
            await message.channel.send("Impossible for u!")
    except:
        await message.channel.send("Too less args")

def Gunban_user(memid):
    with open("gbans.json", "r") as gb:
        peepee = json.loads(gb.read())
        for y in peepee:
            if(y['id'] == memid):
                peepee.remove({"id": memid, "reason": y['reason']})
    with open("gbans.json", "w") as gb:
        gb.write(json.dumps(peepee))
    return "Gunbanned this bitch!"