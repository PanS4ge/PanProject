#{}leave - Leave VC
import discord

def Get_Connected_VC(message):
    for x in message.guild.voice_channels:
        if(message.author in x.members):
            return x.id
    return 2137

async def Cmd(language, serverlang, message, client):
    channel = Get_Connected_VC(message)
    if(channel == 2137):
        await message.channel.send("I won't leave channel if I'm not connected.")
    else:
        mem = message.guild.get_member(client.user.id)
        await mem.move_to(None)
        await message.channel.send("Left")