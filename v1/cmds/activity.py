#{}activity - Change activity of bot (only for dev)
import utils
import discord
import json

async def Cmd(language, serverlang, message, client):
    try:
        if (not (utils.admin_perms_if(message.author))):
            return await message.channel.send(language[serverlang[str(message.guild.id)]]["activity"]['not_owner'])
        array_of_args = []
        array_of_args = message.content.split(" ")
        func = array_of_args[1]

        if("_" in func):
            func_array = []
            func_array = func.split("_")
            #print(str(message.content).replace(array_of_args[0], "").replace(array_of_args[1], ""))
            await client.change_presence(activity=discord.Streaming(name=str(message.content).replace(array_of_args[0], "").replace(array_of_args[1], ""), url=func_array[1]))
        if(func == "Game"):
            await client.change_presence(activity=discord.Game(name=str(message.content).replace(array_of_args[0], "").replace(array_of_args[1], "")))
        if(func == "Watching"):
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(message.content).replace(array_of_args[0], "").replace(array_of_args[1], "")))
        if(func == "Listening"):
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(message.content).replace(array_of_args[0], "").replace(array_of_args[1], "")))

    except Exception as e:
        return await message.channel.send(language[serverlang[str(message.guild.id)]]["activity"]['error'])