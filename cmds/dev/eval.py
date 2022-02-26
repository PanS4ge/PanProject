#{}eval - Run code (Only Owner)
import discord
import os
import glob
import json
import utils
import asyncio

from rem_cmds import generate
from rem_cmds import serialkey

async def Send_All_Backgrounds(message):
    #print("Starting...")
    for x in range(len(glob.glob("cmds/image_data/bg/*.png")) + 1):
        if(x == 0):
            await message.channel.send("id: 0\n(Empty)")
        else:
            #print(x)
            #await message.channel.send(f"id: {x.replace('cmds/image_data/bg\\', '').replace('.jpg', '')}")
            if(x != 6):
                bs = "\\"
                await message.channel.send(content=f"id: {str(x)}", file=discord.File(os.path.abspath(f"cmds/image_data/bg/{str(x)}.png")))
            else:
                bs = "\\"
                await message.channel.send(content=f"id: {str(x)} - has empty space", file=discord.File(os.path.abspath(f"cmds/image_data/bg/{str(x)}.png")))


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

async def Send_Message(towho, message):
    await towho.send(message)

async def Clear_Messages_Globally(message, memid):
    for x in message.guild.text_channels:
        yee = await x.history(limit=200).flatten()
        for y in yee:
            if(y.author.id == memid):
                try:
                    await y.delete()
                except:
                    pass

async def Clear_Badge_Roles(message):
    yee = await message.guild.fetch_roles()
    for x in yee:
        if(x.name.endswith("badge owners")):
            await x.delete()
    return "Cleared!"

async def Create_Badges_Role(message):
#def Create_Badges_Role(message):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    for x in badge["badge"]:
        role = await message.guild.create_role(name=x["name"] + " badge owners")
        x["role_id"] = role.id
        if(len(x["owners"]) != 0):
            for y in x["owners"]:
                try:
                    pee = message.guild.get_member(y)
                    await pee.add_roles(role)
                    print(f"Added {pee.name} to {x['name']} badge owners")
                except:
                    print("Error in there")
            await asyncio.sleep(5)
        print(f"Created {x['name']} badges owners")
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge, indent=4))
        cny.close()

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

async def Give_Role(message, memid, rolid):
    mem = await message.guild.fetch_member(memid)
    rol = message.guild.get_role(rolid)
    await mem.add_roles(rol)

async def Cmd(language, serverlang, message, client):
    try:
        if("await " in message.content):
            try:
                if (utils.is_owner_of_bot(message.author.id)):
                    evalDone = await eval(str(message.content).replace('await ', '').replace(str(message.content).split(" ")[0], ''))
                    #print(str(message.content).replace('await ', '').split(" ")[2])

                    embedEval = discord.Embed(title=":white_check_mark: Eval!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",
                                        value=f'{str(message.content).replace("await ", "").replace(str(message.content).split(" ")[0], "")}')
                    embedEval.add_field(name=":outbox_tray: Back", value=f"{evalDone}")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for dev")
            except Exception as e:
                if (utils.is_owner_of_bot(message.author.id)):
                    embedEval = discord.Embed(title=":negative_squared_cross_mark: Eval!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",
                                        value=f'{str(message.content).replace(str(message.content).split(" ")[0], "")}')
                    embedEval.add_field(name=":outbox_tray: Back", value=f":x: {e} :x:")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for dev")
        else:
            try:
                if(utils.is_owner_of_bot(message.author.id)):
                    evalDone = eval(str(message.content).replace(str(message.content).split(" ")[0], ''))

                    embedEval = discord.Embed(title=":white_check_mark: Eval!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got", value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f"{evalDone}")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for dev")
            except Exception as e:
                if (utils.is_owner_of_bot(message.author.id)):
                    embedEval = discord.Embed(title=":negative_squared_cross_mark: Eval!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f":x: {e} :x:")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for dev")
    except RuntimeWarning:
        pass
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")