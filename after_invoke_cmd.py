import discord
import discord_components
import time
import random

import asyncio

from cmds import economy

from discord_components import DiscordComponents
from discord_components import Component
from discord_components import Button
from discord_components import ButtonStyle

one = 1
two = 1
three = 1
four = 1
five = 1
votedusers = []

def Count_Votes(inter, cnt):
    if(inter.author.id in votedusers):
        pass
    else:
        if(cnt == 1):
            one = one + 1
        if(cnt == 2):
            two = two + 1
        if(cnt == 3):
            three = three + 1
        if(cnt == 4):
            four = four + 1
        if(cnt == 5):
            five = five + 1
        economy.Give_Money(inter.guild.id, inter.author.id, 20)
        print(str(cnt))
        votedusers.append(inter.author.id)

#except Exception as ecv:
    #    print(f"Unable to load after_invoke_cmd.py\n{ecv}")

async def Daily_Poll(client):
    print("Got Daily_Poll()")
    unixtim = 0
    global one, two, three, four, five
    DiscordComponents(client)
    quesno = 0
    while True:
        if(int(time.time()) - unixtim >= 60*3):
            unixtim = int(time.time())
            with open("quesno.txt", "r") as qn:
                quesno = int(qn.read())
            if(3>2):
                quesno = quesno + 1
                with open("quesno.txt", "w") as qn:
                    qn.write(str(quesno))
                with open("poll_questions.txt", "r") as jgs:
                    array = []
                    for x in jgs.readlines():
                        array.append(x)
                    nm = random.randint(0, len(array) - 1)
                    temp = array[nm]
                    embedVar = discord.Embed(
                        title="Todays question no. " + str(quesno),
                        description=temp.split("-")[0], color=0x00ffff)
                    ar = [[]]
                    for x in temp.split("-")[1].split("/"):
                        ar[0].append(Button(style=ButtonStyle.blue, label=x, custom_id=str(len(ar[0]))))
                    chanid = client.get_channel(928717155313270794)
                    await chanid.send(embed=embedVar, components=ar)
                #time.sleep(60*60*24)
                time.sleep(60*3)
                ar = [[]]
                embedVar = discord.Embed(
                    title="Results: (added one to each to prevent *division by zero* error)",
                    description=f"1. {str(one)} - {str(((one/one+two+three+four+five)*100))}%\n2. {str(two)} - {str((two/one+two+three+four+five)*100)}\n3. {str(three)} - {str((three/one+two+three+four+five)*100)}\n4. {str(four)} - {str((four/one+two+three+four+five)*100)}%\n5. {str(five)} - {str((five/one+two+three+four+five)*100)}%", color=0x00ffff)
                chanid = client.get_channel(928717155313270794)
                await chanid.send(embed=embedVar, components=ar)
        else:
            pass
        time.sleep(5)