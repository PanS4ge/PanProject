#{}do_i_have_perms - Checks if you have permission
import discord
import requests
import json

import utils

async def Cmd(language, serverlang, message, client):
    if(utils.has_sc_perms(message.author.id)):
        await message.channel.send("<:yeee:928675155465621525>")
    else:
        await message.channel.send("<:nope:928675155440443503>")