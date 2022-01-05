import threading

import discord
import json
import os
from discord_components import DiscordComponents

import utils, pmc

from cmds import help, devtoolkit, backup, generate, ping, serialkey, loadbackup, economy, msgcnt

from dev import nuke, errorcheck, stats

panproj = ["normal", "premium", "manager"]

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

keys = {}
with open(f"serialkey.json", encoding='utf8') as data:
    keys = json.load(data)

client = discord.Client()

@client.event
async def on_ready():
    global whichone
    DiscordComponents(client)
    await client.change_presence(activity=discord.Game(name=f"ur mom"))
    print("Successfully logged in.")

@client.event
async def on_message(message):
    try:
        #print(message)
        if(message.channel == "DMchannel"):
            return message.channel.send("Bro. Don't DM me ok?")
        username = str(message.author).split('#')[0]
        usertag = str(message.author).split('#')[1]
        userid = str(message.author.id)
        user_msg = str(message.content)
        channel = str(message.channel.name)

        if message.author == client.user:
            return
        #with open("message_log.txt", "a") as log:
        #    log.write(f"({client.user}): " + username + "#" + usertag + " (" + userid + "): " + user_msg + " / " + message.guild.name + " -> #" + channel + "\n")

        whichone = ""
        for panp in panproj:
            if (config[f'token_{panp}'] == toktocheck):
                whichone = panp
        #print(whichone)
        if(whichone == "normal" or whichone == "premium"):
            if(user_msg.startswith(config[f'prefix_{whichone}'] + "generate") or user_msg.startswith(config[f'prefix_{whichone}'] + "gen")):
                await generate.Cmd(message, user_msg)
            if(user_msg.startswith(config[f'prefix_{whichone}'] + "help")):
                await help.Cmd(message, whichone)
            if(user_msg.startswith(config[f'prefix_{whichone}'] + "devtoolkit")):
                await devtoolkit.Cmd(message)
            if(user_msg.startswith(config[f'prefix_{whichone}'] + "ping")):
                await ping.Cmd(message)
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
                await economy.Cmd_Clear_Eco(message)
            if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco set")):
                await economy.Cmd_Set_Eco(message)
            if(user_msg.startswith(config[f'prefix_{whichone}'] + "serialkey")):
                await serialkey.Cmd(message)
            if(user_msg.startswith(config[f'prefix_{whichone}'] + "msgcnt")):
                await msgcnt.Cmd(message)
            if(user_msg.startswith(config[f'prefix_{whichone}'] + "say")):
                await message.channel.send(user_msg.replace("?say ", ""))

            await pmc.CheckMsg(message)
            #if(user_msg.startswith(config[f'prefix_{whichone}'])):
            #    await message.delete()
        #else:
            #print(f"bot is {whichone}")
    except Exception as ex:
        await message.channel.send(":warning: KERNEL ERROR! :warning:\nLogging off & saving to database...")
        await utils.save_error(f"Kernel ({client.user})", os.path.basename(__file__), ex)
        exit(ex)

@client.event
async def on_button_click(interaction):
    try:
        user = interaction.author
        guild = interaction.guild
        if("Error Check" in interaction.component.label):
            await interaction.respond(content="Here you go!", embed=await errorcheck.ReturnCmd(user.id))
        if("Nuke" in interaction.component.label):
            await nuke.Cmd(user.id, guild)
        if("Stats" in interaction.component.label):
            await interaction.respond(content="Here you go!", embed=await stats.ReturnCmd(user.id))
        lele = interaction.component.label.replace("🔑", "")
        if(lele in serialkey.SysKeys):
            embedVar = discord.Embed(title=f"Keys for {lele}", description="for Pansage Bot.", color=0x00ffff)
            for e in keys["Win"]:
                if(e["System"].startswith(lele)):
                    embedVar.add_field(name=e["System"], value=e["SysKey"], inline=False)
            await interaction.respond(content="Here you go!", embed=embedVar)
    except Exception as exc:
        await utils.save_error(f"Btn Selection / Kernel ({client.user})", os.path.basename(__file__), exc)
        await interaction.respond(content="Error. I saved error in my error database, my creator will check out.")

async def Kill_Kernel(tok):
    try:
        if(toktocheck == tok):
            await client.logout()
    except Exception as exc:
        await utils.save_error(f"Kill / Kernel ({client.user})", os.path.basename(__file__), exc)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")

async def Open_Bot_Kernel(token):
    try:
        global toktocheck
        print("Logging bot")
        toktocheck = token
        await client.start(token)
    except Exception as exc:
        await utils.save_error(f"Running / Kernel ({client.user})", os.path.basename(__file__), exc)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")
