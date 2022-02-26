#{}predict - Tries to predict your age by your name
import discord
from urllib.request import urlopen
import json

url = "https://api.agify.io/?name="

async def Cmd(language, serverlang, message, client):
    try:
        response = urlopen(url + message.content.split(" ")[1])
        data_json = json.loads(response.read())
        predictwhat = ""
        if(data_json['count'] <= 100):
            predictwhat = "legendary"
        elif(data_json['count'] <= 1000):
            predictwhat = "very rare"
        elif(data_json['count'] <= 10000):
            predictwhat = "rare"
        elif(data_json['count'] <= 10000):
            predictwhat = "uncommon"
        else:
            predictwhat = "common"
        await message.channel.send(f"Hmmm... {message.content.split(' ')[1].capitalize()}, that's a {predictwhat} name.\nOnly {data_json['count']} are called that,\nSo I think your {data_json['age']}.")
    except:
        await message.channel.send("Put your name as an argument.")