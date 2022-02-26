#{}backup - Backup your server in case of raid.
import os
import time
import datetime

import json

import discord

import utils

async def Cmd(language, serverlang, message, client):
    try:
        if (not(utils.has_permission(message.author, "manage_guild"))):
            return await message.channel.send("You need `MANAGE_GUILD` permission")
        timeunixxx = int(time.time())
        backup_str = {"backup": []}

        with open(f"backup/{message.guild.id}.json", "w") as f:
            f.write(" ")

        await message.channel.send(language[serverlang[str(message.guild.id)]]["backup"]['start_bu'])

        embedVar = discord.Embed(title=language[serverlang[str(message.guild.id)]]["backup"]['end_bu'], description=f"{language[serverlang[str(message.guild.id)]]['backup']['for']} {language[serverlang[str(message.guild.id)]]['backup']['bot_project_name']}", color=0x00ff00)
        dt = datetime.datetime.fromtimestamp(timeunixxx)
        embedVar.add_field(name=language[serverlang[str(message.guild.id)]]['backup']['date'], value=dt, inline=False)

        for category in message.guild.categories:
            temp = {"category": category.name, "text": [], "vc": []}
            tearr = []
            embedVar.add_field(name=f"{language[serverlang[str(message.guild.id)]]['backup']['category']}: ", value=category.name, inline=False)
            for text in message.guild.text_channels:
                if(text.category_id == category.id):
                    tearr.append(f"txt:{text.name}")
                    embedVar.add_field(name=f"{language[serverlang[str(message.guild.id)]]['backup']['text']}: ", value=text.name, inline=True)
                    temp["text"].append(text.name)
            for vc in message.guild.voice_channels:
                if (vc.category_id == category.id):
                    tearr.append(f"vc:{vc.name}")
                    embedVar.add_field(name=f"{language[serverlang[str(message.guild.id)]]['backup']['vc']}: ", value=vc.name, inline=True)
                    temp["vc"].append(vc.name)
            backup_str["backup"].append(temp)
        with open(f"backup/{message.guild.id}.json", "w") as f:
            f.write(json.dumps(backup_str, indent=4))
        await message.channel.send(embed=embedVar)
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send(language[serverlang[str(message.guild.id)]]['global']['error_save'])

