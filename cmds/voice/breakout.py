#{}breakout create (count) - Put your people to breakout channels (need move_members)||{}breakout send (channel id) - Send people back to channel by ID (need move_members)
import math

import discord
import json
import random

import utils


def Get_Connected_VC(message):
    for x in message.guild.voice_channels:
        if(message.author in x.members):
            return x.id
    return 2137

async def Cmd(language, serverlang, message, client):
    if(utils.has_permission(message.author, "move_members")):
        if(str(message.content).split(" ")[1] == "create"):
            vc = Get_Connected_VC(message)
            if(vc == 2137):
                await message.channel.send("You aren't on channel")
            try:
                count = int(message.content.split(" ")[2])
                embedVar = discord.Embed(title=f"Made {count} breakout channels", description="and sent people to them.", color=0x00ff00)
                catteg = await message.guild.create_category("Breakout rooms.")
                jd = []
                memb = client.get_channel(vc).members
                if(count > len(memb)):
                    await message.channel.send("Too less people for that count of rooms")
                    return
                for x in range(1, count + 1):
                    channel = await message.guild.create_voice_channel(f"Breakout room #{x}", category=catteg)
                    jd.append(channel)

                #if(len(client.get_channel(vc).members) > 0):
                #    for x in client.get_channel(vc).members:
                #        c = random.choice(jd)
                #        await x.move_to(c)
                times = len(memb)
                for x in jd:
                    for y in range(math.floor(times / count)):
                        try:
                            yes = random.choice(memb)
                            memb.remove(yes)
                            await yes.move_to(x)
                        except:
                            pass

                if (len(memb) > 0):
                    for y in memb:
                        team = random.randint(1, count + 1)
                        yes = random.choice(memb)
                        memb.remove(yes)
                        #print(f"POMINETE: {yes} do teamu #{team}")

                for x in message.guild.voice_channels:
                    if (x.name.startswith("Breakout")):
                        temp2 = "List:\n"
                        for y in x.members:
                            temp2 = temp2 + f"{y.display_name}#{y.discriminator}\n"
                        embedVar.add_field(name=x.name, value=temp2)
                        #temp2 = temp2 + f"{member.display_name}#{member.discriminator} - to {c.name}\n"
                    #if(temp2 != ""):
                    #    embedVar.add_field(name=f"Other ones to send", value=temp2)
                await message.channel.send(embed=embedVar)
            except Exception as exexexexexe:
                await message.channel.send(f"Error:\n{exexexexexe}")
                return
        elif(str(message.content).split(" ")[1] == "send"):
            try:
                for x in message.guild.voice_channels:
                    if(x.name.startswith("Breakout")):
                        for y in x.members:
                            await y.move_to(client.get_channel(int(str(message.content).split(" ")[2])))
                        await x.delete()
                for x in message.guild.categories:
                    if(x.name == "Breakout rooms."):
                        await x.delete()
                await message.channel.send("Done :D")
            except Exception as exexexexexe:
                await message.channel.send(f"Error:\n{exexexexexe}")
        else:
            await message.channel.send("create or send.")
    else:
        await message.channel.send("Need `MOVE_MEMBERS`.")