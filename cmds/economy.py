#{}eco earn - Earn some :fries: in PanProject economy!||{}eco bal - Check your :fries: balance in PanProject economy||{}eco ccd - Remove cooldown (only for owners)
import os
import discord

import time
import json

import random
import math

import utils

with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

eco_curr = "🍟"

async def Cmd_Earn(message):
    cd = {}
    mon = -1
    with open(f"cooldown.json", "r") as cny:
        cd = json.loads(cny.read())
        cny.close()
    try:
        print(int(time.time()) - cd[str(message.author.id)])
        if(not(int(time.time()) - cd[str(message.author.id)] >= 3600)):
            return await message.channel.send(f"""Sorry, you can run this command again in {math.floor(60 - (int(time.time()) - cd[str(message.author.id)]) / 60)} minutes.""")
    except:
        pass
    try:
        cd[str(message.author.id)] = int(time.time())
        with open(f"cooldown.json", "w") as cny:
            cny.write(json.dumps(cd, indent=4, sort_keys=True))
        cnt = {}
        econ = {}
        try:
            with open(f"msgcount/{str(message.guild.id)}.json", "r") as cny:
                cnt = json.loads(cny.read())
                cny.close()
            with open(f"economy/{str(message.guild.id)}.json", "r") as cny:
                econ = json.loads(cny.read())
                cny.close()
        except Exception as e:
            pass
        mon = math.ceil(random.randint(math.floor(int(cnt[f"{message.author.id}"]) / 1000), 100000 + int(cnt[f"{message.author.id}"])) * (int(cnt[f"{message.author.id}"]) / 1000))
        #print(mon)
        try:
            if (econ[str(message.author.id)] != 0):
                econ[str(message.author.id)] = int(econ[str(message.author.id)]) + mon
                #print(econ[str(message.author.id)])
        except Exception as e:
            econ[str(message.author.id)] = mon
        with open(f"economy/{str(message.guild.id)}.json", "w") as f:
            f.write(json.dumps(econ, indent=4, sort_keys=True))
        await message.channel.send(f"You earned {mon}{eco_curr}")

    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")

async def Cmd_Bal(message):
    try:
        with open(f"economy/{str(message.guild.id)}.json", "r") as cny:
            cnt = json.loads(cny.read())
            try:
                if (cnt[str(message.author.id)] != 0):
                    await message.channel.send(f"Your balance count is {cnt[str(message.author.id)]}{eco_curr}")
            except:
                await message.channel.send(f"No data.")
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")

async def Cmd_ClearCD(message):
    if(utils.is_owner_of_bot(message.author.id)):
        with open(f"cooldown.json", "r") as cny:
            cd = json.loads(cny.read())
            cny.close()
        cd[str(message.author.id)] = 1
        with open(f"cooldown.json", "w") as cny:
            cny.write(json.dumps(cd, indent=4, sort_keys=True))
    await message.channel.send("Removed Cooldown!")

async def Cmd_Clear_Eco(message):
    if(utils.is_owner_of_bot(message.author.id)):
        try:
            with open(f"economy/{message.guild.id}.json", "r") as cny:
                e = json.loads(cny.read())
                cny.close()
            e[str(message.content).split(" ")[1]] = 0
            with open(f"cooldown.json", "w") as cny:
                cny.write(json.dumps(e, indent=4, sort_keys=True))
            await message.channel.send(f"Cleared his {eco_curr}!")
        except:
            await message.channel.send("Invalid id")

async def Cmd_Set_Eco(message):
    if(utils.is_owner_of_bot(message.author.id)):
        try:
            with open(f"economy/{message.guild.id}.json", "r") as cny:
                e = json.loads(cny.read())
                cny.close()
            e[str(message.content).split(" ")[1]] = int(e[str(message.content).split(" ")[2]])
            with open(f"cooldown.json", "w") as cny:
                cny.write(json.dumps(e, indent=4, sort_keys=True))
            await message.channel.send(f"Set his {eco_curr}!")
        except:
            await message.channel.send("Invalid id/value")