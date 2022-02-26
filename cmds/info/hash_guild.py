#{}hash_guild - Sends hash of guild
import discord
import requests
import json

async def Cmd(language, serverlang, message, client):
    await message.channel.send(f"Your guild hash is *{str(hash(message.guild))}*")