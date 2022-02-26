#{}vent - Vent.
import json
import discord
import BadgesManager
import hashlib

prefix = {}
with open("prefix.json", "r") as welcom:
    prefix = json.loads(welcom.read())

async def Cmd(language, serverlang, message, client):
        try:
            if(BadgesManager.Have_Badge(14, message.author.id) == False):
                await message.delete()
                try:
                    useprefix = prefix[str(message.guild.id)]
                except KeyError:
                    useprefix = "?"
                await client.get_channel(935098676957823006).send(
                    f"<:vent:935096581756170261> > {message.content.replace(useprefix, '').replace('vent ', '')}\nIf there is something malicious/not tos friendly it will be soon deleted!")
                await client.get_channel(936942816280604672).send(
                    f"<:vent:935096581756170261> > {message.author} sent *{message.content.replace(useprefix, '').replace('vent ', '')}*")
                await message.channel.send(
                    f"<:vent:935096581756170261> > {message.content.replace(useprefix, '').replace('vent ', '')}\nIf there is something malicious/not tos friendly it will be soon deleted!\n*Sent on #vents on my support server*")
                await BadgesManager.Add_Badge(14, message.author.id, client)
            else:
                await message.channel.send(f"<:vent:935096581756170261> You already vented!")
        except:
            await message.channel.send(f"Error, use won't be took")