#{}spacex - Get SpaceX public api information
import discord
from urllib.request import urlopen
import json

url = "https://api.spacexdata.com/v4/launches/latest"

async def Cmd(language, serverlang, message, client):
    response = urlopen(url)
    data_json = json.loads(response.read())
    embedVar = discord.Embed(title=data_json['name'], description=data_json['details'], color=0x000000)
    embedVar.set_thumbnail(url=data_json['links']['patch']['small'])
    embedVar.add_field(name="Reddit info", value=f"[Campaign]({data_json['links']['reddit']['campaign']}), [Launch]({data_json['links']['reddit']['launch']}), [Media]({data_json['links']['reddit']['media']}), [Recovery]({data_json['links']['reddit']['recovery']})", inline=True)
    #temp = ""
    #for x in data_json['links']['flickr']['original']:
    #    temp = temp + f"[{str(data_json['links']['flickr']['original'].index(x))}]({x})"
    #embedVar.add_field(name="Images", value=temp, inline=True)
    embedVar.add_field(name="YouTube video", value=f"https://youtu.be/{data_json['links']['youtube_id']}", inline=True)
    embedVar.add_field(name="Article", value=data_json['links']['article'], inline=True)
    embedVar.add_field(name="Windows in rocket", value=data_json['window'], inline=True)
    if(data_json['success']):
        embedVar.add_field(name="They succeed :tada:", value="Woohoo!", inline=True)
    else:
        embedVar.add_field(name="They didn't succeed :sob:", value="It's sad", inline=True)
    embedVar.add_field(name="There is more info they gave but it's too much.", value="Link to api to check out: https://github.com/r-spacex/SpaceX-API", inline=False)
    embedVar.set_footer(text=data_json['name'] + " " + data_json['date_utc'])
    #embedVar.set_image(url=data_json['hdurl'])
    await message.channel.send(embed=embedVar)