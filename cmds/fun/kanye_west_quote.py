#{}kanye_west_quote - Gives you a random Kanye West quote!
import discord
import requests
import json

url = "https://api.kanye.rest"

async def Cmd(language, serverlang, message, client):
    response = requests.get(url)
    data_json = response.json()
    await message.channel.send(f"{data_json['quote']}")