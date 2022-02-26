#{}bot_stats - Sends you info about bot
import asyncio
import matplotlib.pyplot as plt

import discord
import requests

import glob
import sys
import discord
import json

import utils

async def Cmd(language, serverlang, message, client):
    #print(info)
    bad = 1
    good = 1
    for foldersa in glob.glob(f"cmds/*/"):
        # print(foldersa)
        if (int(len(glob.glob(f"{foldersa}/*/"))) > 2):
            # print(int(len(glob.glob(f"{foldersa}/*/"))))
            for foldererer in glob.glob(f"{foldersa}/*/"):
                for folderer in glob.glob(f"{foldererer}/*.py"):
                    # print(folderer)
                    package = folderer.replace(foldererer, "").replace(".py", "")
                    try:
                        if (f'{foldererer.replace(backslashes, ".")}{package}' in sys.modules):
                            good = good + 1
                        else:
                            bad = bad + 1
                    except Exception as exept:
                        bad = bad + 1
                    except:
                        bad = bad + 1
        else:
            for x in glob.glob(f"{foldersa}/*.py"):
                package = x.replace(foldersa, "").replace(".py", "")
                backslashes = "\\"
                try:
                    if (f'{foldersa.replace(backslashes, ".")}{package}' in sys.modules):
                        good = good + 1
                    else:
                        bad = bad + 1
                except Exception as exept:
                    bad = bad + 1
                except:
                    bad = bad + 1
    for x in glob.glob(f"dev/*.py"):
        package = x.replace("dev\\", "").replace(".py", "")
        backslashes = "\\"
        try:
            if (f'dev.{package}' in sys.modules):
                good = good + 1
            else:
                bad = bad + 1
        except Exception as exept:
            bad = bad + 1
        except:
            bad = bad + 1
    labels = ["working (there was +1)", "broken (there was +1)"]
    sizes = [good, bad]
    explode = [0.1, 0.1]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig("output.png")

    websitestat = "<:nope:928675155440443503>"
    apitest = "<:nope:928675155440443503>"
    apitest2 = "<:yeee:928675155465621525>"
    apiuptime = "<:nope:928675155440443503>"

    req1 = requests.request("GET", "https://pansage-bot.glitch.me/does-it-work.html")
    if(req1.text.startswith("yes")):
        websitestat = "<:yeee:928675155465621525>"

    req2 = requests.request("GET", "https://psbapi.herokuapp.com/apitest")
    if(req2.text.startswith("Hello World!")):
        apitest = "<:yeee:928675155465621525>"

    req3 = requests.request("GET", "https://psbapi.herokuapp.com/apitest/uptime")
    if(req3.text == "{\"hello\": \"world\", \"love\": \"beans\"}"):
        apitest2 = "<:nope:928675155440443503>"

    embedVar = discord.Embed(title=f"Here's bot statistics", description=f"Commands: {str(good + bad - 2)}\nWorking: {str(good - 1)}\nNot working: {str(bad - 1)}\n\nWebsite: {websitestat}\nAPI (is up): {apitest}\nAPI (has data): {apitest2}\n\nHere is statistics of my commands.",
                             color=0x00ff00)
    file = discord.File("C:/Users/User/PycharmProjects/discord.py/output.png", filename="output.png")
    embedVar.set_image(url="attachment://output.png")
    await message.channel.send(file=file, embed=embedVar)