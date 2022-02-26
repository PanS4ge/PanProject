#{}perms (add/rem) (user id) - Add/Remove permissions to user
import discord
import requests
import json
import utils

async def Cmd(language, serverlang, message, client):
    if(utils.is_owner_of_bot(message.author.id)):
        with open("permissions.json", "r") as twojstary:
            twojastara = json.loads(twojstary.read())
            if(message.content.split(" ")[1] == "add"):
                twojastara.append(message.content.split(' ')[2])
            elif(message.content.split(" ")[1] == "rem"):
                twojastara.remove(message.content.split(' ')[2])
            else:
                await message.channel.send("Invalid action")
        with open("permissions.json", "w") as teztwojstary:
            teztwojstary.write(json.dumps(twojastara))
        await message.channel.send(f"<@!{message.content.split(' ')[2]}> has been added/removed.")
    else:
        await message.channel.send(f"Not dev idot.")
