#expanding_brain - Generate Expanding Brain meme with 4 boxes.
import discord
import requests
import json
username = "rng31323"
password = "rng31323@zwoho.com"
boxcount = 4
urlimage = 93895088
URL = 'https://api.imgflip.com/caption_image'
async def Cmd(language, serverlang, message, client):
   if(len(str(message.content).split("||")) != 4):
       await message.channel.send("You gave invalid number of texts - seperate them with **||**")
       return
   prefix = {}
   with open("prefix.json", "r") as welcom:
       prefix = json.loads(welcom.read())

   try:
       useprefix = prefix[str(message.guild.id)]
   except KeyError:
       useprefix = "?"

   params = {
       'username': username,
       'password': password,
       'template_id': urlimage,
       'text0': str(message.content).replace(useprefix + "expanding_brain", "").split('||')[0],
       'text1': str(message.content).replace(useprefix + "expanding_brain", "").split('||')[1],
       'text2': str(message.content).replace(useprefix + "expanding_brain", "").split('||')[2],
       'text3': str(message.content).replace(useprefix + "expanding_brain", "").split('||')[3],
   }
   response = requests.request('POST',URL,params=params).json()
   await message.channel.send(content=f"Did I succeed? {response['success']}\nHere's your meme! {response['data']['url']}")
