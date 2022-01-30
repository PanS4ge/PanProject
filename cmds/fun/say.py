#{}say - Says what user wants
import discord

async def Cmd(language, serverlang, message, client):
    if ("lubi" in user_msg.lower() and "dis" in user_msg.lower()):
        await message.channel.send("JD kuwo, spierdalaj bo banicje dostaniesz")
    elif ("kocha" in user_msg.lower() and "dis" in user_msg.lower()):
        try:
            await message.author.ban(reason="Kochanie disa (gay moment)")
            await message.channel.send("Dostal banicje, o jednego \"kochanka\" disa mniej.")
        except:
            pass
    elif ("1 2 7 3" in user_msg.lower()):
        await message.channel.send(
            "... down to Rockefeller Street\nLife is marchin' on do you feel that\n1273, down to Rockefeller Street\nEverything is more than surreal (than surreal)")
    elif ("21:37" in user_msg.lower()):
        await message.channel.send(
            "Pan kiedyś stanął nad brzegiem,\nSzukał ludzi gotowych pójść za Nim;\nBy łowić serca\nSłów Bożych prawdą.\n\nO Panieeee, to Ty na mnie spojrzałeś,\nTwoje usta dziś wyrzekły me imię.\nSwoją barkę pozostawiam na brzegu,\nRazem z Tobą nowy zacznę dziś łów.")
    else:
        await message.channel.send(user_msg.replace("?say ", ""))