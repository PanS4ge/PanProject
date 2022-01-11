#{}random_prntsc - Sorry bro, god bless your eyes
import os
import discord
import time

import string
import random

import utils

async def Cmd(message):
    try:
        await message.channel.send("Sorry, bro. God bless your eyes! Hope it isn't that bad!")
        randomurl = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))
        await message.channel.send("https://prnt.sc/" + randomurl)
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")
