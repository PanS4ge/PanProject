#{}bulk_dm - Sends bulk info for everyone (only for dev)
import os

import utils
import discord
import asyncio
import math
import json

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

async def Cmd(language, serverlang, message : discord.Message, client : discord.Client):
    try:
        yes = []
        no = []
        if (not (utils.admin_perms_if(message.author))):
            return await message.channel.send(language[serverlang[str(message.guild.id)]]["activity"]['not_owner'])
        await message.channel.send(f"Starting fetching guild x members")
        for guildd in client.guilds:
            #if(guildd.id == 450594207787384832 and guildd.id == 737714786711896125):
            if(guildd.member_count >= 1000):
                pass
            else:
                no.append(guildd)
                for member in guildd.members:
                    yes.append(member)
        await message.channel.send(f"Fetched {str(len(yes))} users... checking if they are unique...")

        tosend = unique(yes)
        await message.channel.send("I sent on console all servers with member count - if you don't agree to some, reset me and add to no-no list!")
        for u in no:
            print(f"Guild: {u.name}, Members: {u.member_count}, ID: {u.id}")
        await asyncio.sleep(30)
        await message.channel.send(f"Checked - {str(len(yes))} -> {str(len(tosend))}")
        await message.channel.send(f"Break every send will be {str(len(tosend) / math.ceil(15 + len(tosend)/1000))} - I will be finished in {math.ceil(len(tosend) * (len(tosend) / math.ceil(15 + len(tosend)/1000)) / 60)} minutes!\n On console will be logs who I sent!")
        for send in tosend:
            try:
                print(send)
                await send.send(message.content.replace(message.content.split(" ")[0] + " ", "") + "\nIt's a bulk message sent from dev, sorry!")
                await asyncio.sleep(len(tosend) / math.ceil(15 + len(tosend)/100))
            except:
                print("Error sending!")
        print("-----------------------------------")
        no = []
        yes = []
    except Exception as e:
        await message.channel.send(language[serverlang[str(message.guild.id)]]["global"]['error_save'])
        return await utils.save_error(message.content, os.path.basename(__file__), e)