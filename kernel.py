import asyncio
import math
import random
import threading
import glob
import time

import dislash
import power

import discord_components
import psutil
import importlib

import matplotlib.pyplot as plt

import discord
from discord_together import DiscordTogether

import json
import os

import requests
from discord_components import Select, SelectOption
from discord_components import Button, ButtonStyle
from discord_components import DiscordComponents

#from dislash import slash_commands
#from dislash import *

from dislash import InteractionClient, Option, OptionType

import update_votes
import BadgesManager
import after_invoke_cmd

import utils, pmc
import o1k_msg

updatetimeout = 0
users_on_cooldown = []

def updateimportcmds():
    print("Starting import")
    print(f'-----------------------------')
    for foldersa in glob.glob(f"cmds/*/"):
        # print(foldersa)
        if (int(len(glob.glob(f"{foldersa}/*/"))) > 2):
            # print(int(len(glob.glob(f"{foldersa}/*/"))))
            for foldererer in glob.glob(f"{foldersa}/*/"):
                for folderer in glob.glob(f"{foldererer}/*.py"):
                    # print(folderer)
                    package = folderer.replace(foldererer, "").replace(".py", "")
                    try:
                        backslashes = "\\"
                        globals()[package] = importlib.import_module(f'{foldererer.replace(backslashes, ".")}{package}')
                        print(f'{foldererer.replace(backslashes, ".")}{package} was imported!')
                    except Exception as exept:
                        print(f'-----------------------------')
                        print(f'{foldererer.replace(backslashes, ".")}{package} had error importing')
                        print(exept)
                        print(f'-----------------------------')
                    except:
                        print(package + "wasn't registered due to error")
        else:
            for x in glob.glob(f"{foldersa}/*.py"):
                package = x.replace(foldersa, "").replace(".py", "")
                try:
                    backslashes = "\\"
                    globals()[package] = importlib.import_module(f'{foldersa.replace(backslashes, ".")}{package}')
                    print(f'{foldersa.replace(backslashes, ".")}{package} was imported!')
                except Exception as exept:
                    print(f'-----------------------------')
                    print(f'{foldersa.replace(backslashes, ".")}{package} had error importing')
                    print(exept)
                    print(f'-----------------------------')
                except:
                    print(package + "wasn't registered due to error")
    print(f'-----------------------------')
    for x in glob.glob(f"dev/*.py"):
        package = x.replace("dev\\", "").replace(".py", "")
        try:
            backslashes = "\\"
            globals()[package] = importlib.import_module(f'dev.{package}')
            print(f'dev.{package} was imported!')
        except Exception as exept:
            print(f'-----------------------------')
            print(f'dev.{package} had error importing')
            print(exept)
            globals()[package] = "Didnt import due to error: " + exept
            print(f'-----------------------------')
    print(f'-----------------------------')
    print(f'Ending import')

def importcmds():
    print("Starting import")
    print(f'-----------------------------')
    for foldersa in glob.glob(f"cmds/*/"):
        #print(foldersa)
        if(int(len(glob.glob(f"{foldersa}/*/"))) > 2):
            #print(int(len(glob.glob(f"{foldersa}/*/"))))
            for foldererer in glob.glob(f"{foldersa}/*/"):
                for folderer in glob.glob(f"{foldererer}/*.py"):
                    #print(folderer)
                    package = folderer.replace(foldererer, "").replace(".py", "")
                    try:
                        backslashes = "\\"
                        globals()[package] = importlib.import_module(f'{foldererer.replace(backslashes, ".")}{package}')
                        print(f'{foldererer.replace(backslashes, ".")}{package} was imported!')
                    except Exception as exept:
                        print(f'-----------------------------')
                        print(f'{foldererer.replace(backslashes, ".")}{package} had error importing')
                        print(exept)
                        print(f'-----------------------------')
                    except:
                        print(package + "wasn't registered due to error")
        else:
            for x in glob.glob(f"{foldersa}/*.py"):
                package = x.replace(foldersa, "").replace(".py", "")
                try:
                    backslashes = "\\"
                    globals()[package] = importlib.import_module(f'{foldersa.replace(backslashes, ".")}{package}')
                    print(f'{foldersa.replace(backslashes, ".")}{package} was imported!')
                except Exception as exept:
                    print(f'-----------------------------')
                    print(f'{foldersa.replace(backslashes, ".")}{package} had error importing')
                    print(exept)
                    print(f'-----------------------------')
                except:
                    print(package + "wasn't registered due to error")
    print(f'-----------------------------')
    for x in glob.glob(f"dev/*.py"):
        package = x.replace("dev\\", "").replace(".py", "")
        try:
            backslashes = "\\"
            globals()[package] = importlib.import_module(f'dev.{package}')
            print(f'dev.{package} was imported!')
        except Exception as exept:
            print(f'-----------------------------')
            print(f'dev.{package} had error importing')
            print(exept)
            globals()[package] = "Didnt import due to error: " + exept
            print(f'-----------------------------')
    print(f'-----------------------------')
    print(f'Ending import')

importcmds()
import get_message_image
from io import BytesIO

panproj = ["normal", "manager"]
maintence = False

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

language = {}
with open(f"language_files/english.json", encoding='utf8') as data:
    language = json.load(data)
    #print(language)

serverlang = {}
with open(f"language_server.json", encoding='utf8') as data:
    serverlang = json.load(data)

keys = {}
with open(f"serialkey.json", encoding='utf8') as data:
    keys = json.load(data)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

lastissuedcmd = ""

usagecount = 0
ratio = 0

def keep_usage_ratio():
    usagecount = 0
    time.sleep(3600)
    ratio = usagecount / 60

@client.event
async def on_member_join(member):
    with open("banned_bots.txt", "r") as rer:
        for x in rer.readlines():
            if(str(member.id) == x.replace("\n", "")):
                await member.kick(reason="You just added destructive bot!")
    welcomechan = {}
    with open("settings/welcome_channel.json", "r") as welcom:
        welcomechan = json.loads(welcom.read())
    try:
        try:
            if(welcomechan[str(member.guild.id)]["image_welcome"].lower() == "true"):
                with BytesIO() as image_binary:
                    get_message_image.get_welcome(member).save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await client.get_channel(int(welcomechan[str(member.guild.id)]["join_channel"])).send(content=f"<@!{member.id}>", file=discord.File(fp=image_binary, filename='image.png'))
            else:
                await client.get_channel(int(welcomechan[str(member.guild.id)]["join_channel"])).send(f'Welcome <@!{member.id}> on the server!')
        except KeyError:
            await client.get_channel(int(welcomechan[str(member.guild.id)]["join_channel"])).send(f'Welcome <@!{member.id}> on the server!')
        if(member.guild.id == 925744274706939956):
            role = discord.utils.get(client.get_guild(925744274706939956).roles, id=927854767894593556)
            await member.add_roles(role)
    except:
        return

@client.event
async def on_member_leave(member):
    welcomechan = {}
    with open("settings/welcome_channel.json", "r") as welcom:
        welcomechan = json.loads(welcom.read())
    try:
        try:
            if(welcomechan[str(member.guild.id)]["image_leave"].lower() == "true"):
                with BytesIO() as image_binary:
                    get_message_image.get_leave(member).save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await client.get_channel(int(welcomechan[str(member.guild.id)]["leave_channel"])).send(content=f"<@!{member.id}>", file=discord.File(fp=image_binary, filename='image.png'))
            else:
                await client.get_channel(int(welcomechan[str(member.guild.id)]["leave_channel"])).send(f'<@!{member.name}> left us')
        except KeyError:
            await client.get_channel(int(welcomechan[str(member.guild.id)]["leave_channel"])).send(f'<@!{member.name}> left us')
    except:
        return



@client.event
async def on_ready():
    global maintence
    global whichone
    print("Starting necessary functions...")
    DiscordComponents(client)
    #print("0.5/2")
    #slash = slash_commands.SlashClient(client)
    #print("1/2")
    await client.change_presence(activity=discord.Game(name=f"Bot is booting, please wait..."))
    #a = threading.Thread(target=keep_usage_ratio)
    #a.setDaemon(True)
    #a.start()
    print("DONE.")
    print("StatusLoop() started!")
    await StatusLoop()
    #await after_invoke_cmd.Daily_Poll(client)

async def StatusLoop():
    while True:
        memcount = 0
        for guildd in client.guilds:
            for member in guildd.members:
                memcount = memcount + 1
        status = ["?help", f"I'm on {str(len(client.guilds))} guilds!", f"My global member count is {memcount}", f"My shard count is {client.shard_count}"]
        for x in status:
            #print(f"My new status: {x}")
            with open("activity", "r") as w:
                #print(w.read())
                if(w.read() == "F"):
                    await client.change_presence(activity=discord.Game(name=x))
            await asyncio.sleep(45)
            await update_votes.Update(client)


@client.event
async def on_guild_join(guild):
    bltoken = "eb75f59765a354ae5b991a99ff9e885a2dcf6b4d"
    headersbl = {
        #"Content-Type": "application/json",
        "Authorization": f"Token {bltoken}"
    }
    data = {"server_count": len(client.guilds), "shard_count": client.shard_count}
    # if(blgb['server_count'] != len(client.guilds)):
    req = requests.post("https://api.bladelist.gg/bots/915657093862817802/", data=json.dumps(data), headers=headersbl)
    chanlog = client.get_channel(937665605362925669)
    await chanlog.send("<:yeee:928675155465621525> Updated Bladelist!")

    guildname = guild.name
    guildid = guild.id
    temp = {}
    try:
        if(f"ecojson/{guildid}.json"):
            with open(f"ecojson/{guildid}.json", "w") as yee:
                yee.write(json.dumps(temp))
            #os.remove(f"ecojson/{guildid}.json")
    except:
        pass
    try:
        if(f"msgcount/{guildid}.json"):
            with open(f"msgcount/{guildid}.json", "w") as yee:
                yee.write(json.dumps(temp))
    except:
        pass
    try:
        serverlang[str(guild.id)] = 'eng'
        with open("language_server.json", "w") as welcom:
            welcom.write(json.dumps(serverlang, indent=4))
    except:
        pass

    #try:
    #    if(f"backup/{guildid}.json"):
    #        with open(f"msgcount/{guildid}.json", "w") as yee:
    #            yee.write(json.dumps(temp))
    #except:
    #    pass
    chanid = client.get_channel(927848602821349386)
    #link = client.create_invite(destination=guild, xkcd=True, max_age=0, max_uses=0)

    await chanid.send(language['eng']["kernel"]['added_server'].replace("{guildname}", guildname).replace("{guildid}", str(guildid)))#\nHere's link to join {link}\n")

@client.event
async def on_guild_remove(guild):
    badge = {}
    with open(f"partnered_server_id.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    try:
        badge['badges'].remove(guild.id)
        await client.get_channel(936200778102743081).send(
            f"<:server_partner:928283450723672085> PARTNER ALERT!\nOur lost partner: {client.get_guild(guild.id).name}\n*It's automatic message, reason: Kicked.*")

    except:
        pass
    with open(f"partnered_server_id.json", "w") as cny:
        cny.write(json.dumps(badge, indent=4))
        cny.close()

    bltoken = "eb75f59765a354ae5b991a99ff9e885a2dcf6b4d"
    headersbl = {
        #"Content-Type": "application/json",
        "Authorization": f"Token {bltoken}"
    }
    data = {"server_count": len(client.guilds), "shard_count": client.shard_count}
    # if(blgb['server_count'] != len(client.guilds)):
    req = requests.post("https://api.bladelist.gg/bots/915657093862817802/", data=json.dumps(data), headers=headersbl)
    chanlog = client.get_channel(937665605362925669)
    await chanlog.send("<:yeee:928675155465621525> Updated Bladelist!")

    guildname = guild.name
    guildid = guild.id
    try:
        if(f"ecojson/{guildid}.json"):
            os.remove(f"ecojson/{guildid}.json")
    except:
        pass
    try:
        if(f"msgcount/{guildid}.json"):
            os.remove(f"msgcount/{guildid}.json")
    except:
        pass
    #try:
    #    if(f"backup/{guildid}.json"):
    #        os.remove(f"backup/{guildid}.json")
    #except:
    #    pass
    chanid = client.get_channel(927848602821349386)
    await chanid.send(language['eng']["kernel"]['kicked_server'].replace("{guildname}", guildname).replace("{guildid}", str(guildid)))

@client.event
async def on_message(message):
    #if(message.guild.id == 811602684552544286):
    #    if(message.author.id == 540251806500913178):
    #        await message.delete()
    #        await message.channel.send(f":mask: <@!{message.author.id}> próbował coś powiedzieć.\nTutaj tekst w spoilerze ||{message.content}||")

    if message.author == client.user:
        return
    if (message.channel.type == discord.ChannelType.private):
        return
    '''
    if (str(message.content).startswith("Obcy: ") and message.channel.id == 940315229387120741):
        try:
            chan2 = client.get_channel(940319110842159194)
            await chan2.send(str(message.content).replace("Obcy: ", ""))
        except:
            pass
    elif (str(message.content).startswith("Obcy: ") and message.channel.id == 940319110842159194):
        try:
            chan2 = client.get_channel(940315229387120741)
            await chan2.send(str(message.content).replace("Obcy: ", ""))
        except:
            pass
    '''
    if message.author.bot:
        return
    try:
        if(language[serverlang[str(message.guild.id)]]["kernel"]["kernel_error"]):
            pass
    except KeyError:
        #await select_language(message)
        serverlang[str(message.guild.id)] = 'eng'
        with open("language_server.json", "w") as welcom:
            welcom.write(json.dumps(serverlang, indent=4))
            #print("language_server saved")

    prefix = {}
    with open("prefix.json", "r") as welcom:
        prefix = json.loads(welcom.read())
    useprefix = ""
    try:
        useprefix = prefix[str(message.guild.id)]
    except KeyError:
        useprefix = "?"

    source = power.PowerManagement().get_providing_power_source_type()
    if(source == power.POWER_TYPE_BATTERY):
        global maintence
        if (maintence == True):
            maintence = False
            await client.get_channel(927982475379097620).send(
                language[serverlang[str(message.guild.id)]]["kernel"]['maintencemodeonoff'])
        elif (maintence == False):
            maintence = True
            await client.get_channel(927982475379097620).send(
                language[serverlang[str(message.guild.id)]]["kernel"]['maintencemodeoffon'])

    if(f"<@!{client.user.id}>" in message.content):
        await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["on_ping_wakeup"].replace(
            "{config[f'prefix_{whichone}']}", useprefix))
    #print(str(message.content).startswith(prefix[str(message.guild.id)]))
    #print(message.content)
    if (message.channel.id == 929668126654750741 and str(message.content) == "!d bump"):
        if (not (BadgesManager.Have_Badge(12, message.author.id))):
            await message.channel.send(
                language[serverlang[str(message.guild.id)]]["kernel"]["dbump_first"].replace("{message.author.id}",
                                                                                             str(message.author.id)))
            await eco.Give_Money(message.guild.id, message.author.id, 1000)
            await BadgesManager.Add_Badge(12, message.author.id, message)
        else:
            await message.channel.send(
                language[serverlang[str(message.guild.id)]]["kernel"]["dbump"].replace("{message.author.id}",
                                                                                       str(message.author.id)))
            await eco.Give_Money(message.guild.id, message.author.id, 500)
        info = await message.channel.history(limit=None).flatten()
        labels = []
        sizes = []
        explode = []
        for x in info:
            if(x.author.id != 302050872383242240 and x.author.id != 915657093862817802 and not(x.author.name.encode("ascii", "ignore").decode() in labels)):
                temp = 0
                for y in info:
                    #print(f"{x.author} / {x.content}, {y.author} / {y.content} - temp = {temp}, !d bump? - {y.content.startswith('!d bump')}")
                    if(y.author.id == x.author.id and y.content.startswith("!d bump")):
                        temp = temp + 1
                labels.append(str(x.author.name).encode("ascii", "ignore").decode())
                sizes.append(temp + 1)
                explode.append(0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        plt.savefig("output.png")

        embedVar = discord.Embed(title=f"Here's a chart of people writing !d bump", description=".",
                                 color=0x00ff00)
        file = discord.File("C:/Users/User/PycharmProjects/discord.py/output.png", filename="output.png")
        embedVar.set_image(url="attachment://output.png")
        try:
            chan = client.get_channel(937691235404091392)
            msgtodel = await chan.history(limit=None).flatten()
            for x in msgtodel:
                await x.delete()
            await chan.send(content="Look under (all of them got +1 to reduce 0)", file=file, embed=embedVar)
        except:
            pass
    if ("👉" in str(message.content) and "👈" in str(message.content) or "👉" in str(message.content) and "👈" in str(message.content) and"🥺" in str(message.content)):
        await message.channel.send(":rotating_light: **! PICK ME ALERT !** :rotating_light:")
    try:
        if (str(message.content).startswith(useprefix)):
            isgbanned = False
            reason = ""
            with open("gbans.json", "r") as gb:
                jsgb = json.loads(gb.read())
                for gbgb in jsgb:
                    if(gbgb['id'] == message.author.id):
                        isgbanned = True
                        reason = gbgb['reason']
            if(not(maintence)):
                if (not (isgbanned)):
                    await handler(message)
                else:
                    await message.channel.send("Bro - you got GBANNED,\nreason: " + reason)
            else:
                await message.channel.send(language['eng']["kernel"]['maintencemode'])
    except Exception as ex:
        await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["kernel_error"])
        await utils.save_error(
            f"Kernel ({client.user}) / Crashed by {message.author.name} ({message.author.id})",
            os.path.basename(__file__), ex)
        exit(ex)

    #await pmc.CheckMsg(language, serverlang, message)
    try:
        await Reload_Badges_Roles(client)
    except:
        pass

def lookup(path):
    obj = globals()
    for element in path.split('.'):
        #print(element)
        try:
            obj = obj[element]
        except KeyError:
            obj = getattr(obj, element)
    return obj

async def Reload_Badges_Roles(client : discord.Client):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    for x in badge["badge"]:
        if (len(x["owners"]) != 0):
            for y in x["owners"]:
                try:
                    guiid = client.get_guild(925744274706939956)
                    poo = guiid.get_role(x["role_id"])
                    pee = guiid.get_member(y)
                    #print(f"Added {pee.name} to {x['name']} badge owners")
                    await pee.add_roles(poo)
                except KeyError:
                    guiid = client.get_guild(925744274706939956)
                    role = await guiid.create_role(name=x["name"] + " badge owners")
                    x["role_id"] = role.id
                    if (len(x["owners"]) != 0):
                        for y in x["owners"]:
                            try:
                                guiid = client.get_guild(925744274706939956)
                                pee = guiid.get_member(y)
                                await pee.add_roles(role)
                                #print(f"Added {pee.name} to {x['name']} badge owners")
                            except:
                                pass
                                #print("Error in there")
                        await asyncio.sleep(5)
                    #print(f"Created {x['name']} badges owners")
                except AttributeError:
                    pass
                with open(f"badges.json", "w") as cny:
                    cny.write(json.dumps(badge))
                    cny.close()
        await asyncio.sleep(2)

async def select_language(message):
    await message.channel.send("Here will be language selector")

async def handler(message):
        if(True):
            global usagecount, lastissuedcmd
            username = str(message.author).split('#')[0]
            usertag = str(message.author).split('#')[1]
            userid = str(message.author.id)
            user_msg = str(message.content)
            channel = str(message.channel.name)
            #with open("message_log.txt", "a") as log:
            #    log.write(f"({client.user}): " + username + "#" + usertag + " (" + userid + "): " + user_msg + " / " + message.guild.name + " -> #" + channel + "\n")

            global whichone
            whichone = ""
            for panp in panproj:
                if (config[f'token_{panp}'] == toktocheck):
                    whichone = panp
            #print(whichone)
            if (f"<@!{config[f'id_manager']}>" in message.content):
                prefix = {}
                with open("prefix.json", "r") as welcom:
                    prefix = json.loads(welcom.read())
                useprefix = ""
                try:
                    useprefix = prefix[str(message.guild.id)]
                except KeyError:
                    useprefix = "?"
                await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["on_ping_wakeup"].replace("{config[f'prefix_{whichone}']}", useprefix))

            if(True):#whichone == "normal"):
                #print(message.content)
                #print(user_msg.startswith(config[f'prefix_manager']))
                #if (not message.author.id in config["owners"]):
                #    return await message.channel.send("Only my dev can use me - I'm only testing, to deliver bot without bugs!")
                #else:
                    #if(user_msg.startswith(config[f'prefix_manager'] + "generate") or user_msg.startswith(config[f'prefix_manager'] + "gen")):
                    #    await generate.Cmd(message, user_msg)
                    for folder in glob.glob(f"C:/Users/User/PycharmProjects/discord.py/cmds/*/", recursive=True):
                        if(int(len(glob.glob(f"{folder}/*/"))) > 2):
                            for folders in glob.glob(f"{folder}/*/"):
                                for cmdsname in glob.glob(f"{folders}/*.py"):
                                    package = cmdsname.replace(f"{folders}", "").replace("\\", "").replace(".py", "")
                                    # print(package)
                                    prefix = {}
                                    with open("prefix.json", "r") as welcom:
                                        prefix = json.loads(welcom.read())
                                    useprefix = ""
                                    try:
                                        useprefix = prefix[str(message.guild.id)]
                                    except KeyError:
                                        useprefix = "?"
                                    if(user_msg.startswith(useprefix + "aport") and message.guild.id == 878262061581357106):
                                        await random.choice(message.guild.text_channels).send("`kość`\n*dla <@!850647239475068973>")
                                        return
                                    if (user_msg.startswith(useprefix + package)):
                                        # print(" F O U N D I T")
                                        # yes = await eval(f"{package}.Cmd(message='{message}', client='{client}', whichone='{whichone}')")
                                        try:
                                            if(message.author in users_on_cooldown):
                                                finalcd = 15
                                                if (message.guild.member_count >= 100):
                                                    finalcd = finalcd - 5
                                                if (message.guild.member_count >= 1000):
                                                    finalcd = finalcd - 5
                                                await message.channel.send(f"You are on cooldown, wait {finalcd} seconds from your last command.")
                                            else:
                                                await message.add_reaction("<:pikalike:936375124356128878>")
                                                if(lookup(package) != "UNLOADED"):
                                                    users_on_cooldown.append(message.author)
                                                    if("music" in folder):
                                                        await message.channel.send(":warning: Warning :warning:\nMUSIC MODULE IS IN EXPERIMENTAL STATE.")
                                                    await getattr(lookup(package), "Cmd")(language, serverlang, message, client)
                                                    usagecount = usagecount + 1
                                                    lastissuedcmd = message.content
                                                    finalcd = 15
                                                    if(message.guild.member_count >= 100):
                                                        finalcd = finalcd - 5
                                                    if(message.guild.member_count >= 1000):
                                                        finalcd = finalcd - 5
                                                    await asyncio.sleep(finalcd)
                                                    users_on_cooldown.remove(message.author)
                                                else:
                                                    await message.channel.send("This command was unloaded")
                                        except Exception as exex:
                                            print(exex)
                                            await message.channel.send(
                                                f":warning: {package} didn't import due to error")
                                            await client.get_user(850647239475068973).send(
                                                f":warning: {package} didn't import due to error\n{message.author} discovered it!\nException: {exex}")
                        else:
                            for cmdsname in glob.glob(f"{folder}/*.py"):
                                package = cmdsname.replace(f"{folder}", "").replace("\\", "").replace(".py", "")
                                #print(package)
                                prefix = {}
                                with open("prefix.json", "r") as welcom:
                                    prefix = json.loads(welcom.read())
                                useprefix = ""
                                try:
                                    useprefix = prefix[str(message.guild.id)]
                                except KeyError:
                                    useprefix = "?"
                                if (user_msg.startswith(useprefix + package)):
                                    #print(" F O U N D I T")
                                    #yes = await eval(f"{package}.Cmd(message='{message}', client='{client}', whichone='{whichone}')")
                                    try:
                                        if (message.author in users_on_cooldown):
                                            finalcd = 15
                                            if (message.guild.member_count >= 100):
                                                finalcd = finalcd - 5
                                            if (message.guild.member_count >= 1000):
                                                finalcd = finalcd - 5
                                            await message.channel.send(
                                                f"You are on cooldown, wait {finalcd} seconds from your last command.")
                                        else:
                                            await message.add_reaction("<:pikalike:936375124356128878>")
                                            if (lookup(package) != "UNLOADED"):
                                                users_on_cooldown.append(message.author)
                                                if ("music" in folder):
                                                    await message.channel.send(
                                                        ":warning: Warning :warning:\nMUSIC MODULE IS IN EXPERIMENTAL STATE.")
                                                await getattr(lookup(package), "Cmd")(language, serverlang, message,
                                                                                      client)
                                                usagecount = usagecount + 1
                                                lastissuedcmd = message.content
                                                finalcd = 15
                                                if (message.guild.member_count >= 100):
                                                    finalcd = finalcd - 5
                                                if (message.guild.member_count >= 1000):
                                                    finalcd = finalcd - 5
                                                await asyncio.sleep(finalcd)
                                                users_on_cooldown.remove(message.author)
                                        usagecount = usagecount + 1
                                        lastissuedcmd = message.content
                                    except Exception as exex:
                                        await message.channel.send(f":warning: {package} didn't import due to error")
                                        await client.get_user(850647239475068973).send(f":warning: {package} didn't import due to error\n{message.author} discovered it!\nException: {exex}")
                        '''
                    if(user_msg.startswith(config[f'prefix_manager'] + "help")):
                        await help.Cmd(message, whichone)
                    if(user_msg.startswith(config[f'prefix_manager'] + "exec")):
                        await exec.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_manager'] + "devtoolkit")):
                        await devtoolkit.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "mc_pfp")):
                        await mc_pfp.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "ping")):
                        await ping.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "guildinfo")):
                        await guildinfo.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "random_prntsc")):
                        await random_prntscr.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "yt_stats")):
                        await yt_stats.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "memberinfo")):
                        await memberinfo.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_manager'] + "heck") or user_msg.startswith("$sudo_heck")):
                        await heck.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_manager'] + "backup")):
                        await backup.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "loadbackup")):
                        await loadbackup.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "add_bot")):
                        await add_bot.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "eco")):
                        await economy.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_manager'] + "settings")):
                        #if(utils.is_owner_of_bot(message.author.id)):
                            await settings.Cmd(message, client)
                    #if(user_msg.startswith(config[f'prefix_manager'] + "serialkey")):
                    #    await serialkey.Cmd(message)
                    #if(user_msg.startswith(config[f'prefix_manager'] + "o1k")):
                    #    await o1k_msg.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "activity")):
                        await activity.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_manager'] + "msgcnt")):
                        await msgcnt.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "to_fix")):
                        await to_fix.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "legend")):
                        await legend.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_manager'] + "eval")):
                        await eval.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_manager'] + "terminal")):
                        await terminal.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "say")):
                        await say.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "support_server")):
                        await support_server.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "c4k")):
                        await c4k.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + 'vent ')):
                        await vent.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_manager'] + 'micup')):
                        await micup.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_manager'] + "ask8ball")):
                        await ask8ball.Cmd(message)
                        '''

                #if(user_msg.startswith(config[f'prefix_manager'])):
                #    await message.delete()

@client.event
async def on_select_option(interaction : discord_components.Interaction):
    rickroll = [
        "Never gonna give you up",
        "Never gonna let you down",
        "Never gonna run around and desert you",
        "Never gonna make you cry",
        "Never gonna say goodbye",
        "Never gonna tell a lie and hurt you"
    ]

    for rr in rickroll:
        if(interaction.values[0] == rr):
            await interaction.respond(content="It isn't supposed to work, don't click it again ok?")
    global maintence
    if(maintence):
        await interaction.respond(content="Maintence mode.")
        return
    for folder in glob.glob("cmds/*/"):
        if (interaction.values[0].startswith(folder.replace("cmds", "").replace("\\", ""))):
            if ("part" in interaction.values[0]):
                folder = folder + f"/{str(interaction.values[0].split(' part ')[1])}"
            if(len(glob.glob(f"{folder}/*/")) > 2):
                ar = []
                backslash = "\\"
                for x in range(1, len(glob.glob(f"{folder}/*/"))):
                    ar.append(SelectOption(
                        label=f"{folder.replace('cmds', '').replace(backslash, '')} part {str(x)}", value=f"{folder.replace('cmds', '').replace(backslash, '')} part {str(x)}"))
                await interaction.respond(content="This command is multi-parted, select part.", components=[Select(placeholder='Select part.', options=ar), ])
            else:
                backslash = "\\"
                count = 0
                embedVar = discord.Embed(title=f'Help {folder.replace("cmds", "").replace(backslash, "")}', description="for Pan-Project Bot.", color=0x00ff00)
                for file in glob.glob(f"{folder}/*.py"):
                    with open(file, "r", encoding="utf8") as f:
                        try:
                            #if not("{H}" in f.readline()):
                                prefix = {}
                                with open("prefix.json", "r") as welcom:
                                    prefix = json.loads(welcom.read())
                                try:
                                    useprefix = prefix[str(interaction.guild.id)]
                                except KeyError:
                                    useprefix = "?"
                                t = f.readline().replace("#", "")
                                t = t.replace("{}", useprefix)
                                t = t.replace("{HASH}", "#")
                                if ("||" in t):
                                    for c in t.split("||"):
                                        embedVar.add_field(name=c.split("-")[0], value=c.split("-")[1], inline=True)
                                        count = count + 1
                                else:
                                    embedVar.add_field(name=t.split("-")[0], value=t.split("-")[1], inline=True)
                                    count = count + 1
                        except:
                            pass
                await interaction.respond(content=language[serverlang[str(interaction.guild.id)]]["global"]["interaction_embed"], embed=embedVar)

@client.event
async def on_button_click(interaction):
    #try:
        user = interaction.author
        guild = interaction.guild
        #for x in range(1, 5):
            #if(str(x) in interaction.component.custom_id):
                #after_invoke_cmd.Count_Votes(interaction, x)
                #await interaction.respond(content="Counted your vote (If you already counted, we won't count it)")
        if ("Error Check" in interaction.component.label):
            await interaction.respond(content=language[serverlang[str(guild.id)]]["global"]["interaction_embed"],
                            embed=await errorcheck.ReturnCmd(user.id),
                            components=[Button(style=ButtonStyle.blue, label="Clear errors", custom_id="CE"), ])
        if ("Clear errors" in interaction.component.label):
            errors_structure = """{"errors": []}"""
            loc = os.environ['PYTHONPATH'].replace(__file__, "")
            with open(f"{loc}/cmds/error.json", "w", encoding='utf8') as f:
                f.write(errors_structure)
            await interaction.respond(content="Cleared!")
        if("Stats" in interaction.component.label):
            await interaction.respond(content=language[serverlang[str(guild.id)]]["global"]["interaction_embed"], embed=await stats.ReturnCmd(user.id))
        if("Reimport commands" in interaction.component.label):
            await interaction.respond(content=reimportcmds())
        if("Maintence Mode" in interaction.component.label):
            if(not(utils.is_owner_of_bot(user.id))):
                await interaction.respond(content=language[serverlang[str(guild.id)]]["kernel"]['maintencemodeonbydefault'])
            else:
                global maintence
                if(maintence == True):
                    maintence = False
                    await client.get_channel(927982475379097620).send(language[serverlang[str(guild.id)]]["kernel"]['maintencemodeonoff'])
                elif(maintence == False):
                    maintence = True
                    await client.get_channel(927982475379097620).send(language[serverlang[str(guild.id)]]["kernel"]['maintencemodeoffon'])
                await interaction.respond(content=language[serverlang[str(guild.id)]]["kernel"]['maintencemodeturningon'])

        if("CLAIM 🍟" in interaction.component.label):
            if (BadgesManager.Have_Badge(5, user.id) == False):# or utils.is_owner_of_bot(user.id)):
                try:
                    for filefetch in glob.glob("ecojson/*.json"):
                        await eco.Give_Not_Add_Money(str(filefetch).replace("ecojson\\", "").replace(".json", ""),
                                                         user.id, 1000)
                    chanid = client.get_channel(927859819665297439)
                    await chanid.send(f"{user.name} claimed his 1,000 :fries: (and got exclusive badge)")
                    await BadgesManager.Add_Badge(5, user.id, client)
                    await interaction.respond(content="Got it! You should see yourself claiming on logs.")
                    # with open("who_got_1k.txt", "a") as gnd:
                    #    gnd.write(str(user.id) + "\n")
                except:
                    await interaction.respond(content="Sorry, try again, use won't be took")
            else:
                await interaction.respond(content="Bruh, you already claimed it!")
            '''
            with open("who_got_1k.txt", "r") as wgk:
                array = []
                array = wgk.readlines()
                if(not(str(interaction.author.id) + "\n" in array)):
                    try:
                        for filefetch in glob.glob("ecojson/*.json"):
                            await economy.Give_Not_Add_Money(str(filefetch).replace("ecojson\\", "").replace(".json", ""), user.id, 1000)
                        chanid = client.get_channel(927859819665297439)
                        await chanid.send(language[serverlang[str(guild.id)]]["kernel"]['claim_1k'].replace("{user.name}", user.name))
                        BadgesManager.Add_Badge(5, user.id)
                        await interaction.respond(content=language[serverlang[str(guild.id)]]["kernel"]['reply_respond'])
                        with open("who_got_1k.txt", "a") as gnd:
                            gnd.write(str(user.id) + "\n")
                    except:
                        await interaction.respond(content=language[serverlang[str(guild.id)]]["kernel"]['reply_respond'])
                else:
                    await interaction.respond(content=language[serverlang[str(guild.id)]]["kernel"]['error_claim'])

'''
        #lele = interaction.component.label.replace("🔑", "")
        #if(lele in serialkey.SysKeys):
        #    embedVar = discord.Embed(title=f"Keys for {lele}", description="for Pansage Bot.", color=0x00ffff)
        #    for e in keys["Win"]:
        #        if(e["System"].startswith(lele)):
        #            embedVar.add_field(name=e["System"], value=e["SysKey"], inline=False)
        #    await interaction.respond(content=language[serverlang[str(guild.id)]]["global"]["interaction_embed"], embed=embedVar)
    #except Exception as exc:
    #    await utils.save_error(f"Btn Selection / Kernel ({client.user})", os.path.basename(__file__), exc)
    #    await interaction.respond(content="Error. I saved error in my error database, my creator will check out.")

#async def Kill_Kernel(tok):
#    try:
#        if(toktocheck == tok):
#            await client.logout()
#    except Exception as exc:
#        await utils.save_error(f"Kill / Kernel ({client.user})", os.path.basename(__file__), exc)
#        await message.channel.send("Error. I saved error in my error database, my creator will check out.")

async def Open_Bot_Kernel(token):
    try:
        global toktocheck
        print("Logging bot")
        toktocheck = token
        #client = discord.AutoShardedClient(shard_count=5)
        await client.start(token)
        inter_client = InteractionClient(client)
    except Exception as exc:
        await utils.save_error(f"Running / Kernel ({client.user})", os.path.basename(__file__), exc)
        #await message.channel.send("Error. I saved error in my error database, my creator will check out.")

async def handle(inter : dislash.Interaction, exec="help"):
    await inter.reply(embed=f"Executing {exec}")
    await handler(inter.send(exec))

#asyncio.run(Open_Bot_Kernel(config['token_manager']))