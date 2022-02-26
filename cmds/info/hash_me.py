#{}hash_me - Sends your hash
import discord
import requests
import json

async def Cmd(language, serverlang, message, client):
    await message.channel.send(f"Your hash is *{str(hash(message.author))}*")