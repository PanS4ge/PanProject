# Error Check - Check logs from error.json
import json
import os

import discord
from discord_components import Button, ButtonStyle

import utils

errors_structure = """{"errors": []}"""

async def ReturnCmd(idres):
    try:
        if (not (utils.is_owner_of_bot(idres))):
            embedVar = discord.Embed(title="Error Check", description="for Pan-Project Bot.", color=0xff0000)
            embedVar.add_field(name="Error.", value="I can't allow you", inline=False)
            return embedVar
        error = {}
        loc = os.environ['PYTHONPATH'].replace(__file__, "")
        with open(f"{loc}/cmds/error.json", encoding='utf8') as data:
            error = json.load(data)

        embedVar = discord.Embed(title="Error Check", description="for Pan-Project Bot.", color=0x00ff00)
        if (len(error['errors']) >= 1):
            for x in error['errors']:
                #print(x)
                try:
                    embedVar.add_field(name=x['error'], value=x['crashed_file'] + " / " + x['message'], inline=False)
                except:
                    embedVar.add_field(name="Too long message or something", value=x['crashed_file'] + " / Check in error.json", inline=False)
            #with open(f"{loc}/cmds/error.json", "w", encoding='utf8') as f:
            #    f.write(errors_structure)
        if (len(error['errors']) == 0):
            embedVar.add_field(name="No errors!", value="Bot is error-proof!", inline=False)
        return embedVar
    except Exception as e:
        await utils.save_error("Error Check / DevToolKit", os.path.basename(__file__), e)
        embedVar = discord.Embed(title="Error Check", description="for Pan-Project Bot.", color=0xff0000)
        embedVar.add_field(name="Error.", value="I saved error in my error database, my creator will check out.", inline=False)
        return embedVar

