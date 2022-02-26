#{}ping - Gets latency of bot
import os
import discord
import time

import utils

saved_ping = 0

def get_num_array(array):
    temp = 0
    for ye in array:
        temp = temp + ye
    return temp / len(array)

def get_ping():
    return saved_ping

async def Cmd(language, serverlang, message, client):
    try:
        try:
            if(str(message.content).split(" ")[1] != None):
                try:
                    temp = []
                    if(int(str(message.content).split(" ")[1]) > 10):
                        await message.channel.send("Too much rounds")
                    for x in range(int(str(message.content).split(" ")[1])):
                        before = time.monotonic()
                        msg = await message.channel.send("**PING!** Awaiting for pong!")
                        ping = (time.monotonic() - before) * 1000
                        await msg.edit(content=f"🏓 Pong! {int(ping)}ms")
                        await msg.delete()
                        temp.append(int(ping))
                    saved_ping = get_num_array(temp)
                    await message.channel.send(f"""🏓Pong! After {str(message.content).split(" ")[1]} ping, ratio is {get_num_array(temp)}ms""")
                except:
                    await message.channel.send("Invalid round number")
        except:
            before = time.monotonic()
            msg = await message.channel.send("**PING!** Awaiting for pong!")
            ping = (time.monotonic() - before) * 1000
            saved_ping = ping
            await msg.edit(content=f"🏓 Pong! {int(ping)}ms")
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")
