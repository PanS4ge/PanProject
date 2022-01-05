import kernel

import utils

import threading
import discord

import asyncio

from discord_components import DiscordComponents, Button, ButtonStyle

from cmds import devtoolkit

from dev import nuke, errorcheck, stats

import os
import json

client = discord.Client()

botseys = [0, 0]

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

@client.event
async def on_ready():
    DiscordComponents(client)
    await client.change_presence(activity=discord.Game(name=f"with bots"))
    print("Successfully logged in.")
    if(config["autorun"] == "True"):
        await kernel.Open_Bot_Kernel(config['token_normal'])
        botseys[0] = 1
        #await kernel.Open_Bot_Kernel(config['token_premium'])
        #botseys[1] = 1
        #kernel.Open_Bot_Kernel(config['token_manager'])
        #botseys[2] = 1

@client.event
async def on_message(message):
    try:
        if(message.channel == "DMchannel"):
            return message.channel.send("Bro. Don't DM me ok?")
        username = str(message.author).split('#')[0]
        usertag = str(message.author).split('#')[1]
        userid = str(message.author.id)
        user_msg = str(message.content)
        channel = str(message.channel.name)

        if message.author == client.user:
            return

        if not utils.is_owner_of_bot(message.author.id):
            return

        if(user_msg.startswith(config['prefix_runner'] + "run")):
            embedVar = discord.Embed(title="Runner", description="for Pansage Bot.", color=0xff0000)
            embedVar.add_field(name="Select bot to open", value="With buttons below, remember only owner can.", inline=False)
            ar = [[]]
            if(botseys[0] == 0):
                ar[0].append(Button(style=ButtonStyle.green, label=config['name_normal'], custom_id="zeroon"))
            else:
                ar[0].append(Button(style=ButtonStyle.red, label=config['name_normal'], custom_id="zerooff"))
            #if(botseys[1] == 0):
            #    ar[0].append(Button(style=ButtonStyle.green, label=config['name_premium'], custom_id="oneon"))
            #else:
            #    ar[0].append(Button(style=ButtonStyle.red, label=config['name_premium'], custom_id="oneoff"))
            if(botseys[1] == 0):
                ar[0].append(Button(style=ButtonStyle.green, label=config['name_manager'], custom_id="twoon"))
            else:
                ar[0].append(Button(style=ButtonStyle.red, label=config['name_manager'], custom_id="twooff"))
            mess = await message.channel.send(embed=embedVar, components=ar)

        if (user_msg.startswith(config['prefix_runner'] + "devtoolkit")):
            await devtoolkit.Cmd(message)

        if(user_msg.startswith(config['prefix_runner'] + "allrun")):
            await kernel.Open_Bot_Kernel(config['token_normal'])
            botseys[0] = 1
            #await kernel.Open_Bot_Kernel(config['token_premium'])
            await kernel.Open_Bot_Kernel(config['token_manager'])
            botseys[1] = 1
            #await kernel.Open_Bot_Kernel(config['token_manager'])
            #botseys[2] = 1

        if(user_msg.startswith(config['prefix_runner'])):
            await message.delete()

    except Exception as ex:
        #await message.channel.send(":warning: RUNNER KERNEL ERROR! :warning:\nLogging off & saving to database...")
        utils.noas_save_error("Runner Kernel", os.path.basename(__file__), ex)

@client.event
async def on_button_click(interaction):
    try:
        user = interaction.author
        guild = interaction.guild
        if ("zeroon" in interaction.component.custom_id):
            if (user.id in config['owners']):
                await interaction.respond(content="Powering on..., please wait while it's running")
                await kernel.Open_Bot_Kernel(config['token_normal'])
                botseys[0] = 1
                ar = [[]]
                if (botseys[0] == 0):
                    ar[0].append(Button(style=ButtonStyle.green, label=config['name_normal'], custom_id="zeroon"))
                else:
                    ar[0].append(Button(style=ButtonStyle.red, label=config['name_normal'], custom_id="zerooff"))
                #if (botseys[1] == 0):
                #    ar[0].append(Button(style=ButtonStyle.green, label=config['name_premium'], custom_id="oneon"))
                #else:
                #    ar[0].append(Button(style=ButtonStyle.red, label=config['name_premium'], custom_id="oneoff"))
                if (botseys[1] == 0):
                    ar[0].append(Button(style=ButtonStyle.green, label=config['name_manager'], custom_id="twoon"))
                else:
                    ar[0].append(Button(style=ButtonStyle.red, label=config['name_manager'], custom_id="twooff"))
                await mess.edit(content=f"{mess.content}", components=ar)
            await interaction.respond(content="Duck off.")
        #if ("oneon" in interaction.component.custom_id):
        #    if (user.id in config['owners']):
        #        await interaction.respond(content="Powering on..., please wait while it's running")
        #        await kernel.Open_Bot_Kernel(config['token_premium'])
        #        botseys[1] = 1
        #        if (botseys[0] == 0):
        #            ar[0].append(Button(style=ButtonStyle.green, label=config['name_normal'], custom_id="zeroon"))
        #        else:
        #            ar[0].append(Button(style=ButtonStyle.red, label=config['name_normal'], custom_id="zerooff"))
        #        if (botseys[1] == 0):
        #            ar[0].append(Button(style=ButtonStyle.green, label=config['name_premium'], custom_id="oneon"))
        #        else:
        #            ar[0].append(Button(style=ButtonStyle.red, label=config['name_premium'], custom_id="oneoff"))
        #        if (botseys[2] == 0):
        #            ar[0].append(Button(style=ButtonStyle.green, label=config['name_manager'], custom_id="twoon"))
        #        else:
        #            ar[0].append(Button(style=ButtonStyle.red, label=config['name_manager'], custom_id="twooff"))
        #        await mess.edit(content=f"{mess.content}", components=ar)
        #    await interaction.respond(content="Duck off.")
        if ("twoon" in interaction.component.custom_id):
            if (user.id in config['owners']):
                await interaction.respond(content="Powering on..., please wait while it's running")
                await kernel.Open_Bot_Kernel(config['token_manager'])
                botseys[2] = 1
                if (botseys[0] == 0):
                    ar[0].append(Button(style=ButtonStyle.green, label=config['name_normal'], custom_id="zeroon"))
                else:
                    ar[0].append(Button(style=ButtonStyle.red, label=config['name_normal'], custom_id="zerooff"))
                # if (botseys[1] == 0):
                #    ar[0].append(Button(style=ButtonStyle.green, label=config['name_premium'], custom_id="oneon"))
                # else:
                #    ar[0].append(Button(style=ButtonStyle.red, label=config['name_premium'], custom_id="oneoff"))
                if (botseys[1] == 0):
                    ar[0].append(Button(style=ButtonStyle.green, label=config['name_manager'], custom_id="twoon"))
                else:
                    ar[0].append(Button(style=ButtonStyle.red, label=config['name_manager'], custom_id="twooff"))
                await mess.edit(content=f"{mess.content}", components=ar)
            await interaction.respond(content="Duck off.")
        if ("zerooff" in interaction.component.custom_id):
            if (user.id in config['owners']):
                await interaction.respond(content="Powering off...,")
                #await kernel.Kill_Kernel(config['token_normal'])
                botseys[0] = 0
                if (botseys[0] == 0):
                    ar[0].append(Button(style=ButtonStyle.green, label=config['name_normal'], custom_id="zeroon"))
                else:
                    ar[0].append(Button(style=ButtonStyle.red, label=config['name_normal'], custom_id="zerooff"))
                # if (botseys[1] == 0):
                #    ar[0].append(Button(style=ButtonStyle.green, label=config['name_premium'], custom_id="oneon"))
                # else:
                #    ar[0].append(Button(style=ButtonStyle.red, label=config['name_premium'], custom_id="oneoff"))
                if (botseys[1] == 0):
                    ar[0].append(Button(style=ButtonStyle.green, label=config['name_manager'], custom_id="twoon"))
                else:
                    ar[0].append(Button(style=ButtonStyle.red, label=config['name_manager'], custom_id="twooff"))
                await mess.edit(content=f"{mess.content}", components=ar)
            await interaction.respond(content="Duck off.")
        #if ("oneoff" in interaction.component.custom_id):
            #if (user.id in config['owners']):
            #    await interaction.respond(content="Powering off...,")
            #    await kernel.Kill_Kernel(config['token_premium'])
            #    botseys[1] = 0
            #    if (botseys[0] == 0):
            #        ar[0].append(Button(style=ButtonStyle.green, label=config['name_normal'], custom_id="zeroon"))
            #    else:
            #        ar[0].append(Button(style=ButtonStyle.red, label=config['name_normal'], custom_id="zerooff"))
                # if (botseys[1] == 0):
                #    ar[0].append(Button(style=ButtonStyle.green, label=config['name_premium'], custom_id="oneon"))
                # else:
                #    ar[0].append(Button(style=ButtonStyle.red, label=config['name_premium'], custom_id="oneoff"))
            #    if (botseys[1] == 0):
            #        ar[0].append(Button(style=ButtonStyle.green, label=config['name_manager'], custom_id="twoon"))
            #    else:
            #        ar[0].append(Button(style=ButtonStyle.red, label=config['name_manager'], custom_id="twooff"))
            #    await mess.edit(content=f"{mess.content}", components=ar)
            #await interaction.respond(content="Duck off.")
        if ("twooff" in interaction.component.custom_id):
            if (user.id in config['owners']):
                await interaction.respond(content="Powering off...,")
                #await kernel.Kill_Kernel(config['token_manager'])
                botseys[2] = 0
                if (botseys[0] == 0):
                    ar[0].append(Button(style=ButtonStyle.green, label=config['name_normal'], custom_id="zeroon"))
                else:
                    ar[0].append(Button(style=ButtonStyle.red, label=config['name_normal'], custom_id="zerooff"))
                # if (botseys[1] == 0):
                #    ar[0].append(Button(style=ButtonStyle.green, label=config['name_premium'], custom_id="oneon"))
                # else:
                #    ar[0].append(Button(style=ButtonStyle.red, label=config['name_premium'], custom_id="oneoff"))
                if (botseys[1] == 0):
                    ar[0].append(Button(style=ButtonStyle.green, label=config['name_manager'], custom_id="twoon"))
                else:
                    ar[0].append(Button(style=ButtonStyle.red, label=config['name_manager'], custom_id="twooff"))
                await mess.edit(content=f"{mess.content}", components=ar)
            await interaction.respond(content="Duck off.")
        if ("Error Check" in interaction.component.label):
            await interaction.respond(content="Here you go!", embed=await errorcheck.ReturnCmd(user.id))
        if ("Nuke" in interaction.component.label):
            await nuke.Cmd(user.id, guild)
        if ("Stats" in interaction.component.label):
            await interaction.respond(content="Here you go!", embed=await stats.ReturnCmd(user.id))
    except Exception as exc:
        await utils.save_error("Btn Selection / Runner Kernel", os.path.basename(__file__), exc)
        await interaction.respond(content="Error. I saved error in my error database, my creator will check out.")

client.run(config['id_runner'])