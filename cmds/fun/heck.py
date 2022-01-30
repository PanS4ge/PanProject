#{}heck (what to heck), (who to heck) (alt. command: $sudo_heck ...) - :flushed: (alt. arg - get_pass, get_email, rem_dc_acc)
import os
import discord
import time
import asyncio

from discord.utils import get

import random

import utils

sussypass1 = ["Ilove", "Ihate", "MyMom", "MyMommaAndMyDaddyAre", "SugarDaddy", "80085", "Sussy", "IVisit"]
sussypass2 = ["Segz", "Hecking", "Begula", "Gay", "Lesbians", "Bakas", "Idiot", "Lesbians", "Porn", "Prnhub", "Cornhub"]
sussypass3 = ["1", "69", "420", "XD", "UwU", "OwO", "12345", "AmogUs"]
sussyemail = ["@gmail.com", "@ilovekids.com", "@twitch.tv", "@papaj.pl", "@pp.com", "@2137.e"]

def get_num_array(array):
    temp = 0
    for ye in array:
        temp = temp + ye
    return temp / len(array)

async def Cmd(language, serverlang, message, client):
    try:
        if("sage" in message.content.split(' ')[2].lower()):
            return await message.channel.send("You can't heck my dev")
        msgheck = await message.channel.send("☎️Calling hecker... Please wait...")
        await asyncio.sleep(random.randint(1, 10))
        await msgheck.edit(content="Hecker got it, starting heck...")
        await asyncio.sleep(3)
        await msgheck.edit(content=f"Setting target: {message.content.split(' ')[2]}'s {message.content.split(' ')[1]}")
        await asyncio.sleep(random.randint(5, 10))
        await msgheck.edit(content=f"Target locked")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Brute-forcing {message.content.split(' ')[2]}'s {message.content.split(' ')[1]}")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Freezing {message.content.split(' ')[2]}'s {message.content.split(' ')[1]}")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Sending nukes on {message.content.split(' ')[2]}'s {message.content.split(' ')[1]}")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Checking {message.content.split(' ')[2]}'s browsing history")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Checking {message.content.split(' ')[2]}'s browsing history\nFound:\n{random.randint(2, 1135)} sus websites")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Checking {message.content.split(' ')[2]}'s browsing history\nFound:\n{random.randint(2, 1135)} very sus websites")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Reporting {message.content.split(' ')[2]}'s death to his parents...")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Updating {message.content.split(' ')[2]} social status")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        await msgheck.edit(content=f"Stealing {message.content.split(' ')[2]}'s {random.randint(1, 50 * len(message.content.split(' ')[2]))} social points")
        await asyncio.sleep(random.randint(100, 1012) / 100)
        try:
            if("rem_dc_acc" in message.content):
                user = get(client.get_all_members(), id=message.author.id)
                if user:
                    await message.channel.send(f"Exception!\nException: User cannot can't be found\nRemoving message.author.id...")
                    user.edit(nick="Deleted User 2137SUS69")
                else:
                    await message.channel.send(f"Exception!\nException: User cannot can't be found")
        except:
            pass
        await msgheck.edit(content=f":tada::tada::tada:`Successful heck!`:tada::tada::tada:")
        if("get_email" in message.content):
            await message.channel.send(f"His email is {sussypass1[random.randint(0, len(sussypass1)-1)]}{sussypass2[random.randint(0, len(sussypass2)-1)]}{sussypass3[random.randint(0, len(sussypass3)-1)]}{sussyemail[random.randint(0, len(sussyemail)-1)]}")
        if("get_pass" in message.content):
            await message.channel.send(f"His password is {sussypass1[random.randint(0, len(sussypass1)-1)]}{sussypass2[random.randint(0, len(sussypass2)-1)]}{sussypass3[random.randint(0, len(sussypass3)-1)]}")
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")
