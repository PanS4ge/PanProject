#{}love_calc (Name 1) (Name 2) - Calculate how much the other person loves you <3
import discord
import os
import glob
import json
import math
import utils
import asyncio
import string
from difflib import SequenceMatcher

def similar(a, b):
    #print(str(a) + "+" + str(b))
    return SequenceMatcher(None, a, b).ratio()

async def Cmd(language, serverlang, message, client):
    try:
        POINTS = 0
        try:
            Love1 = message.content.split(" ")[1]
            Love2 = message.content.split(" ")[2]

            L1 = (len(Love1))
            L2 = (len(Love2))

            S1 = (Love1[:1])
            S2 = (Love2[:1])

            if L1 == L2:
                POINTS = POINTS + 20

            for letter in string.ascii_letters:
                if(letter in Love1 and letter in Love2):
                    POINTS = POINTS + 1

            if S1 == "a" or "e" or "i" or "o" or "u":
                POINTS = POINTS + 5
            else:
                POINTS = POINTS + 2.5
            if S2 == "a" or "e" or "i" or "o" or "u":
                POINTS = POINTS + 5
            else:
                POINTS = POINTS + 2.5

            POINTS = POINTS + math.ceil(similar(Love1, Love2) * 10)
            await message.channel.send(f"I think you love each other in {math.ceil((POINTS/(69 + math.floor((L1 + L2) / 2)))*100)}%")
        except:
            await message.channel.send("Invalid names")
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")