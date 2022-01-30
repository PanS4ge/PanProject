#{}vent - Vent.
import json
import discord
import BadgesManager

async def Cmd(language, serverlang, message, client):
        try:
            if(BadgesManager.Have_Badge(14, message.author.id) == False):
                await message.delete()
                await client.get_channel(935098676957823006).send(
                    f"<:vent:935096581756170261> > {message.content.replace('?vent ', '')}\nIf there is something malicious/not tos friendly it will be soon deleted!")
                await message.channel.send(
                    f"<:vent:935096581756170261> > {message.content.replace('?vent ', '')}\nIf there is something malicious/not tos friendly it will be soon deleted!\n*Sent on #vents on my support server*")
                BadgesManager.Add_Badge(11, message.author.id)
            else:
                await message.channel.send(f"<:vent:935096581756170261> You already vented!")
        except:
            await message.channel.send(f"Error, use won't be took")