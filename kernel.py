import threading
import glob

import discord
import json
import os
from discord_components import DiscordComponents

import BadgesManager

import utils, pmc
import o1k_msg

from cmds import help, devtoolkit, backup, generate, ping, serialkey, loadbackup, economy, msgcnt, heck, guildinfo, activity, legend, eval, memberinfo

from manager import help as helpman
from manager import activity as actiman
from manager import devtoolkit as dtkman
from manager import gban, gunban

from dev import nuke, errorcheck, stats

panproj = ["normal", "manager"]

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

keys = {}
with open(f"serialkey.json", encoding='utf8') as data:
    keys = json.load(data)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    global whichone
    DiscordComponents(client)
    await client.change_presence(activity=discord.Game(name=f"ur mom"))
    print("Successfully logged in.")

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
        if(f"backup/{guildid}.json"):
            with open(f"msgcount/{guildid}.json", "w") as yee:
                yee.write(json.dumps(temp))
    except:
        pass
    chanid = client.get_channel(927848602821349386)
    await chanid.send(f"I got added to server {guildname} ({guildid})")

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
    try:
        if(f"backup/{guildid}.json"):
            os.remove(f"backup/{guildid}.json")
    except:
        pass
    chanid = client.get_channel(927848602821349386)
    await chanid.send(f"I got kicked from server {guildname} ({guildid})")

@client.event
async def on_message(message):
    try:
        #print(message)
        #if(isinstance(message.channel, discord.channel.DMChannel) and not(message.author == client.user)):
        #    return message.channel.send("Bro. Don't DM me ok?")
        #try:
        username = str(message.author).split('#')[0]
        usertag = str(message.author).split('#')[1]
        userid = str(message.author.id)
        user_msg = str(message.content)
        channel = str(message.channel.name)
        #except:
        #    pass

        # TODO: FIX "ECO-GIANT" BADGE
        BadgesManager.Clear_Badges(7)
        ggd = await economy.Get_Global_Data(client)
        ggd.sort(key=economy.sort_func, reverse=True)
        if (ggd[0]["name"] == message.guild.name):
            members = await message.guild.fetch_members(limit=None).flatten()
            for x in members:
                BadgesManager.Add_Badge(7, x.id)

        if("69" in message.content):
            await message.reply("nice.")

        if message.author == client.user:
            pass
        elif message.author.bot:
            pass

        #with open("message_log.txt", "a") as log:
        #    log.write(f"({client.user}): " + username + "#" + usertag + " (" + userid + "): " + user_msg + " / " + message.guild.name + " -> #" + channel + "\n")

        whichone = ""
        for panp in panproj:
            if (config[f'token_{panp}'] == toktocheck):
                whichone = panp
        #print(whichone)
        if(whichone == "normal"):
            await pmc.CheckMsg(message)

            if (message.author.id in config["gbans"]):
                return await message.channel.send("You got gbanned - sorry!")
            else:
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "generate") or user_msg.startswith(config[f'prefix_{whichone}'] + "gen")):
                    await generate.Cmd(message, user_msg)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "help")):
                    await help.Cmd(message, whichone)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "devtoolkit")):
                    await devtoolkit.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "ping")):
                    await ping.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "guildinfo")):
                    await guildinfo.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "memberinfo")):
                    await memberinfo.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "heck") or user_msg.startswith("$sudo_heck")):
                    await heck.Cmd(message, client)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "backup")):
                    await backup.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "loadbackup")):
                    await loadbackup.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco earn")):
                    await economy.Cmd_Earn(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco bal")):
                    await economy.Cmd_Bal(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco ccd")):
                    await economy.Cmd_ClearCD(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco clear")):
                    if(utils.is_owner_of_bot(userid)):
                        return await message.channel.send("Only for owner.")
                    try:
                        await economy.Set_Money(message.guild.id, user_msg.split(" ")[2], 0)
                        await message.channel.send("Cleared his :fries:")
                    except:
                        await message.channel.send("Invalid args")
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco set")):
                    await economy.Cmd_Set_Eco(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco send")):
                    await economy.Cmd_Send_Money(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco leaderboard")):
                    await economy.Cmd_Leaderboard(message, client)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "serialkey")):
                    await serialkey.Cmd(message)
                #if(user_msg.startswith(config[f'prefix_{whichone}'] + "o1k")):
                #    await o1k_msg.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "activity")):
                    await activity.Cmd(message, client)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "msgcnt")):
                    await msgcnt.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "legend")):
                    await legend.Cmd(message, client)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "eval")):
                    await eval.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "say")):
                    await message.channel.send(user_msg.replace("?say ", ""))
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "support_server")):
                    await message.channel.send("Join and you can get free 1,000 :fries: **on every server** and exclusive badge (:man_gesturing_ok:) on memberinfo\n-> https://discord.gg/4dRPUTsPza <-")
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "c4k")):
                    await message.channel.send("Gotcha his ass")
                    await message.channel.send("https://c.tenor.com/QA6mPKs100UAAAAC/caught-in.gif")

            #if(user_msg.startswith(config[f'prefix_{whichone}'])):
            #    await message.delete()
        elif(whichone == "manager"):
            if(message.author.id in config["gbans"]):
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "help")):
                    await helpman.Cmd(message, whichone)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "activity")):
                    await actiman.Cmd(message, client)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "gban")):
                    await gban.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "gunban")):
                    await gunban.Cmd(message)
                if(user_msg.startswith(config[f'prefix_{whichone}'] + "devtoolkit")):
                    await dtkman.Cmd(message)
            #print(f"bot is {whichone}")
    except Exception as ex:
        await message.channel.send(":warning: KERNEL ERROR! :warning:\nLogging off & saving to database...")
        await utils.save_error(f"Kernel ({client.user})", os.path.basename(__file__), ex)
        exit(ex)

@client.event
async def on_button_click(interaction):
    #try:
        user = interaction.author
        guild = interaction.guild
        if("Error Check" in interaction.component.label):
            await interaction.respond(content="Here you go!", embed=await errorcheck.ReturnCmd(user.id))
        if("Nuke" in interaction.component.label):
            await nuke.Cmd(user.id, guild)
        if("Stats" in interaction.component.label):
            await interaction.respond(content="Here you go!", embed=await stats.ReturnCmd(user.id))

        if("CLAIM 🍟" in interaction.component.label):
            with open("who_got_1k.txt", "r") as wgk:
                array = []
                array = wgk.readlines()
                if(not(str(interaction.author.id) + "\n" in array)):
                    try:
                        for filefetch in glob.glob("ecojson/*.json"):
                            await economy.Give_Not_Add_Money(str(filefetch).replace("ecojson\\", "").replace(".json", ""), user.id, 1000)
                        chanid = client.get_channel(927859819665297439)
                        await chanid.send(f"{user.name} claimed his 1,000 :fries: (and got exclusive badge)")
                        BadgesManager.Add_Badge(5, user.id)
                        await interaction.respond(content="Got it! You should see yourself claiming on logs.")
                        with open("who_got_1k.txt", "a") as gnd:
                            gnd.write(str(user.id) + "\n")
                    except:
                        await interaction.respond(content="Sorry, try again, use won't be took")
                else:
                    await interaction.respond(content="Bruh, you already claimed it!")

        lele = interaction.component.label.replace("🔑", "")
        if(lele in serialkey.SysKeys):
            embedVar = discord.Embed(title=f"Keys for {lele}", description="for Pansage Bot.", color=0x00ffff)
            for e in keys["Win"]:
                if(e["System"].startswith(lele)):
                    embedVar.add_field(name=e["System"], value=e["SysKey"], inline=False)
            await interaction.respond(content="Here you go!", embed=embedVar)
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
        await client.start(token)
    except Exception as exc:
        await utils.save_error(f"Running / Kernel ({client.user})", os.path.basename(__file__), exc)
        #await message.channel.send("Error. I saved error in my error database, my creator will check out.")
