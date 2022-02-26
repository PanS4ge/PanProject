#{}search_and_dm - Searches for user globally and sends them a dm (only for dev)
import utils
import discord
import asyncio
import math
import json

async def Cmd(language, serverlang, message : discord.Message, client : discord.Client):
    yes = []
    try:
        if (not (utils.admin_perms_if(message.author))):
            return await message.channel.send(language[serverlang[str(message.guild.id)]]["activity"]['not_owner'])
        await message.channel.send(f"Starting search")
        for guildd in client.guilds:
            for member in guildd.members:
                yes.append(member.id)
        await message.channel.send(f"Fetched {str(len(yes))} users... Searching user...")

        if(int(message.content.split(" ")[1]) in yes):
            send = discord.Member
            for guildd in client.guilds:
                try:
                    send = await guildd.fetch_member(int(message.content.split(" ")[1]))
                except:
                    pass
            try:
                await send.send(message.content.replace(message.content.split(" ")[0] + " ", "").replace(message.content.split(" ")[1] + " ", "") + "\nIt's a message sent from dev, I searched for you on every server, sorry!")
                await message.channel.send(f"Found {send}!")
            except:
                await message.channel.send(f"Found {send}, but couldn't send him")
            yes = []
        else:
            await message.channel.send("Couldn't find him :(")
    except Exception as e:
        return await message.channel.send(language[serverlang[str(message.guild.id)]]["global"]['error_save'])