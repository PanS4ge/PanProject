#is_this_a_pigeon - Generate Is This A Pigeon meme with 3 boxes.
import discord
import requests
import json
username = "rng31323"
password = "rng31323@zwoho.com"
boxcount = 3
urlimage = 100777631
URL = 'https://api.imgflip.com/caption_image'
async def Cmd(language, serverlang, message, client):
   if(len(str(message.content).split("||")) != 3):
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
       'text0': str(message.content).replace(useprefix + "is_this_a_pigeon", "").split('||')[0],
       'text1': str(message.content).replace(useprefix + "is_this_a_pigeon", "").split('||')[1],
       'text2': str(message.content).replace(useprefix + "is_this_a_pigeon", "").split('||')[2],
   }
   response = requests.request('POST',URL,params=params).json()
   await message.channel.send(content=f"Did I succeed? {response['success']}\nHere's your meme! {response['data']['url']}")
