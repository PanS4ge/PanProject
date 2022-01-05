#{}memberinfo - Get member data
import datetime
import json
import os
import glob

from cmds import economy as eco

import BadgesManager
import utils

import discord

def Get_Global_MsgCnt(message):
    yesyes = 0
    for filefetch in glob.glob("msgcount/*.json"):
        try:
            ffet = {}
            with open(filefetch, "r") as ete:
                ffet = json.loads(ete.read())
                yesyes = yesyes + int(ffet[str(message.author.id)])
        except:
            pass
    return yesyes

def Get_Msg(message):
    with open(f"msgcount/{str(message.guild.id)}.json", "r") as cny:
        cnt = json.loads(cny.read())
        return cnt[str(message.author.id)]

async def Cmd(message):
    #try:
        temp = ""
        globworth = await eco.Get_Global_Balance(message)
        for x in BadgesManager.Fetch_Badges(message.author.id):
            temp = temp + x + " "
        embedVar = discord.Embed(title="Member-Info", description=f"For Pan-Project bot.", color=0x00ff00)
        embedVar.set_thumbnail(url=str(message.author.avatar_url))
        embedVar.add_field(name=f"Information About **{message.author.name}**: ",
                        value=f":white_small_square: ID: **{message.author.id}** \n:white_small_square: Highest role: <@&{message.author.top_role.id}>\n:white_small_square: Joined at: **{message.author.joined_at}** \n:white_small_square: Creation: **{message.author.created_at}**\n**Bot Data:**\n:white_small_square: Net Worth (Global): **{str('{:,}'.format(globworth))}**:fries:\n:white_small_square: Net Worth (Server): **{str('{:,}'.format(eco.Get_Bank(message.author.id, message.guild.id)))}**:fries:\n:white_small_square: Message Count (Global): **{str('{:,}'.format(Get_Global_MsgCnt(message)))}**\n:white_small_square: Message Count (Server): **{str('{:,}'.format(Get_Msg(message)))}**\n:white_small_square: Badges `?legend`: \n**{str(temp)}**")
        await message.channel.send(embed=embedVar)
    #except Exception as e:
    #    await utils.save_error(str(message.content), os.path.basename(__file__), e)
    #    await message.channel.send("Error. I saved error in my error database, my creator will check out.")