import os
import time
import urllib

import math
import random

import json

from difflib import SequenceMatcher

from cmds import economy

import discord

import utils

async def Get_Link_From_Msg(message):
    yes = str(message.content)
    if("http" in yes and "." in yes):
        arr = yes.split(" ")
        for ar in arr:
            if (ar.startswith("http") and "." in yes):
                return ar
    else:
        return False

def similar(a, b):
    #print(str(a) + "+" + str(b))
    return SequenceMatcher(None, a, b).ratio()

def get_num_array(array):
    temp = 0
    for ye in array:
        temp = temp + ye
    return temp / len(array)

async def CheckMsg(message):
    try:
        await AntiFishing(message)

        config = {}
        with open(f"config.json", encoding='utf8') as data:
            config = json.load(data)
        if(message.author.id in config["gbans"]):
            return

        await Count_Message(message)
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")

async def Count_Message(message):
    if(not(message.author.bot)):
        cnt = {}
        monet = random.randint(1, 250)
        if(monet == random.randint(1, 250)):
            await message.reply(f"Congrats! You found {monet}:fries: laying on <#{message.channel.id}>!")
            await economy.Give_Money(message.guild.id, message.author.id, monet)
    try:
        with open(f"msgcount/{str(message.guild.id)}.json", "r") as cny:
            cnt = json.loads(cny.read())
            cny.close()
    except Exception as e:
        pass
    try:
        if(cnt[str(message.author.id)] != 0):
            cnt[str(message.author.id)] = int(cnt[str(message.author.id)]) + 1
            #print(cnt[str(message.author.id)])
    except Exception as e:
        cnt[str(message.author.id)] = 1
    with open(f"msgcount/{str(message.guild.id)}.json", "w") as f:
        f.write(json.dumps(cnt, indent=4, sort_keys=True))

async def AntiFishing(message):
    if(message.channel.id == 927869165753229312):
        return

    config = {}
    with open(f"config.json", encoding='utf8') as data:
        config = json.load(data)

    if(message.author.id == config["id_normal"]):
        return
    msglink = await Get_Link_From_Msg(message)
    if(msglink == False):
        return

    msgscan = await message.reply("Starting scan of link...")

    with open("link.txt", "r") as lin:
        file = lin.readlines()
    with open("trailingslash.txt", "r") as lin:
        file2 = lin.readlines()

    rdy = []
    hgdo = []
    beg = ["", "http://", "https://", "http://www.", "https://www."]

    for x in beg:
        if(x in msglink):
            #print(f"{x} in {msglink}")
            msglink = msglink.replace(str(x), "")

    msglink = str(msglink.split("/")[0]) + "/" + str(msglink.split("/")[1])

    for website in file:
        for trailsl in file2:
            url = str(website).replace("\n", "") + str(trailsl).replace("\n", "")
            per = similar(url, msglink)
            rdy.append(per)
            hgdo.append(per)
    await msgscan.edit(content=f"""Starting scan of link ({msglink})\nCurrently comparing link to my database for sus variants""")

    i = 0
    j = 0
    with open("malterms.txt", "r") as op:
        for x in op.readlines():
            if(x in str(message.content)):
                i = i + 100
                rdy.append(i)
                j = j + 1

    per = get_num_array(rdy)
    if(per > 0.3):
        if(per < 0.5):
            await msgscan.edit(content=f"Kicked {str(message.author)}, because user posted scam link\nSimilarity in database {math.floor(per * 150)}%\nAdditional \"Red flags\": {j}")
            try:
                await message.author.kick(reason=f"Posted scam link ({msglink})")
            except:
                await msgscan.edit(content=f"Kicked {str(message.author)}, because user posted scam link\nSimilarity in database {math.floor(per * 150)}%\nAdditional \"Red flags\": {j}\n*Can't kick*")
        else:
            await msgscan.edit(content=f"Banned {str(message.author)}, because user posted scam link\nSimilarity in database {math.floor(per * 150)}%\nAdditional \"Red flags\": {j}")
            try:
                await message.author.ban(reason=f"Posted scam link ({msglink})")
            except:
                await msgscan.edit(content=f"Banned {str(message.author)}, because user posted scam link\nSimilarity in database {math.floor(per * 150)}%\nAdditional \"Red flags\": {j}\n*Can't ban*")
        with open("link.txt", "r") as link1:
            with open("trailingslash.txt", "r") as link2:
                if(msglink.split("/")[0] in link1.readlines() and msglink.split("/")[1] in link2.readlines()):
                    with open("link.txt", "a") as link:
                        link.write("\n" + msglink.split("/")[0])
                    with open("trailingslash.txt", "a") as link:
                        link.write("\n" + "/" + msglink.split("/")[1])
        await message.delete()
    else:
        await msgscan.edit(content=f"Scanned message - Scam link possibility {math.floor(per*150)}%")

