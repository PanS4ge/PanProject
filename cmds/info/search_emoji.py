#{}search_emoji (name) - Searches emoji globally
import glob
import math

import discord
import random

from difflib import SequenceMatcher

def get_srednia_arytmetyczna(table):
    temp = 0
    for x in table:
        temp = temp + x
    return temp

def realround(number):
    _, d = divmod(number, 1)
    if d > 0.5:
        return int(math.ceil(number))
    else:
        return int(math.floor(number))

emote = []
similarity = []
highestemote = ""
highestemoteperc = 0

def similar(a, b):
    #print(str(a) + "+" + str(b))
    return SequenceMatcher(None, a, b).ratio()

async def Cmd(language, serverlang, message, client):
    try:
        global emote, similarity, highestemote, highestemoteperc
        emojitoyoink = message.content.split(" ")[1]
        msgse = await message.channel.send("<a:loading:936978619639668787> Searching...")
        for x in client.guilds:
            for y in x.emojis:
                emote.append(y)
                similarity.append(realround(similar(emojitoyoink, y.name) * 100))
                if(highestemoteperc < realround(similar(emojitoyoink, y.name) * 100)):
                    highestemote = y
                    highestemoteperc = realround(similar(emojitoyoink, y.name) * 100)
        await msgse.edit(content="<a:loading:936978619639668787> Preparing results...")
        temp = "Similar:\n"
        results = 0
        for x in range(len(emote)):
            if(realround(similarity[x]) > 54):
                results = results + 1
            if(realround(similarity[x]) > 54 and len(temp.split("\n")) <= 9):
                begin = ""
                if(emote[x].animated):
                    begin = "a"
                temp = temp + f"<{begin}:{emote[x].name}:{emote[x].id}> [{emote[x].name}]({emote[x].url}) - In {realround(similarity[x])}%\n"
        howmanyresults = len(temp.split('\n'))
        embedVar = discord.Embed(title=f"Search for {emojitoyoink} done!", description=f"I found {results} (Showing 6) results\nI think you searched for *{highestemote.name}* with {highestemoteperc}%\n{temp}", color=0x00ff00)
        embedVar.set_thumbnail(url=highestemote.url)
        await msgse.edit(content="Sent embed", embed=embedVar)
    except Exception as exesxe:
        await message.channel.send(f"Can't yoink.\nEx: {exesxe}")