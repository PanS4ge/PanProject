#{}roastme - I will roast you dumb bi\*\*h!
import discord
import requests
import json

url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

async def Cmd(language, serverlang, message, client):
    response = requests.get(url)
    data_json = response.json()
    await message.channel.send(data_json['insult'])
