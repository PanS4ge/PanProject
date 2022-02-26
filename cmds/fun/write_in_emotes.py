#{}write_in_emotes (text) - Writes text in regional indicators.
import discord
import json
import string

async def Cmd(language, serverlang, message, client):
    prefix = {}
    with open("prefix.json", "r") as welcom:
        prefix = json.loads(welcom.read())

    useprefix = ""
    try:
        useprefix = prefix[str(message.guild.id)]
    except KeyError:
        useprefix = "?"

    temp = ""
    for x in str(message.content).replace(useprefix + "write_in_emotes ", ''):
        if(x in string.ascii_letters):
            temp = temp + f":regional_indicator_{x.lower()}: "
        elif(x == "1"):
            temp = temp + f":one: "
        elif(x == "2"):
            temp = temp + f":two: "
        elif(x == "3"):
            temp = temp + f":three: "
        elif(x == "4"):
            temp = temp + f":four: "
        elif(x == "5"):
            temp = temp + f":five: "
        elif(x == "6"):
            temp = temp + f":six: "
        elif(x == "7"):
            temp = temp + f":seven: "
        elif(x == "8"):
            temp = temp + f":eight: "
        elif(x == "9"):
            temp = temp + f":nine: "
        elif(x == "0"):
            temp = temp + f":zero: "
        elif(x == "#"):
            temp = temp + f":hash: "
        elif(x == "*"):
            temp = temp + f":asterisk: "
        else:
            pass

    await message.channel.send(temp)
    await message.channel.send(f"```{temp}```")