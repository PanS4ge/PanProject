#{}fox - Gives a random fox picture
import discord
import requests
import random
import json

url = "https://randomfox.ca/images/{NUMBER}.jpg"

async def Cmd(language, serverlang, message, client):
    await message.channel.send(f"{url.replace('{NUMBER}', str(random.randint(1, 123)))}")