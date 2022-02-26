#{}micup - Mic up
import discord

async def Cmd(language, serverlang, message, client):
    await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["micup"])