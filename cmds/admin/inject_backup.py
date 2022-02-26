#{}inject_backup - Injects backup files to bot.
import discord
import requests
import json

async def Cmd(language, serverlang, message, client):
    if(len(message.attachments) == 0):
        await message.channel.send("Send JSON file")
    elif(len(message.attachments) >= 2):
        await message.channel.send("Send only one file.")
    else:
        try:
            with open(f"backup/injected/{str(message.guild.id)}_injected.json", "w") as peepee:
                try:
                    yee = await message.attachments[0].read()
                    peepee.write(json.dumps(str(yee), indent=4))
                    await message.channel.send("Saved backup, you can load it using `?loadbackup injected`")
                except:
                    await message.channel.send("Error with writing file...")
        except:
            await message.channel.send("Error!")