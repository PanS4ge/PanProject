import random
import threading
import glob
import time

import discord
import json
import os
from discord_components import DiscordComponents

import BadgesManager
import after_invoke_cmd

import utils, pmc
import o1k_msg

from cmds import help, devtoolkit, backup, generate, ping, serialkey, mc_pfp, loadbackup, economy, msgcnt, heck, guildinfo, activity, legend, eval, memberinfo, clearlinkdb, random_prntscr, exec
from cmds import terminal

from manager import help as helpman
from manager import activity as actiman
from manager import devtoolkit as dtkman
from manager import gban, gunban

from dev import nuke, errorcheck, stats

panproj = ["normal", "manager"]

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

keys = {}
with open(f"serialkey.json", encoding='utf8') as data:
    keys = json.load(data)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    global whichone
    DiscordComponents(client)
    await client.change_presence(activity=discord.Game(name=f"good bro"))
    print("Successfully logged in.")
    #await after_invoke_cmd.Daily_Poll(client)

@client.event
async def on_guild_join(guild):
    guildname = guild.name
    guildid = guild.id
    temp = {}
    try:
        if(f"ecojson/{guildid}.json"):
            with open(f"ecojson/{guildid}.json", "w") as yee:
                yee.write(json.dumps(temp))
            #os.remove(f"ecojson/{guildid}.json")
    except:
        pass
    try:
        if(f"msgcount/{guildid}.json"):
            with open(f"msgcount/{guildid}.json", "w") as yee:
                yee.write(json.dumps(temp))
    except:
        pass
    #try:
    #    if(f"backup/{guildid}.json"):
    #        with open(f"msgcount/{guildid}.json", "w") as yee:
    #            yee.write(json.dumps(temp))
    #except:
    #    pass
    chanid = client.get_channel(927848602821349386)
    #link = client.create_invite(destination=guild, xkcd=True, max_age=0, max_uses=0)
    await chanid.send(f"\nI got added to server {guildname} ({guildid})")#\nHere's link to join {link}\n")

@client.event
async def on_guild_remove(guild):
    guildname = guild.name
    guildid = guild.id
    try:
        if(f"ecojson/{guildid}.json"):
            os.remove(f"ecojson/{guildid}.json")
    except:
        pass
    try:
        if(f"msgcount/{guildid}.json"):
            os.remove(f"msgcount/{guildid}.json")
    except:
        pass
    #try:
    #    if(f"backup/{guildid}.json"):
    #        os.remove(f"backup/{guildid}.json")
    #except:
    #    pass
    chanid = client.get_channel(927848602821349386)
    await chanid.send(f"\nI got kicked from server {guildname} ({guildid})\n")

@client.event
async def on_message(message):
    try:
        #print(message)
        if(message.channel.type == discord.ChannelType.private):
            return
        else:
            #try:
            username = str(message.author).split('#')[0]
            usertag = str(message.author).split('#')[1]
            userid = str(message.author.id)
            user_msg = str(message.content)
            channel = str(message.channel.name)
            #except:
            #    pass

            # TODO: FIX "ECO-GIANT" BADGE
            #try:
            #    BadgesManager.Clear_Badges(7)
            #    ggd = await economy.Get_Global_Data(client)
            #    ggd.sort(key=economy.sort_func, reverse=True)
            #    if (ggd[0]["name"] == message.guild.name):
            #        members = await message.guild.fetch_members(limit=None).flatten()
            #        for x in members:
            #            BadgesManager.Add_Badge(7, x.id)
            #except:
            #    pass

            #if("69" in message.content):
            #    await message.reply("nice.")

            if message.author == client.user:
                pass
            elif message.author.bot:
                pass

            if(message.channel.id == 929668126654750741 and message.content == "!d bump"):
                if(not(BadgesManager.Have_Badge(12, message.author.id))):
                    await message.channel.send(f"Thank you for bumping this server on disboard <@!{message.author.id}>, I see it's your first time bumping so take this ~~500~~ **1000** :fries: and badge BUMPER! Stay bumpin'")
                    await economy.Give_Money(message.guild.id, message.author.id, 1000)
                    BadgesManager.Add_Badge(12, message.author.id)
                else:
                    await message.channel.send(f"Thank you for bumping this server on disboard <@!{message.author.id}>, take this 500 :fries:! Stay bumpin'")
                    await economy.Give_Money(message.guild.id, message.author.id, 500)
            #with open("message_log.txt", "a") as log:
            #    log.write(f"({client.user}): " + username + "#" + usertag + " (" + userid + "): " + user_msg + " / " + message.guild.name + " -> #" + channel + "\n")

            whichone = ""
            for panp in panproj:
                if (config[f'token_{panp}'] == toktocheck):
                    whichone = panp
            #print(whichone)
            if (f"<@!{config[f'id_{whichone}']}>" in message.content):
                await message.channel.send(f"My prefix is `{config[f'prefix_{whichone}']}`, start with `{config[f'prefix_{whichone}']}help`")

            if(whichone == "normal"):
                await pmc.CheckMsg(message)

                if (message.author.id in config["gbans"]):
                    return await message.channel.send("You got gbanned - sorry!")
                else:
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "generate") or user_msg.startswith(config[f'prefix_{whichone}'] + "gen")):
                        await generate.Cmd(message, user_msg)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "help")):
                        await help.Cmd(message, whichone)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "exec")):
                        await exec.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "devtoolkit")):
                        await devtoolkit.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "mc_pfp")):
                        await mc_pfp.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "ping")):
                        await ping.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "guildinfo")):
                        await guildinfo.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "random_prntsc")):
                        await random_prntscr.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "memberinfo")):
                        await memberinfo.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "clear_links_db")):
                        await clearlinkdb.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "heck") or user_msg.startswith("$sudo_heck")):
                        await heck.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "backup")):
                        await backup.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "loadbackup")):
                        await loadbackup.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "add_bot")):
                        await message.channel.send("Thank you for supporting my bot!\nhttps://discord.com/api/oauth2/authorize?client_id=915657093862817802&permissions=8&scope=bot")
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco earn")):
                        await economy.Cmd_Earn(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco bal")):
                        await economy.Cmd_Bal(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco ccd")):
                        await economy.Cmd_ClearCD(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco clear")):
                        if(utils.is_owner_of_bot(userid)):
                            return await message.channel.send("Only for owner.")
                        try:
                            await economy.Set_Money(message.guild.id, user_msg.split(" ")[2], 0)
                            await message.channel.send("Cleared his :fries:")
                        except:
                            await message.channel.send("Invalid args")
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco set")):
                        await economy.Cmd_Set_Eco(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco send")):
                        await economy.Cmd_Send_Money(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "eco leaderboard")):
                        await economy.Cmd_Leaderboard(message, client)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "serialkey")):
                        await serialkey.Cmd(message)
                    #if(user_msg.startswith(config[f'prefix_{whichone}'] + "o1k")):
                    #    await o1k_msg.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "activity")):
                        await activity.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "msgcnt")):
                        await msgcnt.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "legend")):
                        await legend.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "eval")):
                        await eval.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "terminal")):
                        await terminal.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "say")):
                        if("lubi" in user_msg.lower() and "dis" in user_msg.lower()):
                            await message.channel.send("JD kuwo, spierdalaj bo banicje dostaniesz")
                        elif("kocha" in user_msg.lower() and "dis" in user_msg.lower()):
                            try:
                                await message.author.ban(reason="Kochanie disa (gay moment)")
                                await message.channel.send("Dostal banicje, o jednego \"kochanka\" disa mniej.")
                            except:
                                pass
                        else:
                            await message.channel.send(user_msg.replace("?say ", ""))
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "support_server")):
                        await message.channel.send("Join and you can get free 1,000 :fries: **on every server** and exclusive badge (:man_gesturing_ok:) on memberinfo\n-> https://discord.gg/4dRPUTsPza <-")
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "supserver_ad")):
                        await message.channel.send("**-------> Pan-Project Support Server <--------**\n:arrow_forward:  Do you get raided?\n:arrow_forward: Really annoyed by creating channels over and over?\n:arrow_forward: A lot of messages that offer nitro for free?\n:eye: **You are looking on solution right now!**\n:monkey_face: Pansage Bot is offering a lot of features such like:\n:white_small_square: Anti-Fishing :fish: \n:white_small_square: Scam links database with over 4,000 websites! :newspaper: \n:white_small_square: Backups :leftwards_arrow_with_hook: \n:white_small_square: Economy based on messages :speech_left: \n:white_small_square: Not only server leaderboards - but **global** leaderboards :globe_with_meridians: \n:white_small_square: Badges:military_medal: \n:white_small_square: Active developer :man_technologist: \n:white_small_square: Serial Keys to Windows products :key: \n*Remember that Piracy is no good, keys only for VM-testing*\nJoin andyou can get free 1,000 :fries: **on every server** and exclusive badge (:man_gesturing_ok:) on `?memberinfo`\n-> https://discord.gg/4dRPUTsPza <-\n\nAlso we are asking you to help us train the algorythm to prevent future scams! Send on `#🧛scam-links` channel (on support server) and we will add it to our database!")
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "c4k")):
                        await message.channel.send("Gotcha his ass")
                        await message.channel.send("https://c.tenor.com/QA6mPKs100UAAAAC/caught-in.gif")
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + 'micup')):
                        await message.channel.send("fuck off")
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "8ball")):
                        try:
                            responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
                                         "Cannot predict now.", "Concentrate and ask again.",
                                         "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.",
                                         "My reply is no.", "My sources say no.",
                                         "Outlook not so good.", "Outlook good.", "Reply hazy, try again.",
                                         "Signs point to yes.", "Very doubtful.", "Without a doubt.",
                                         "Yes.", "Yes – definitely.", "You may rely on it."]
                            msg8ball = await message.channel.send(f"8ball is now answering to question *{user_msg.replace(config[f'prefix_{whichone}'] + '8ball ', '')}*\nAnswer: Shaking 8ball...")
                            time.sleep(1)
                            await msg8ball.edit(content=f"8ball is now answering to question *{user_msg.replace(config[f'prefix_{whichone}'] + '8ball ', '')}*\nAnswer: 8ball is giving answer...")
                            time.sleep(3)
                            await msg8ball.edit(content=f"8ball is now answering to question *{user_msg.replace(config[f'prefix_{whichone}'] + '8ball ', '')}*\nAnswer: **{responses[random.randint(0, len(responses))]}**")
                        except:
                            await message.channel.send("On what should I decide?")

                #if(user_msg.startswith(config[f'prefix_{whichone}'])):
                #    await message.delete()
            elif(whichone == "manager"):
                if(message.author.id in config["gbans"]):
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "help")):
                        await helpman.Cmd(message, whichone)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "activity")):
                        await actiman.Cmd(message, client)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "gban")):
                        await gban.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "gunban")):
                        await gunban.Cmd(message)
                    if(user_msg.startswith(config[f'prefix_{whichone}'] + "devtoolkit")):
                        await dtkman.Cmd(message)
                #print(f"bot is {whichone}")
    except Exception as ex:
        await message.channel.send(":warning: KERNEL ERROR! :warning:\nLogging off & saving to database...")
        await utils.save_error(f"Kernel ({client.user})", os.path.basename(__file__), ex)
        exit(ex)

@client.event
async def on_button_click(interaction):
    #try:
        user = interaction.author
        guild = interaction.guild
        for x in range(1, 5):
            if(str(x) in interaction.component.custom_id):
                after_invoke_cmd.Count_Votes(interaction, x)
                await interaction.respond(content="Counted your vote (If you already counted, we won't count it)")

        if("Error Check" in interaction.component.label):
            await interaction.respond(content="Here you go!", embed=await errorcheck.ReturnCmd(user.id))
        if("Nuke" in interaction.component.label):
            await nuke.Cmd(user.id, guild)
        if("Stats" in interaction.component.label):
            await interaction.respond(content="Here you go!", embed=await stats.ReturnCmd(user.id))

        if("CLAIM 🍟" in interaction.component.label):
            with open("who_got_1k.txt", "r") as wgk:
                array = []
                array = wgk.readlines()
                if(not(str(interaction.author.id) + "\n" in array)):
                    try:
                        for filefetch in glob.glob("ecojson/*.json"):
                            await economy.Give_Not_Add_Money(str(filefetch).replace("ecojson\\", "").replace(".json", ""), user.id, 1000)
                        chanid = client.get_channel(927859819665297439)
                        await chanid.send(f"{user.name} claimed his 1,000 :fries: (and got exclusive badge)")
                        BadgesManager.Add_Badge(5, user.id)
                        await interaction.respond(content="Got it! You should see yourself claiming on logs.")
                        with open("who_got_1k.txt", "a") as gnd:
                            gnd.write(str(user.id) + "\n")
                    except:
                        await interaction.respond(content="Sorry, try again, use won't be took")
                else:
                    await interaction.respond(content="Bruh, you already claimed it!")

        lele = interaction.component.label.replace("🔑", "")
        if(lele in serialkey.SysKeys):
            embedVar = discord.Embed(title=f"Keys for {lele}", description="for Pansage Bot.", color=0x00ffff)
            for e in keys["Win"]:
                if(e["System"].startswith(lele)):
                    embedVar.add_field(name=e["System"], value=e["SysKey"], inline=False)
            await interaction.respond(content="Here you go!", embed=embedVar)
    #except Exception as exc:
    #    await utils.save_error(f"Btn Selection / Kernel ({client.user})", os.path.basename(__file__), exc)
    #    await interaction.respond(content="Error. I saved error in my error database, my creator will check out.")

#async def Kill_Kernel(tok):
#    try:
#        if(toktocheck == tok):
#            await client.logout()
#    except Exception as exc:
#        await utils.save_error(f"Kill / Kernel ({client.user})", os.path.basename(__file__), exc)
#        await message.channel.send("Error. I saved error in my error database, my creator will check out.")

async def Open_Bot_Kernel(token):
    try:
        global toktocheck
        print("Logging bot")
        toktocheck = token
        await client.start(token)
    except Exception as exc:
        await utils.save_error(f"Running / Kernel ({client.user})", os.path.basename(__file__), exc)
        #await message.channel.send("Error. I saved error in my error database, my creator will check out.")
