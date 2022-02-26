#{}say - Says what user wants
import discord
import json


async def Cmd(language, serverlang, message, client):
    prefix = {}
    with open("prefix.json", "r") as welcom:
        prefix = json.loads(welcom.read())
    if ("lubi" in message.content.lower() and "dis" in message.content.lower()):
        await message.channel.send("JD kuwo, spierdalaj bo banicje dostaniesz")
    elif ("kocha" in message.content.lower() and "dis" in message.content.lower()):
        try:
            await message.author.ban(reason="Kochanie disa (gay moment)")
            await message.channel.send("Dostal banicje, o jednego \"kochanka\" disa mniej. (" + message.author + " / " + str(message.author.id) + ")")
        except:
            pass
    elif ("1 2 7 3" in message.content.lower()):
        await message.channel.send(
            "... down to Rockefeller Street\nLife is marchin' on do you feel that\n1273, down to Rockefeller Street\nEverything is more than surreal (than surreal)")
    elif ("21:37" in message.content.lower()):
        await message.channel.send(
            "Pan kiedyś stanął nad brzegiem,\nSzukał ludzi gotowych pójść za Nim;\nBy łowić serca\nSłów Bożych prawdą.\n\nO Panieeee, to Ty na mnie spojrzałeś,\nTwoje usta dziś wyrzekły me imię.\nSwoją barkę pozostawiam na brzegu,\nRazem z Tobą nowy zacznę dziś łów.")
    else:
        useprefix = ""
        try:
            useprefix = prefix[str(message.guild.id)]
        except KeyError:
            useprefix = "?"
        await message.delete()
        await message.channel.send(message.content.replace(useprefix, "").replace("say ", "").replace("@", ""))