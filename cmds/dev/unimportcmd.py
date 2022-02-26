#{}unimportcmd (package) - Unimports command mid-run (only dev)
import discord
import kernel
import utils
import importlib

def importpackage(package):
    try:
        globals()[package] = "UNLOADED"
        return f"{package} was removed!"
    except Exception as ezezez:
        return ezezez

async def Cmd(language, serverlang, message, client):
    if(utils.is_owner_of_bot(message.author.id)):
        try:
            await message.channel.send(importpackage(message.content.split(" ")[1]))
        except:
            await message.channel.send("Invalid arguments")