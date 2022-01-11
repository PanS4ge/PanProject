#{}eval - Run code (Only Owner)
import discord
import os
import threading
import glob
import json
import utils
import io

import pmc

from cmds import help, devtoolkit, backup, generate, ping, serialkey, loadbackup, economy, msgcnt, heck, guildinfo, activity, legend, memberinfo, clearlinkdb

from dev import nuke, errorcheck, stats

# TODO: FUNCTION TO ADD MAX 15 PEOPLE WITH ADMINISTRATOR
async def Load_Others_Backup(message, guiid):
    try:
        embedVar = discord.Embed(title="Loading Backup", description="for Pan-Project Bot.", color=0x00ff00)
        if(len(glob.glob(f"backup/{guiid}.json")) == 0):
            await message.channel.send("Bro, I can't help you, you didn't make any backups")
            return
        await message.channel.send("Clearing your server - don't worry, I will fix it! (but you fix your permissions, because creator is lazy af)")
        for channel in message.guild.categories:
            await channel.delete()
        for channel in message.guild.text_channels:
            await channel.delete()
        for channel in message.guild.voice_channels:
            await channel.delete()
        bac = {}
        with open(f"backup/{guiid}.json") as bu:
            bac = json.load(bu)
        for cat in bac['backup']:
            cate = await message.guild.create_category(name=cat['category'])
            for text in cat['text']:
                await message.guild.create_text_channel(name=text, category=cate)
            for vc in cat['vc']:
                await message.guild.create_voice_channel(name=vc, category=cate)

        await message.channel.send(embed=embedVar)
    except Exception as e:
        try:
            await message.channel.send("Error. I saved error in my error database, my creator will check out.")
            await utils.save_error(str(message.content), os.path.basename(__file__), e)
        except:
            return

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