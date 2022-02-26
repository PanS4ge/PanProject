#{}log_msg (msg number) - Logs messages in txt file.
import glob

import discord
import random

async def Cmd(language, serverlang, message, client):
    try:
        if(int(message.content.split(" ")[1]) > 25000):
            await message.channel.send("Bro, you will lag me out :(")
        else:
            msgar = await message.channel.history(limit=int(message.content.split(" ")[1])).flatten()
            with open("messages.txt", "w") as msgs:
                msgs.write("")
            with open("messages.txt", "a") as msgs:
                for msglog in range(1, len(msgar) + 1):
                    try:
                        msgs.write(f"{msgar[(msglog * -1) - 1].author.display_name.encode('ascii', 'ignore').decode()}#{msgar[(msglog * -1) - 1].author.discriminator} > {msgar[(msglog * -1) - 1].content.encode('ascii', 'ignore').decode()}\n")
                    except:
                        try:
                            msgs.write(f"{msgar[(msglog * -1) - 1].author.display_name.encode('ascii', 'ignore').decode()}#{msgar[(msglog * -1) - 1].author.discriminator} > Unable to get content\n")
                        except:
                            pass
            file = discord.File("messages.txt", filename="messages.txt")
            await message.channel.send(file=file)
    except:
        await message.channel.send("Wrong number")