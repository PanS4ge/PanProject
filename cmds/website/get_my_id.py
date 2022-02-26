#{}get_my_id - Gives your ID
import discord
import requests
import json

async def Cmd(language, serverlang, message, client):
    await message.channel.send(f"Your ID is *{message.author.id}*")