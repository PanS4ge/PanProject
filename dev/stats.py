# Stats - Get statistics of bot
import os
import psutil

import discord

import utils


async def ReturnCmd(idres):
    try:
        if (not (utils.is_owner_of_bot(idres))):
            embedVar = discord.Embed(title="Error Check", description="for Pan-Project Bot.", color=0xff0000)
            embedVar.add_field(name="Error.", value="I can't allow you", inline=False)
            return embedVar

        embedVar = discord.Embed(title="Error Check", description="for Pan-Project Bot.", color=0x00ff00)
        embedVar.add_field(name="CPU Percents", value=f"`{psutil.cpu_percent(interval=1, percpu=True)}`", inline=False)
        embedVar.add_field(name=f"RAM", value=f"`{psutil.virtual_memory()}`", inline=False)
        embedVar.add_field(name=f"SWAP", value=f"`{psutil.swap_memory()}`", inline=False)
        embedVar.add_field(name=f"Network", value=f"`{psutil.net_io_counters(pernic=False, nowrap=False)}`", inline=False)
        return embedVar
    except Exception as e:
        await utils.save_error("Stats / DevToolKit", os.path.basename(__file__), e)
        embedVar = discord.Embed(title="Stats", description="for Pan-Project Bot.", color=0xff0000)
        embedVar.add_field(name="Error.", value="I saved error in my error database, my creator will check out.", inline=False)
        return embedVar

