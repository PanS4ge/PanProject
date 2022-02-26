#{}count - Count how many times the word was said on this channel
import asyncio

import discord
import requests
import matplotlib.pyplot as plt

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

url = "https://random-word-api.herokuapp.com/word?number=1"
gaveword = False

async def Cmd(language, serverlang, message, client):
    try:
        word = str(message.content).split(" ")[1]
        gaveword = True
    except:
        response = requests.get(url)
        data_json = response.json()
        word = data_json[0]
    cntmsg = await message.channel.send(f"<a:loading:936978619639668787> Getting history of this channel...")
    messages = await message.channel.history(limit=None).flatten()
    await cntmsg.edit(f"<a:loading:936978619639668787> Got it, searching for word *{word}* in messages...")
    count = 0
    whosaid = []
    for msgs in messages:
        if(word in str(msgs.content)):
            count = count + 1
            whosaid.append(str(msgs.author).encode("ascii", "ignore").decode())
    await cntmsg.edit("<a:loading:936978619639668787> Got it, now getting only unique elements...")
    whosaidagain = unique(whosaid)
    await cntmsg.edit("<a:loading:936978619639668787> Got it, now generating chart...")
    try:
        #labels = []
        #sizes = []
        #explode = []
        #for x in whosaidagain:
        #    temp = 0
        #    for y in messages:
        #        if(str(y.author.name).encode("ascii", "ignore").decode() == x and word in str(message.content)):
        #            temp = temp + 1
        #    if(temp != 0):
        #        labels.append(x)
        #        sizes.append(temp)
        #        explode.append(0.1)
        #
        #if(count >= int(len(messages) / 10)):
        #    labels.append(f"Without word {word}")
        #    sizes.append(len(messages) - count)
        #    explode.append(0.2)
        #fig1, ax1 = plt.subplots()
        #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        #        shadow=True, startangle=90)
        #ax1.axis('equal')
        #plt.savefig("output.png")

        if(word == "kremówka"):
            count = 2137

        await cntmsg.edit("<a:loading:936978619639668787> Generating embed message...")

        embedVar = discord.Embed(title=f"Here's a chart of people saying {word}", description=".",
                                 color=0x00ff00)
        embedVar.add_field(name=f"There are {str(count)} messages with {word}", value="I love beans!")
        #file = discord.File("C:/Users/User/PycharmProjects/discord.py/output.png", filename="output.png")
        #embedVar.set_image(url="attachment://output.png")
        await cntmsg.delete()
        await message.channel.send(content="Here is the final product!", embed=embedVar)#, file=file, embed=embedVar)
    except Exception as exex:
        await cntmsg.edit(f"Error creating Chart, probably too much messages too handle.\nI counted {word}, and it was written {str(count)} times!")
        print(exex)