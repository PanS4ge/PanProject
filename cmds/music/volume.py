#{}volume (volume) - Sets volume on vc
import discord
from discord.utils import get
import youtube_dl
import os

def Get_Connected_VC(message):
    for x in message.guild.voice_channels:
        if(message.author in x.members):
            return x.id
    return 2137

async def Cmd(language, serverlang, message, client):
    channel = Get_Connected_VC(message)
    if(channel != 2137):
        try:
            url = int(message.content.split(" ")[1])
        except:
            await message.channel.send("Bro put valid number after command.")
        guild = message.guild
        vcli = get(client.voice_clients, guild=message.guild)
        if(url > 100):
            await message.channel.send("I won't kill your eardrums idot")
        else:
            vcli.volume = url
            vcli.is_playing()
    else:
        await message.channel.send("Join VC idot, or join me with join cmd")