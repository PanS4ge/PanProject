#{}doggo - Gives you a random doggo image!
import discord
import requests
import json

url = "https://random.dog/woof.json"

async def Cmd(language, serverlang, message, client):
    response = requests.get(url)
    data_json = response.json()
    await message.channel.send(f"{data_json['url']}")