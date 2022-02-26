#{}eco earn/crime/slut - Earn some :fries: in PanProject economy!||{}eco bal - Check your :fries: balance in PanProject economy||{}eco ccd - Remove cooldown (only for owners)||{}eco set - Set :fries: for user (only for owners)||{}eco send - Give :fries: for user||{}eco leaderboard - Check who has the most :fries: in server (arg. "global" check which server has the most :fries: globally)||{}eco chart - Gives pie chart with whole info who has the most fries on server
import os
import glob
import discord

import matplotlib.pyplot as plt
import time
import json

import collections

import BadgesManager

import random
import math

import utils

language = {}
with open(f"language_files/english.json", encoding='utf8') as data:
    language = json.load(data)

serverlang = {}
with open(f"language_server.json", encoding='utf8') as data:
    serverlang = json.load(data)

with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

eco_curr = "🍟"

async def Cmd(language, serverlang, message, client):
    if("bal" in message.content):
        await Cmd_Bal(language, serverlang, message, client)
    elif("earn" in message.content):
        await Cmd_Earn(language, serverlang, message, client, 1, 1, 0)
    elif("crime" in message.content):
        await Cmd_Earn(language, serverlang, message, client, random.randint(-2, 2), 2, 1)
    elif("slut" in message.content):
        await Cmd_Earn(language, serverlang, message, client, random.randint(-1, 1), 0.5, 2)
    elif("leaderboard" in message.content):
        await Cmd_Leaderboard(language, serverlang, message, client)
    elif("chart" in message.content):
        await Cmd_Chart(message, client)
    elif("set" in message.content and utils.is_owner_of_bot(message.author.id)):
        await Cmd_Set_Eco(language, serverlang, message, client)
    elif("send" in message.content):
        await Cmd_Send_Money(language, serverlang, message, client)
    elif("ccd" in message.content and utils.is_owner_of_bot(message.author.id)):
        await Cmd_ClearCD(language, serverlang, message, client)
    else:
        await message.channel.send("Invalid action")

def Get_Server_Net_Worth(guild):
    try:
        with open(f"ecojson/{guild}.json", "r") as f:
            data = json.loads(f.read())
            allnom = 0
            for value in data.values():
                allnom = allnom + int(value)
        return allnom
    except:
        return -1

async def Get_Server_Data(client, guild):
    eco = {}
    give_back_array = []
    with open(f"ecojson/{guild}.json", "r") as f:
        eco = json.loads(f.read())
        for i in eco.keys():
            usern = await client.fetch_user(i)
            give_back_array.append({
                "name": f"{usern.name}",
                "nw": Get_Bank(i, guild)
            })
    return give_back_array

async def Cmd_Chart(message, client):
    info = await Get_Server_Data(client, message.guild.id)
    #print(info)
    labels = []
    sizes = []
    explode = []
    for x in info:
        labels.append(x['name'].encode("ascii", "ignore").decode())
        sizes.append(x['nw'])
        explode.append(0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig("output.png")

    embedVar = discord.Embed(title=f"Here's a pie chart of server {message.guild.name}", description=".",
                             color=0x00ff00)
    file = discord.File("C:/Users/User/PycharmProjects/discord.py/output.png", filename="output.png")
    embedVar.set_image(url="attachment://output.png")
    await message.channel.send(file=file, embed=embedVar)

async def Get_Global_Data(client):
    file = []
    all_server_id = []
    for filefetch in glob.glob("ecojson/*.json"):
        all_server_id.append(str(filefetch).replace("ecojson\\", "").replace(".json", ""))
        file.append(filefetch)
    give_back_array = []
    fetched_guilds = client.guilds
    for y in fetched_guilds:
            #print(y)
        if(y == None):
            pass
        if(y.id in all_server_id):
            give_back_array.append({
                "name": y.name,
                "nw": Get_Server_Net_Worth(y.id)
            })
    return give_back_array

async def Get_Global_Balance(message):
    yesyes = 0
    for filefetch in glob.glob("ecojson/*.json"):
        try:
            ffet = {}
            with open(filefetch, "r") as ete:
                ffet = json.loads(ete.read())
                yesyes = yesyes + int(ffet[str(message.author.id)])
        except:
            pass

    if (yesyes >= 10000000 and not (BadgesManager.Have_Badge(2, message.author.id))):
        await BadgesManager.Add_Badge(2, message.author.id, message)
    elif (yesyes >= 1000000 and not (BadgesManager.Have_Badge(1, message.author.id))):
        await BadgesManager.Add_Badge(1, message.author.id, message)
    elif (yesyes >= 100000 and not (BadgesManager.Have_Badge(0, message.author.id))):
        await BadgesManager.Add_Badge(0, message.author.id, message)
    return yesyes

def sort_func(e):
  return e['nw']

async def Cmd_Earn(language, serverlang, message, client, multiplayer, mptime, action):
    cd = {}
    mon = -1
    with open(f"cooldown.json", "r") as cny:
        cd = json.loads(cny.read())
        cny.close()
    try:
        #print(int(time.time()) - cd[str(message.author.id)])
        if(not(int(time.time()) - int(cd[str(message.author.id)].split("/")[action]) >= 3600 * mptime)):
            return await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['cooldown_hour'].replace("{math.floor(60 - (int(time.time()) - cd[str(message.author.id)]) / 60)}", str(math.floor((60 * mptime) - (int(time.time()) - int(cd[str(message.author.id)].split('/')[action])) / (60 * mptime)))))
    except:
        pass
    try:
        try:
            if(action == 0): cd[str(message.author.id)] = str(int(time.time())) + "/" + cd[str(message.author.id)].split("/")[1] + "/" + cd[str(message.author.id)].split("/")[2]
            if(action == 1): cd[str(message.author.id)] = cd[str(message.author.id)].split("/")[0] + "/" + str(int(time.time())) + "/" + cd[str(message.author.id)].split("/")[2]
            if(action == 2): cd[str(message.author.id)] = cd[str(message.author.id)].split("/")[0] + "/" + cd[str(message.author.id)].split("/")[1] + "/" + str(int(time.time()))
        except KeyError:
            if (action == 0): cd[str(message.author.id)] = str(int(time.time())) + "/0/0"
            if (action == 1): cd[str(message.author.id)] = "0/" + str(
                int(time.time())) + "/0"
            if (action == 2): cd[str(message.author.id)] = "/0/0" + str(
                int(time.time()))

        with open(f"cooldown.json", "w") as cny:
            cny.write(json.dumps(cd, indent=4))
        cnt = {}
        econ = {}
        try:
            with open(f"msgcount/{str(message.guild.id)}.json", "r") as cny:
                cnt = json.loads(cny.read())
                cny.close()
            with open(f"ecojson/{str(message.guild.id)}.json", "r") as cny:
                econ = json.loads(cny.read())
                cny.close()
        except Exception as e:
            pass
        mon = math.ceil(math.ceil(random.randint(math.floor(int(cnt[f"{message.author.id}"]) / 2500), 250 * int(cnt[f"{message.author.id}"])) * (int(cnt[f"{message.author.id}"]) / 2500)) * multiplayer)
        #print(mon)
        try:
            if (econ[str(message.author.id)] != 0):
                econ[str(message.author.id)] = int(econ[str(message.author.id)]) + mon
                #print(econ[str(message.author.id)])
        except Exception as e:
            econ[str(message.author.id)] = mon
        with open(f"ecojson/{str(message.guild.id)}.json", "w") as f:
            f.write(json.dumps(econ, indent=4, sort_keys=True))
        await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['ecoearn'].replace("{mon}", str(mon)).replace("{eco_curr}", eco_curr))

    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send(language[serverlang[str(message.guild.id)]]['global']['error_save'])

async def Cmd_Leaderboard(language, serverlang, message, client):
        try:
            if("server" in message.content):
                dat = await Get_Global_Data(client)
                dat.sort(key=sort_func, reverse=True)
                embedVar = discord.Embed(title=language[serverlang[str(message.guild.id)]]['economy']['glb'], description=f"{language[serverlang[str(message.guild.id)]]['backup']['for']} {language[serverlang[str(message.guild.id)]]['backup']['bot_project_name']}", color=0x00ff00)
                amount_of_server = 10
                if(len(dat) < 10):
                    amount_of_server = len(dat)
                    #print(amount_of_server)
                for x in range(1, amount_of_server+1):
                    #print(dat)
                    #print(f"{str(x)}: {dat[x-1]['name']} with {dat[x-1]['nw']}{eco_curr}")
                    yee = '\*'
                    temp = f"{str(x)}. *{dat[x-1]['name']}* {language[serverlang[str(message.guild.id)]]['economy']['with']} *{dat[x-1]['nw']}*{eco_curr}"
                    embedVar.add_field(name=temp, value=f"{int(len(temp)) * yee}", inline=False)
                if(amount_of_server == 10):
                    if (dat[0]['name'] != message.guild.name):
                        embedVar.add_field(name=f"{language[serverlang[str(message.guild.id)]]['economy']['your_place']}", value=int(len(language[serverlang[str(message.guild.id)]]['economy']['your_place'])) * '\*', inline=False)

                    for t in range(1+amount_of_server, len(dat)):
                        if(dat[t-1]['name'] == message.guild.name):
                            temp = f"{t+amount_of_server}. {dat[t-1]['name']} with {dat[t-1]['nw']}{eco_curr}"
                            embedVar.add_field(name=f"{t+amount_of_server}. {dat[t-1]['name']} with {dat[t-1]['nw']}{eco_curr}", value=int(len(temp)) * '\*', inline=False)
                await message.channel.send(embed=embedVar)
            else:
                dat = await Get_Server_Data(client, message.guild.id)
                dat.sort(key=sort_func, reverse=True)
                embedVar = discord.Embed(title=language[serverlang[str(message.guild.id)]]['economy']['glb'], description=f"{language[serverlang[str(message.guild.id)]]['backup']['for']} {language[serverlang[str(message.guild.id)]]['backup']['bot_project_name']}", color=0x00ff00)
                amount_of_server = 10
                if(len(dat) < 10):
                    amount_of_server = len(dat)
                    #print(amount_of_server)
                for x in range(1, amount_of_server+1):
                    #print(dat)
                    #print(f"{str(x)}: {dat[x-1]['name']} with {dat[x-1]['nw']}{eco_curr}")
                    yee = '\*'
                    temp = f"{str(x)}. *{dat[x-1]['name']}* {language[serverlang[str(message.guild.id)]]['economy']['with']} *{dat[x-1]['nw']}*{eco_curr}"
                    embedVar.add_field(name=temp, value=f"{int(len(temp)) * yee}", inline=False)
                if(amount_of_server == 10):
                    if (dat[0]['name'] != message.guild.name):
                        embedVar.add_field(name=f"{language[serverlang[str(message.guild.id)]]['economy']['your_place']}", value=int(len("Your place on leaderboard")) * '\*', inline=False)

                    for t in range(1+amount_of_server, len(dat)):
                        if(dat[t-1]['name'] == message.guild.name):
                            temp = f"{t+amount_of_server}. {dat[t-1]['name']} {language[serverlang[str(message.guild.id)]]['economy']['with']} {dat[t-1]['nw']}{eco_curr}"
                            embedVar.add_field(name=f"{t+amount_of_server}. {dat[t-1]['name']} {language[serverlang[str(message.guild.id)]]['economy']['with']} {dat[t-1]['nw']}{eco_curr}", value=int(len(temp)) * '\*', inline=False)
                await message.channel.send(embed=embedVar)
        except Exception as e:
            await utils.save_error(str(message.content), os.path.basename(__file__), e)
            await message.channel.send(language[serverlang[str(message.guild.id)]]['global']['error_save'])

async def Cmd_Bal(language, serverlang, message, client):
    try:
        with open(f"ecojson/{str(message.guild.id)}.json", "r") as cny:
            cnt = json.loads(cny.read())
            try:
                if (int(cnt[str(message.author.id)]) != 0):
                    await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['ecobal'].replace("{'{:,}'.format(cnt[str(message.author.id)])}", '{:,}'.format(cnt[str(message.author.id)])).replace("{eco_curr}", eco_curr))
            except:
                await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['nodata'])
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send(language[serverlang[str(message.guild.id)]]['global']['error_save'])

async def Cmd_ClearCD(language, serverlang, message, client):
    if(utils.is_owner_of_bot(message.author.id)):
        with open(f"cooldown.json", "r") as cny:
            cd = json.loads(cny.read())
            cny.close()
        cd[str(message.author.id)] = "1/1/1"
        with open(f"cooldown.json", "w") as cny:
            cny.write(json.dumps(cd, indent=4, sort_keys=True))
    await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['ccd'])

def Get_Bank(memid, guiid):
    cd = {}
    with open(f"ecojson/{guiid}.json", "r") as cny:
        cd = json.loads(cny.read())
        cny.close()
    try:
        return cd[str(memid)]
    except:
        cd[str(memid)] = 0
        with open(f"ecojson/{guiid}.json", "w") as cny:
            cny.write(json.dumps(cd, indent=4, sort_keys=True))
        return cd[str(memid)]

async def Cmd_Send_Money(message):
    try:
        ping = message.content.split(" ")[2]
        ping = ping.replace("<@", "")
        if("!" in ping):
            ping = ping.replace("!", "")
        ping = ping.replace(">", "")
        try:
            #print(str(Get_Bank(message.author.id, message.guild.id)))
            #print(str(message.content.split(" ")[3]))
            try:
    #    if(3>2):
                with open(f"ecojson/{message.guild.id}.json", "r") as cny:
                    e = json.loads(cny.read())
                    cny.close()
                try:
                    if (int(Get_Bank(message.author.id, message.guild.id)) >= int(message.content.split(" ")[3])):
                        e[str(ping)] = int(e[str(ping)]) + int(message.content.split(" ")[3])
                        e[str(message.author.id)] = int(e[str(message.author.id)]) - int(message.content.split(" ")[3])
                    else:
                        await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['not_enough_money'])
                except:
                    if (int(Get_Bank(message.author.id, message.guild.id)) >= int(message.content.split(" ")[3])):
                        e[str(ping)] = int(message.content.split(" ")[3])
                        e[str(message.author.id)] = int(e[str(message.author.id)]) - int(message.content.split(" ")[3])
                    else:
                        await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['not_enough_money'])
                with open(f"ecojson/{message.guild.id}.json", "w") as cny:
                    cny.write(json.dumps(e, indent=4, sort_keys=True))
                ef = message.content.split(" ")[2]
                if ("<@!" in ef):
                    ef = ef.replace("<@!", "")
                elif ("<@" in ef):
                    ef = ef.replace("<@", "")
                ef = ef.replace(">", "")
                await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['send'].replace("{eco_curr}", eco_curr).replace("{message.content.split(' ')[3]}", message.content.split(' ')[3]).replace("{Get_Bank(message.author.id, message.guild.id)}", Get_Bank(message.author.id, message.guild.id)).replace("{message.content.split(' ')[2]}", message.content.split(' ')[2]).replace("{Get_Bank(ping, message.guild.id)}", Get_Bank(ping, message.guild.id)))
            except Exception:
                return await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['error'])
        except Exception:
            return await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['invalid_ping'])
    except Exception:
        return await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['invalid_args'])

async def Cmd_Set_Eco(language, serverlang, message, client):
    if(utils.is_owner_of_bot(message.author.id)):
        try:
            ping = message.content.split(" ")[2]
            if ("<@!" in ping):
                ping = ping.replace("<@!", "")
            elif ("<@" in ping):
                ping = ping.replace("<@", "")
            ping = ping.replace(">", "")
            try:
                #print(str(Get_Bank(message.author.id)))
                #print(str(message.content.split(" ")[3]))
                try:
                    with open(f"ecojson/{message.guild.id}.json", "r") as cny:
                        e = json.loads(cny.read())
                        cny.close()
                    e[str(ping)] = int(message.content.split(" ")[3])
                    with open(f"ecojson/{message.guild.id}.json", "w") as cny:
                        cny.write(json.dumps(e, indent=4, sort_keys=True))
                    ef = message.content.split(" ")[2]
                    if ("<@!" in ef):
                        ef = ef.replace("<@!", "")
                    elif ("<@" in ef):
                        ef = ef.replace("<@", "")
                    ef = ef.replace(">", "")
                    #await message.channel.send(f"You set his {eco_curr}\n{message.content.split(' ')[2]} balance: {Get_Bank(message.author.id, message.guild.id)}{eco_curr}")
                    await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['set'].replace("{eco_curr}", eco_curr).replace("{message.content.split(' ')[3]}", message.content.split(' ')[3]))
                except:
                    return await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['error'])
            except:
                return await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['invalid_ping'])
        except:
            return await message.channel.send(language[serverlang[str(message.guild.id)]]['economy']['invalid_args'])

async def Give_Money(guild, ping, amount):
    with open(f"ecojson/{guild}.json", "r") as cny:
        e = json.loads(cny.read())
        cny.close()
    try:
        e[str(ping)] = int(e[str(ping)]) + int(amount)
    except:
        e[str(ping)] = int(amount)
    with open(f"ecojson/{guild}.json", "w") as cny:
        cny.write(json.dumps(e, indent=4, sort_keys=True))

async def Give_Not_Add_Money(guild, ping, amount):
    with open(f"ecojson/{guild}.json", "r") as cny:
        e = json.loads(cny.read())
        cny.close()
    try:
        #print(e[str(ping)])
        e[str(ping)] = int(e[str(ping)]) + int(amount)
        #print(e[str(ping)])
    except:
        pass
    with open(f"ecojson/{guild}.json", "w") as cny:
        cny.write(json.dumps(e, indent=4, sort_keys=True))


async def Set_Money(guild, ping, amount):
    with open(f"ecojson/{guild}.json", "r") as cny:
        e = json.loads(cny.read())
        cny.close()
    e[str(ping)] = int(amount)
    with open(f"ecojson/{guild}.json", "w") as cny:
        cny.write(json.dumps(e, indent=4, sort_keys=True))