#{}loadbackup - Raided? Load your backup
import os
import glob
import json

import discord

import utils

async def Cmd(message):
    try:
        if (not (await utils.admin_perms(message, message.author))):
            return

        embedVar = discord.Embed(title="Loading Backup", description="for Pan-Project Bot.", color=0x00ff00)
        if(len(glob.glob(f"backup/{message.guild.id}.json")) == 0):
            await message.channel.send("Bro, I can't help you, you didn't make any backups")
            return
        await message.channel.send("Clearing your server - don't worry, I will fix it! (but you fix your permissions, because creator is lazy af)")
        for channel in message.guild.categories:
            await channel.delete()
        for channel in message.guild.text_channels:
            await channel.delete()
        for channel in message.guild.voice_channels:
            await channel.delete()
        bac = {}
        with open(f"backup/{message.guild.id}.json") as bu:
            bac = json.load(bu)
        for cat in bac['backup']:
            cate = await message.guild.create_category(name=cat['category'])
            for text in cat['text']:
                await message.guild.create_text_channel(name=text, category=cate)
            for vc in cat['vc']:
                await message.guild.create_voice_channel(name=vc, category=cate)

        await message.channel.send(embed=embedVar)
    except Exception as e:
        try:
            await message.channel.send("Error. I saved error in my error database, my creator will check out.")
            await utils.save_error(str(message.content), os.path.basename(__file__), e)
        except:
            return