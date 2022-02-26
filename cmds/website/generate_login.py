#{}generate_login - Generates your login for webiste.
import discord
import requests
import json

headers = {
    "ADMIN_KEY": "pansageyt",
    "Content-Type": "application/json"
}

async def Cmd(language, serverlang, message, client):
    '''
    jsone = {}
    jsone['created_user_date'] = str(message.author.created_at)
    jsone['display_name'] = str(message.author.display_name)
    url = await message.author.avatar_url.read()
    jsone['avatar'] = str(url)
    jsone['name'] = str(message.author.name) + "#" + str(message.author.discriminator)
    req = requests.get(f"http://psbapi.herokuapp.com/botdata/post/{message.author.id}", headers=headers, json=jsone)
    await message.channel.send("Done, I will send you things right away!")
    await message.author.send(f"Login: {message.author.id}\nPassword: {req.json()[message.author.id]['password']}\nAuth: {req.json()[message.author.id]['2auth']}")
    '''
    await message.channel.send("Disabled due to a bug, maybe it's a good thing, because there is no login yet")