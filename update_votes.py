import glob
import json
import time

import discord
import requests

async def Update(client : discord.Client):
    tggtoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjkxNTY1NzA5Mzg2MjgxNzgwMiIsImJvdCI6dHJ1ZSwiaWF0IjoxNjQzNjI0NzgwfQ.lpElqa679qqRQaRccFKDL0TsHaKxF8PBcJEXDWUIiG8"

    blgb = "ERROR"
    tggt = "ERROR"

    #try:
    #    bladelist = dbots.BladeList(token=bltoken)
    #    blgb = await bladelist.get_bot(bot_id="915657093862817802")
    #except Exception as xex:
    #    blgb = xex
    #try:

    if(3>2):
        headers = {
            "ADMIN_KEY": "pansageyt",
            "Content-Type": "application/json"
        }
        #if(psbapi['GuildCount'] != client.get_guild(925744274706939956).member_count):
        if(3>2):
            jsone = json.loads('{"PansageBot": {}}')
            jsone['PansageBot']['GuildCount'] = len(client.guilds)
            temp = 0
            for yeye in client.guilds:
                for xexe in yeye.members:
                    temp = temp + 1
            jsone['PansageBot']['GlobalMemberCount'] = temp
            jsone['PansageBot']['SupportServerMemberCount'] = client.get_guild(925744274706939956).member_count
            jsone['PansageBot']['Partnerships'] = []
            with open("partnered_server_id.json", "r") as psid:
                jsonn = json.loads(psid.read())
                for x in jsonn['badges']:
                        #gui = client.get_guild(x)
                        #print("Clearing " + gui.name)
                        #invites = await gui.invites()
                        #print(f"He has {invites}")
                        #for y in invites:
                        #    if(y.inviter == client.user):
                        #        try:
                        #            print(f"Removed invite - Guild: {gui.name}, Code: {y.code}")
                        #            await y.delete()
                        #        except:
                        #            print("Unable to remove")
                    try:
                        invite = await client.get_guild(x).text_channels[0].create_invite(unique=False)
                        jsone['PansageBot']['Partnerships'].append({"id": x, "name": client.get_guild(x).name, "membercount": client.get_guild(x).member_count, "invite": invite.url, "avatar": str(client.get_guild(x).icon_url)})
                    except:
                        pass
            jsone['PansageBot']['Cmds'] = []
            for folder in glob.glob("C:/Users/User/PycharmProjects/discord.py/cmds/*/", recursive=True):
                jenn = {"group": folder.replace('C:/Users/User/PycharmProjects/discord.py/cmds', '').replace('\\', ''), "cmds": []}
                for file in glob.glob(folder + "/*.py"):
                    with open(file, "r", encoding="utf8") as f:
                                #print(file)
                                useprefix = "?"
                                t = f.readline().replace("#", "")
                                t = t.replace("{}", useprefix)
                                t = t.replace("{HASH}", "#")
                                try:
                                    if ("||" in t):
                                        for c in t.split("||"):
                                            jenn['cmds'].append({"name": c.split("-")[0], "desc": c.split("-")[1]})
                                            #embedVar.add_field(name=c.split("-")[0], value=c.split("-")[1], inline=True)
                                            #count = count + 1
                                    else:
                                        jenn['cmds'].append({"name": t.split("-")[0], "desc": t.split("-")[1]})
                                        #embedVar.add_field(name=t.split("-")[0], value=t.split("-")[1], inline=True)
                                        #count = count + 1
                                except:
                                    pass
                for folder3 in glob.glob(folder + "/*/"):
                    folder2 = folder3.replace("C:/Users/User/PycharmProjects/discord.py/cmds", "").replace("\\", "")
                    if(glob.glob(folder2 + "/*.py")):
                        for file in glob.glob(folder2 + "/*.py"):
                            #print(file)
                            with open(file, "r", encoding="utf8") as f:
                                useprefix = "?"
                                t = f.readline().replace("#", "")
                                t = t.replace("{}", useprefix)
                                t = t.replace("{HASH}", "#")
                                if ("||" in t):
                                    for c in t.split("||"):
                                        jenn['cmds'].append({"name": c.split("-")[0], "desc": c.split("-")[1]})
                                        # embedVar.add_field(name=c.split("-")[0], value=c.split("-")[1], inline=True)
                                        # count = count + 1
                                else:
                                    jenn['cmds'].append({"name": t.split("-")[0], "desc": t.split("-")[1]})
                                    # embedVar.add_field(name=t.split("-")[0], value=t.split("-")[1], inline=True)
                                    # count = count + 1
                    else:
                         for file in glob.glob(folder2 + "/*/"):
                             for file2 in glob.glob(file + "/*.py"):
                                 with open(file2, "r", encoding="utf8") as f:
                                     useprefix = "?"
                                     t = f.readline().replace("#", "")
                                     t = t.replace("{}", useprefix)
                                     t = t.replace("{HASH}", "#")
                                     t = t.replace("\n", "")
                                     if ("||" in t):
                                         for c in t.split("||"):
                                             jenn['cmds'].append({"name": c.split("-")[0], "desc": c.split("-")[1]})
                                             # embedVar.add_field(name=c.split("-")[0], value=c.split("-")[1], inline=True)
                                             # count = count + 1
                                     else:
                                         jenn['cmds'].append({"name": t.split("-")[0], "desc": t.split("-")[1]})
                                         # embedVar.add_field(name=t.split("-")[0], value=t.split("-")[1], inline=True)
                                         # count = count + 1
                jsone['PansageBot']['Cmds'].append(jenn)
            headerstgg = {
                "Authorization": tggtoken
            }
            req = requests.request("GET", "https://top.gg/api/bots/915657093862817802", headers=headerstgg)
            tggt = json.loads(req.text)
            jsone['PansageBot']['top.gg'] = {}
            jsone['PansageBot']['top.gg']['AllVotes'] = tggt['points']
            jsone['PansageBot']['top.gg']['MonthlyVotes'] = tggt['monthlyPoints']
            req = requests.request("GET", "https://top.gg/api/bots/915657093862817802/votes", headers=headerstgg)
            tggt = json.loads(req.text)
            jsone['PansageBot']['top.gg']['LastToVote'] = tggt[-1]['username']
            with open("cooldown.json", "r") as cd:
                jsone['PansageBot']['Cooldowns'] = json.loads(cd.read())
            #print(json.dumps(str(jsone), indent=4))
            req = requests.request("GET", "http://psbapi.herokuapp.com/botdata/get", headers=headers)
            psbapi = json.loads(req.text)
            #print(str(jsone))
            #time.sleep(5)
            if(psbapi != jsone):
                req = requests.post("http://psbapi.herokuapp.com/botdata/post", headers=headers, json=json.dumps(jsone))
                #print(req.text)
    #except Exception as exxexexe:
    #    print("Error updating Pansage Bot API\nException: " + str(exxexexe))

    try:
        headers = {
            "Authorization": tggtoken
        }
        req = requests.request("GET", "https://top.gg/api/bots/915657093862817802", headers=headers)
        tggt = json.loads(req.text)
        day = client.get_channel(936620742156623932)
        if(day.name != f"All: {str(tggt['points'])}"):
            await day.edit(name=f"All: {str(tggt['points'])}")
        month = client.get_channel(937655729739939870)
        if (month.name != f"Monthly: {str(tggt['monthlyPoints'])}"):
            await month.edit(name=f"Monthly: {str(tggt['monthlyPoints'])}")

        req = requests.request("GET", "https://top.gg/api/bots/915657093862817802/votes", headers=headers)
        tggt = json.loads(req.text)
        last = client.get_channel(937656006190714881)
        try:
            if (last.name != f"Last: {str(tggt[-1]['username'])}"):
                await last.edit(name=f"Last: {str(tggt[-1]['username'])}")
        except KeyError:
            await last.edit(name=f"Last: None today :(")
    except Exception as xex:
        chan = client.get_channel(937665605362925669)
        await chan.send("<:nope:928675155440443503> Unable to change top.gg stats\nException" + str(xex))
    #try:
    #    tggt = dbots.TopGG(token=tggtoken)
    #    tggtv = await tggt.get_bot_votes(bot_id="915657093862817802")
    #    tggts = await tggt.get_bot_stats(bot_id="915657093862817802")
    #except Exception as xex:
    #    tggtv = xex
    #    tggts = xex

    #try:
    #    print(blgb.text)
    #except:
    #    print(blgb)

    #try:
    #    print(tggt.text)
    #except:
    #    print(tggt)



