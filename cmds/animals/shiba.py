#{}shiba - Gives a random shiba picture
import discord
import requests
import json

url = "http://shibe.online/api/shibes"

async def Cmd(language, serverlang, message, client):
    response = requests.get(url)
    data_json = response.text
    link = str(data_json).replace("[", "").replace("]", "").replace("\"", "")
    await message.channel.send(f"{link}")