import asyncio
import random
import threading
import glob
import time

import discord_components
import psutil
import importlib

import discord
import json
import os
from discord_components import DiscordComponents

import BadgesManager
import after_invoke_cmd

import utils, pmc
import o1k_msg

print("Starting import")
print(f'-----------------------------')
for foldersa in glob.glob(f"cmds/*/"):
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
        print(f'-----------------------------')
print(f'-----------------------------')
print(f'Ending import')

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

prefix = {}
with open("prefix.json", "r") as welcom:
    prefix = json.loads(welcom.read())

keys = {}
with open(f"serialkey.json", encoding='utf8') as data:
    keys = json.load(data)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
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
    print("0/2")
    DiscordComponents(client)
    print("1/2")
    await client.change_presence(activity=discord.Game(name=f"Beta test!"))
    print("2/2 - Successfully logged in.")
    #await after_invoke_cmd.Daily_Poll(client)

@client.event
async def on_guild_join(guild):
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

    await chanid.send(english['eng']["kernel"]['added_server'].replace("{guildname}", guildname).replace("{guildid}", guildid))#\nHere's link to join {link}\n")

@client.event
async def on_guild_remove(guild):
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
    await chanid.send(english['eng']["kernel"]['kicked_server'].replace("{guildname}", guildname).replace("{guildid}", guildid))

@client.event
async def on_message(message):
    prefix = {}
    with open("prefix.json", "r") as welcom:
        prefix = json.loads(welcom.read())

    if message.author == client.user:
        return
    if (message.channel.type == discord.ChannelType.private):
        return
    if message.author.bot:
        return
    try:
        if(language[serverlang[str(message.guild.id)]]["kernel"]["kernel_error"]):
            pass
    except KeyError:
        await select_language(message)

    useprefix = ""
    try:
        useprefix = prefix[str(message.guild.id)]
    except KeyError:
        useprefix = "?"
    #print(str(message.content).startswith(prefix[str(message.guild.id)]))
    try:
        if (str(message.content).startswith(prefix[str(message.guild.id)])):
            if (not (maintence)):
                await handler(message)
            else:
                await message.channel.send(english['eng']["kernel"]['maintencemode'])
    except Exception as ex:
        await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["kernel_error"])
        await utils.save_error(
            f"Kernel ({client.user}) / Crashed by {message.author.name} ({message.author.id})",
            os.path.basename(__file__), ex)
        exit(ex)

    await pmc.CheckMsg(message)
    await Reload_Badges_Roles(client)

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
                    role = await message.guild.create_role(name=x["name"] + " badge owners")
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
            username = str(message.author).split('#')[0]
            usertag = str(message.author).split('#')[1]
            userid = str(message.author.id)
            user_msg = str(message.content)
            channel = str(message.channel.name)

            if(message.channel.id == 929668126654750741 and message.content == "!d bump"):
                if(not(BadgesManager.Have_Badge(12, message.author.id))):
                    await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["dbump_first"].replace("{message.author.id}", message.author.id))
                    await economy.Give_Money(message.guild.id, message.author.id, 1000)
                    BadgesManager.Add_Badge(12, message.author.id)
                else:
                    await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["dbump"].replace("{message.author.id}", message.author.id))
                    await economy.Give_Money(message.guild.id, message.author.id, 500)
            #with open("message_log.txt", "a") as log:
            #    log.write(f"({client.user}): " + username + "#" + usertag + " (" + userid + "): " + user_msg + " / " + message.guild.name + " -> #" + channel + "\n")

            global whichone
            whichone = ""
            for panp in panproj:
                if (config[f'token_{panp}'] == toktocheck):
                    whichone = panp
            #print(whichone)
            if (f"<@!{config[f'id_manager']}>" in message.content):
                useprefix = ""
                try:
                    useprefix = prefix[str(message.guild.id)]
                except KeyError:
                    useprefix = "?"
                await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["on_ping_wakeup"].replace("{config[f'prefix_{whichone}']}", useprefix))

            if(True):#whichone == "normal"):
                #print(message.content)
                #print(user_msg.startswith(config[f'prefix_manager']))
                if (not message.author.id in config["owners"]):
                    return await message.channel.send("Only my dev can use me - I'm only testing, to deliver bot without bugs!")
                else:
                    #if(user_msg.startswith(config[f'prefix_manager'] + "generate") or user_msg.startswith(config[f'prefix_manager'] + "gen")):
                    #    await generate.Cmd(message, user_msg)
                    for folder in glob.glob(f"cmds/*/"):
                        for cmdsname in glob.glob(f"{folder}/*.py"):
                            package = cmdsname.replace(f"{folder}", "").replace("\\", "").replace(".py", "")
                            #print(package)
                            useprefix = ""
                            try:
                                useprefix = prefix[str(message.guild.id)]
                            except KeyError:
                                useprefix = "?"
                            if (user_msg.startswith(useprefix + package)):
                                #print(" F O U N D I T")
                                #yes = await eval(f"{package}.Cmd(message='{message}', client='{client}', whichone='{whichone}')")
                                await getattr(lookup(package), "Cmd")(language, serverlang, message, client)

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
    for folder in glob.glob("cmds/*/"):
        if (interaction.values[0] == folder.replace("cmds", "").replace("\\", "")):
            backslash = "\\"
            embedVar = discord.Embed(title=f'Help {folder.replace("cmds", "").replace(backslash, "")}', description="for Pan-Project Bot.", color=0x00ff00)
            for file in glob.glob(f"{folder}/*.py"):
                with open(file, "r", encoding="utf8") as f:
                    t = f.readline().replace("#", "")
                    t = t.replace("{}", useprefix)
                    t = t.replace("{HASH}", "#")
                    if ("||" in t):
                        for c in t.split("||"):
                            embedVar.add_field(name=c.split("-")[0], value=c.split("-")[1], inline=True)
                    else:
                        embedVar.add_field(name=t.split("-")[0], value=t.split("-")[1], inline=True)
            await interaction.respond(content=language[serverlang[str(interaction.guild.id)]]["global"]["interaction_embed"], embed=embedVar)

@client.event
async def on_button_click(interaction):
    #try:
        user = interaction.author
        guild = interaction.guild
        for x in range(1, 5):
            if(str(x) in interaction.component.custom_id):
                after_invoke_cmd.Count_Votes(interaction, x)
                await interaction.respond(content="Counted your vote (If you already counted, we won't count it)")

        if("Error Check" in interaction.component.label):
            await interaction.respond(content=language[serverlang[str(guild.id)]]["global"]["interaction_embed"], embed=await errorcheck.ReturnCmd(user.id))
        if("Nuke" in interaction.component.label):
            await nuke.Cmd(user.id, guild)
        if("Stats" in interaction.component.label):
            await interaction.respond(content=language[serverlang[str(guild.id)]]["global"]["interaction_embed"], embed=await stats.ReturnCmd(user.id))
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
            if (BadgesManager.Have_Badge(5, user.id) == False):
                try:
                    for filefetch in glob.glob("ecojson/*.json"):
                        await economy.Give_Not_Add_Money(str(filefetch).replace("ecojson\\", "").replace(".json", ""),
                                                         user.id, 1000)
                    chanid = client.get_channel(927859819665297439)
                    await chanid.send(f"{user.name} claimed his 1,000 :fries: (and got exclusive badge)")
                    BadgesManager.Add_Badge(5, user.id)
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
        print("-1/2")
        await client.start(token)
    except Exception as exc:
        await utils.save_error(f"Running / Kernel ({client.user})", os.path.basename(__file__), exc)
        #await message.channel.send("Error. I saved error in my error database, my creator will check out.")

#asyncio.run(Open_Bot_Kernel(config['token_manager']))