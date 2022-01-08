#{}eval - Run code (Only Owner)
import discord
import os
import threading
import glob
import json
import utils

import pmc

from cmds import help, devtoolkit, backup, generate, ping, serialkey, loadbackup, economy, msgcnt, heck, guildinfo, activity, legend, memberinfo, clearlinkdb

from dev import nuke, errorcheck, stats

# TODO: FUNCTION TO ADD MAX 15 PEOPLE WITH ADMINISTRATOR

def Add_Partnered_Server(guiid):
    badge = {}
    with open(f"partnered_server_id.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    badge['badges'].append(guiid)
    with open(f"partnered_server_id.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

def Remove_Partnered_Server(guiid):
    badge = {}
    with open(f"partnered_server_id.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    badge['badges'].remove(guiid)
    with open(f"partnered_server_id.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

def Create_Badge(emoji, name, desc, owners):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    addthis = {"id": len(badge['badge']), "emoji": emoji, "name": name, "description": desc, "owners": owners}
    badge['badge'].append(addthis)
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

def Add_Badge(ide, towho):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    badge['badge'][ide]['owners'].append(towho)
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

def Remove_Badge(ide, towho):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    badge['badge'][ide]['owners'].remove(towho)
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

def Have_Badge(ide, towho):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    return towho in badge['badge'][ide]['owners']

def Fetch_Badges(towho):
    badge = {}
    allbadges = []
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    for x in badge['badge']:
        if(towho in x['owners']):
            allbadges.append(x['emoji'])
    return allbadges

def Clear_Badges(ide):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    badge['badge'][ide]['owners'] = []
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

async def Cmd(message, client):
    try:
        if("await " in message.content):
            try:
                if (utils.is_owner_of_bot(message.author.id)):
                    evalDone = await eval(str(message.content).replace(str(message.content).split(" ")[0], "").replace("await ", ""))

                    embedEval = discord.Embed(title=":white_check_mark: Eval!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",
                                        value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f"{evalDone}")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for owner")
            except Exception as e:
                if (utils.is_owner_of_bot(message.author.id)):
                    embedEval = discord.Embed(title=":negative_squared_cross_mark: Eval!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",
                                        value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f":x: {e} :x:")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for owner")
        else:
            try:
                if(utils.is_owner_of_bot(message.author.id)):
                    evalDone = eval(str(message.content).replace(str(message.content).split(" ")[0], ""))

                    embedEval = discord.Embed(title=":white_check_mark: Eval!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got", value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f"{evalDone}")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for owner")
            except Exception as e:
                if (utils.is_owner_of_bot(message.author.id)):
                    embedEval = discord.Embed(title=":negative_squared_cross_mark: Eval!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f":x: {e} :x:")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for owner")
    except:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")