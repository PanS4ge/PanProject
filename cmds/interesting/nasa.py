#{}nasa - Get NASA public api information
import discord
from urllib.request import urlopen
import json

url = "https://api.nasa.gov/planetary/apod?api_key=5vuqN7ClED4E06czXprU4MI9gLszjcFueNRS7jdw"

async def Cmd(language, serverlang, message, client):
    msgedit = await message.channel.send("<a:loading:936978619639668787> This API has poop hosting... Please wait...")
    try:
        response = urlopen(url)
        data_json = json.loads(response.read())
        embedVar = discord.Embed(title=data_json['title'], description=data_json['explanation'], color=0x000000)
        embedVar.set_footer(text=f"{data_json['date']}")
        embedVar.set_image(url=data_json['hdurl'])
        await msgedit.edit(content="I got it!", embed=embedVar)
    except KeyError:
        await msgedit.edit(content="They changed the JSON layout :(")
    except:
        await msgedit.edit(content="API denied my connection :(\n||SpaceX at least has better api, thanks Elon, very cool!||")