#{}vc_activity list - Activities for your vc!
import math

import discord
from discord_together import DiscordTogether
import dislash

import json
import random

import utils
import json

activities = ['youtube', 'poker', 'chess', 'betrayal', 'fishing', 'letter-league', 'word-snack', 'sketch-heads', 'spellcast', 'awkword', 'checkers']

def Get_Connected_VC(message):
    for x in message.guild.voice_channels:
        if(message.author in x.members):
            return x.id
    return 2137

config = {}
with open("config.json", "r") as conf:
    config = json.loads(conf.read())

async def Cmd(language, serverlang, message, client : discord.Client):
    client.togetherControl = await DiscordTogether(config['token_normal'])
    try:
        if(str(message.content).split(" ")[1] == "list"):
            await message.channel.send(f"Here's activities list for **Pansage Bot!**\n\n" +
                                       f"<:youtube:941290504614731776> Watch Together (0 <:boost:941067904777064468>), use `youtube`\n" +
                                       f"<:pokercoin:941290504895758386> Poker Night (1 <:boost:941067904777064468>), use `poker`\n" +
                                       f"<:checkmate:941290504853803008> Chess in the Park (1 <:boost:941067904777064468>), use `chess`\n" +
                                       f"<:puppycatbetrayal:941290504899948564> Betrayal.io (0 <:boost:941067904777064468>), use `betrayal`\n" +
                                       f"<:chibipaimonfishing:941290505025769502> Fishington.io (0 <:boost:941067904777064468>), use `fishing`\n" +
                                       f"<:letter:941290504866381846> Letter League (1 <:boost:941067904777064468>), use `letter-league`\n" +
                                       f"<:PencilOof:941290504228835339> Sketch Heads (0 <:boost:941067904777064468>), use `sketch-heads`\n" +
                                       f"<:healermagicmagickawand:941290504681840680> SpellCast (1 <:boost:941067904777064468>), use `spellcast`\n" +
                                       f"<:ninja2thonks:941290504467918918> Awkword (1 <:boost:941067904777064468>), use `awkword`\n" +
                                       f"<:gamerkeyboard:941290815462977546> Checkers in the Park (1 <:boost:941067904777064468>), use `checkers`\n" +
                                       f"<:PeepoSnack:941290505826873364> Word Snack (0 <:boost:941067904777064468>), use `word-snack`")
        elif(str(message.content).split(" ")[1] in activities):
            if(Get_Connected_VC(message) != 2137):
                try:
                    link = await client.togetherControl.create_link(Get_Connected_VC(message), str(message.content).split(" ")[1])
                    await message.channel.send(f"At least one person needs to click on the BLUE LINK, not the 'Play' button, in order to start the activity! Once the activity is started, people can join by clicking 'Play'.\nClick the blue link!\n{link}")
                #await client.close()
                except:
                    await message.channel.send("It doesn't exist.")
            else:
                await message.channel.send("Connect to vc idot")
        else:
            await message.channel.send("Invalid activity, try activity list for possibilities!")
    except:
        await message.channel.send("Invalid activity, try activity list for possibilities!")