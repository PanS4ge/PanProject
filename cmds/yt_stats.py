#{}yt_stats (link to yt video) - Check details of this video (I have dislikes :D)
import os
import discord
import time
import requests
import json

from discord.utils import get

import random

import utils

async def Cmd(message):
    try:
        try:
            if('https://www.youtube.com/watch?v=' in message.content):
                url = f"https://returnyoutubedislikeapi.com/votes?videoId={str(message.content.split(' ')[1].replace('https://www.youtube.com/watch?v=', ''))}"
            else:
                url = f"https://returnyoutubedislikeapi.com/votes?videoId={str(message.content.split(' ')[1].replace('https://youtu.be/', ''))}"
            #print(url)
            respnj = requests.get(url)
            resp = respnj.json()
            #print(resp)
            #try:
            #    if(resp['title'] != None):
            #        return
            #except:
            #    pass
            embedVar = discord.Embed(title=f"YouTube statistics for {str(message.content.split(' ')[1].replace('https://youtu.be/', ''))}", description="for Pan-Project Bot.", color=0x00ff00)
            embedVar.add_field(name="🤖 Hope you like my bot", value="?add_bot to add it!", inline=True)
            embedVar.add_field(name=":date: Date created", value=str(resp['dateCreated'].split("T")[0]), inline=True)
            embedVar.add_field(name=":alarm_clock: Hour created", value=str(resp['dateCreated'].split("T")[1].replace("Z", "")), inline=True)
            embedVar.add_field(name=f"<:yeee:928675155465621525> {str('{:,}'.format(resp['likes']))}", value="\*\*\*\*\*\*\*", inline=True)
            embedVar.add_field(name=f":link: Rating", value=str(resp['rating']), inline=True)
            embedVar.add_field(name=f"<:nope:928675155440443503> {str('{:,}'.format(resp['dislikes']))}", value="\*\*\*\*\*\*\*", inline=True)
            embedVar.add_field(name=f"<:views:931894288663609364> View Count", value=str('{:,}'.format(resp['viewCount'])))
            embedVar.add_field(name=f"<:nope:928675155440443503> API used", value="Return Youtube Dislikes")
            if(resp['deleted'] == False):
                embedVar.add_field(name=f"<:deleted:931894288491630612> This video isn't deleted", value="It's available to watch!")
            else:
                embedVar.add_field(name=f"<:deleted:931894288491630612> This video got deleted", value="Sorry!")
            await message.channel.send(embed=embedVar)
        except:
            await message.channel.send("Invalid YouTube link, maybe try putting https://")
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")
