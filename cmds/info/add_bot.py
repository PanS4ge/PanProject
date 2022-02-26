#{}add_bot - Thank you for supporting my bot!
import discord

async def Cmd(language, serverlang, message, client):
    await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["add_bot_link"])