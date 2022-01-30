#{}support_server - Join our support server||#{}support_server ad - Advertisement for our support server/bot
import discord

async def Cmd(language, serverlang, message, client):
    if("ad" in message.content):
        await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["support_server_ad"])
    else:
        await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["support_server"])