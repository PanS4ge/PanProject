#{}join - Joins VC
import discord

def Get_Connected_VC(message):
    for x in message.guild.voice_channels:
        if(message.author in x.members):
            return x.id
    return 2137

async def Cmd(language, serverlang, message, client):
    channel = Get_Connected_VC(message)
    if(channel != 2137):
        await client.get_channel(channel).connect()
        await message.channel.send("Joined")
    else:
        await message.channel.send("Join VC idot")