#{}calc - Count with bot
import discord
import os
import glob
import json
import utils
import asyncio
import string

async def Cmd(language, serverlang, message, client):
    try:
        letlater = True
        count = message.content.replace(message.content.split(" ")[0], '')
        for i in count:
            if(i in string.ascii_letters):
                letlater = False
        if(letlater == False):
            await message.channel.send("Bro, operations are + - * /, you don't need letters.")
        else:
            try:
                calculation = eval(count)
            except Exception as exexex:
                if(exexex == "invalid syntax (<string>, line 1)"):
                    await message.channel.send("I don't understand, maybe try putting multiplying symbol before brackets and operations are + - * /.")
            try:
                calculation = int(calculation)
                await message.channel.send(f"{count} = {calculation}")
            except:
                await message.channel.send("I had problem, maybe try putting multiplying symbol before brackets.")
    except RuntimeWarning:
        pass
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")