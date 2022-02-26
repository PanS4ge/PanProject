#{}memberinfo - Get member data
import datetime
import json
import os
import glob

from cmds.economy import eco as eco

import BadgesManager
import utils

import discord

language = {}
with open(f"language_files/english.json", encoding='utf8') as data:
    language = json.load(data)

serverlang = {}
with open(f"language_server.json", encoding='utf8') as data:
    serverlang = json.load(data)

def Get_Global_MsgCnt(member):
    yesyes = 0
    for filefetch in glob.glob("msgcount/*.json"):
        try:
            ffet = {}
            with open(filefetch, "r") as ete:
                ffet = json.loads(ete.read())
                yesyes = yesyes + int(ffet[str(member.id)])
        except:
            pass
    return yesyes

def Get_Msg(member):
    with open(f"msgcount/{str(member.guild.id)}.json", "r") as cny:
        cnt = json.loads(cny.read())
        return cnt[str(member.id)]

async def Cmd(language, serverlang, message, client):
    try:
        #member = discord.Member
        #try:
        #    try:
        #        member = message.guild.get_member(int(message.content.split(" ")[1].replace("<@!", "").replace(">", "")))
        #    except:
        #        member = message.guild.get_member(int(message.content.split(" ")[1]))
        #except:
            #member = message.author
        member = message.author
        globworth = await eco.Get_Global_Balance(message)
        embedVar = discord.Embed(title=language[serverlang[str(message.guild.id)]]['member_info']['memberinfo'], description=f"{language[serverlang[str(message.guild.id)]]['global']['for']} {language[serverlang[str(message.guild.id)]]['global']['bot_project_name']}", color=0x00ff00)
        embedVar.set_thumbnail(url=str(member.avatar_url))
        x = ""
        for ewx in BadgesManager.Fetch_Badges(member.id):
            x = x + ewx
        if(x == ""):
            x = "None :(\nEarn your first joining on my support server!"
        embedVar.add_field(name=language[serverlang[str(message.guild.id)]]['member_info']['title'].replace("{message.author.name}", str(member.name)),
                        value=language[serverlang[str(message.guild.id)]]['member_info']['value'].replace("{message.author.id}", str(member.id)).replace("{message.author.top_role.id}", str(member.top_role.id)).replace("{message.author.joined_at}", str(member.joined_at.strftime("%m/%d/%Y, %H:%M:%S"))).replace("{message.author.created_at}", member.created_at.strftime("%m/%d/%Y, %H:%M:%S")).replace("{str('{:,}'.format(globworth))}", str('{:,}'.format(globworth))).replace("{str('{:,}'.format(eco.Get_Bank(message.author.id, message.guild.id)))}", str('{:,}'.format(eco.Get_Bank(message.author.id, message.guild.id)))).replace("{str(temp)}", str(x)).replace("{str('{:,}'.format(Get_Global_MsgCnt(message)))}", str('{:,}'.format(Get_Global_MsgCnt(member)))).replace("{str('{:,}'.format(Get_Msg(message)))}", str('{:,}'.format(Get_Msg(member)))).replace("{BADGES}",x))
        await message.channel.send(embed=embedVar)
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send(language[serverlang[str(message.guild.id)]]['global']['error_save'])