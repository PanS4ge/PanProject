#{}terminal - Run command in terminal (Only owner)||{}micup - mic up kid
import discord
import os
import threading
import glob
import json
import utils
import io

import pmc

from cmds import help, devtoolkit, backup, generate, ping, serialkey, loadbackup, economy, msgcnt, heck, guildinfo, activity, legend, memberinfo, clearlinkdb

from dev import nuke, errorcheck, stats

async def Cmd(message):
    try:
            try:
                if(utils.is_owner_of_bot(message.author.id)):
                    evalDone = str(message.content).replace(str(message.content).split(" ")[0], "")
                    pope = os.popen(evalDone)
                    for wlin in pope.readlines():
                        await message.channel.send(f"`{wlin}`")
                else:
                    await message.channel.send("Only for owner")
            except Exception as e:
                if (utils.is_owner_of_bot(message.author.id)):
                    await message.channel.send("Invalid cmd")
                else:
                    await message.channel.send("Only for owner")
    except:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")