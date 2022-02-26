#{}c4k - Caught in 4K moment.
import discord

async def Cmd(language, serverlang, message, client):
    embedVar = discord.Embed(title=language[serverlang[str(message.guild.id)]]["kernel"]["c4k"], description=".", color=0x00ff00)
    embedVar.set_image(url="https://c.tenor.com/QA6mPKs100UAAAAC/caught-in.gif")
    await message.channel.send(embed=embedVar)