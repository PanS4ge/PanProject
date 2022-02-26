#{}axolotl_fact - Gives a random axolotl fact
import discord
import requests
import random
import json

url = "https://axoltlapi.herokuapp.com"

async def Cmd(language, serverlang, message, client):
    req = requests.request("GET", url)
    reqj = req.json()
    await message.channel.send(f"{reqj['facts']}")