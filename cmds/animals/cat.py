#{}cat - Gives you a random cat image!
import discord
import requests
import json

url = "https://api.thecatapi.com/v1/images/search"

async def Cmd(language, serverlang, message, client):
    response = requests.get(url)
    data_json = response.json()
    #print(response.json())
    await message.channel.send(f"{data_json[0]['url']}")