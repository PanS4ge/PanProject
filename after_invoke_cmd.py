import discord
import discord_components
import time
import random

from discord_components import DiscordComponents

one = 0
two = 0
three = 0
four = 0
five = 0

def Count_Votes(cnt):
    if(cnt == 1):
        one = one + 1
    if(cnt == 2):
        two = two + 1
    if(cnt == 3):
        three = three + 1
    if(cnt == 4):
        four = four + 1
    if(cnt == 5):
        five = five + 1

async def Cmd(client):
    try:
        DiscordComponents(client)
        global one, two, three, four, five
        await Daily_Poll(client)
    except Exception as ecv:
        print(f"Unable to load after_invoke_cmd.py\n{ecv}")

async def Daily_Poll(client):
    quesno = 0
    with open("quesno.txt", "r") as qn:
        quesno = qn.read()
    while True:
        quesno = quesno + 1
        with open("quesno.txt", "w") as qn:
            qn.write(quesno)
        with open("poll_questions.txt", "r") as jgs:
            array = []
            for x in jgs.readlines():
                array.append(x)
            nm = random.randint(0, int(array) - 1)
            temp = array[nm]
            embedVar = discord.Embed(
                title="Todays question",
                description=temp.split("-")[0], color=0x00ffff)
            ar = [[]]
            for x in temp.split("-")[1].split("/"):
                ar[0].append(Button(style=ButtonStyle.blue, label="x", custom_id=str(len(ar[0]))))
            chanid = client.get_channel(928717155313270794)
            await chanid.send(embed=embedVar, components=ar)
        time.sleep(60*60*24)
        ar = [[]]
        embedVar = discord.Embed(
            title="Results:",
            description=f"1. {str(one)} - {str(((one/one+two+three+four+five)*100))}%\n2. {str(two)} - {str((two/one+two+three+four+five)*100)}\n3. {str(three)} - {str((three/one+two+three+four+five)*100)}\n4. {str(four)} - {str((four/one+two+three+four+five)*100)}%\n5. {str(five)} - {str((five/one+two+three+four+five)*100)}%", color=0x00ffff)
