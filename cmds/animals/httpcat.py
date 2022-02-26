#{}httpcat - Cats representing http errors!
import discord

async def Cmd(language, serverlang, message, client):
    try:
        await message.channel.send(f"https://http.cat/{message.content.split(' ')[1]}.jpg")
    except:
        await message.channel.send(f"https://http.cat/404.jpg")