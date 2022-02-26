#{}chuck_norris_joke - Gives a random joke about Chuck Norris
import discord
import requests
import json

url = "https://api.chucknorris.io/jokes/random"

async def Cmd(language, serverlang, message, client):
    response = requests.get(url)
    data_json = response.json()
    await message.channel.send(f"{data_json['value']}")