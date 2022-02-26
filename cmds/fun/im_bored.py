#{}im_bored - Gives you a random activity to do!
import discord
import requests
import json

url = "https://www.boredapi.com/api/activity/"

async def Cmd(language, serverlang, message, client):
    response = requests.get(url)
    data_json = response.json()
    msggen = f"Bro, you can *{data_json['activity']}*!\n"
    msggen = msggen + f"It's type is *{data_json['type']}*!\n"
    if(data_json['participants'] == 1):
        msggen = msggen + f"You can do it solo!\n"
    else:
        msggen = msggen + f"You need min. *{data_json['participants']}* people to do it!\n"
    if (data_json['price'] == 0):
        msggen = msggen + f"It's FREE!\n"
    else:
        msggen = msggen + f"You need to spend money (grade *{data_json['price'] * 10}*)\n"
    if (data_json['link'] != ""):
        msggen = msggen + f"(Here)[{data_json['link']}] are materials that can help!\n"
    await message.channel.send(msggen)
