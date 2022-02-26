#{}am_i_on_discord - Uses extreme technology needed to check if you are on discord
import discord
import json
import asyncio
import random

async def Cmd(language, serverlang, message, client):
    aiod = await message.channel.send("<a:loading:936978619639668787> Preparing check...")
    await asyncio.sleep(2)
    await aiod.edit(content="<a:loading:936978619639668787> Using quantum physics...")
    await asyncio.sleep(5)
    await aiod.edit(content="<a:loading:936978619639668787> Hecking discord servers...")
    await asyncio.sleep(3)
    await aiod.edit(content="<a:loading:936978619639668787> Hecked, searching for user")
    await asyncio.sleep(1)
    await aiod.edit(content=f"<a:loading:936978619639668787> Found {message.author}.")
    await asyncio.sleep(2)
    await aiod.edit(content=f"<a:loading:936978619639668787> Preparing results...")
    await asyncio.sleep(2)
    temp = random.randint(1, 69)
    if(temp == 21):
        await aiod.edit(content=f"Nope, you are on Samsung Smart Fridge.")
    else:
        await aiod.edit(content=f"Yes, you are on Discord.")