#{}member_count - Count how many members are here
import discord

async def Cmd(language, serverlang, message, client):
    await message.channel.send(f"Here we have {str(message.guild.member_count)}!")