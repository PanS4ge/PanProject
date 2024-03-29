#{}guildinfo - Get guild data
import json
import os

import utils

import discord

def Get_Server_Net_Worth(guild):
    with open(f"ecojson/{guild.id}.json") as jsonFile:
        data = json.load(jsonFile)
        allnom = 0
        for value in data.values():
            allnom = allnom + int(value)
    return allnom

def Get_Server_Messages(guild):
    with open(f"msgcount/{guild.id}.json") as jsonFile:
        data = json.load(jsonFile)
        allnom = 0
        for value in data.values():
            allnom = allnom + int(value)
    return allnom

async def Cmd(language, serverlang, message, client):
    try:
        embedVar = discord.Embed(title="Guild-Info", description=f"{language[serverlang[str(message.guild.id)]]['global']['for']} {language[serverlang[str(message.guild.id)]]['global']['bot_project_name']}", color=0x00ff00)
        text_channels = len(message.guild.text_channels)
        voice_channels = len(message.guild.voice_channels)
        categories = len(message.guild.categories)
        channels = text_channels + voice_channels
        embedVar.set_thumbnail(url=str(message.guild.icon_url))
        badge = {}
        with open(f"partnered_server_id.json", "r") as cny:
            badge = json.loads(cny.read())
            cny.close()
        partnered = " "
        if(message.guild.id in badge['badges']):
            partnered = "<:server_partner:928283450723672085>"
        embedVar.add_field(name=f"Information About {partnered} **{message.guild.name}**: ",
                        value=f":white_small_square: ID: **{message.guild.id}** \n:white_small_square: Owner: **<@!{message.guild.owner_id}>** \n:white_small_square: Location: **{message.guild.region}** \n:white_small_square: Creation: **{message.guild.created_at}** \n:white_small_square: Members: **{'{:,}'.format(message.guild.member_count)}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(message.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in message.guild.features)} \n:white_small_square: Splash: {message.guild.splash}\n**Bot Data:**\n:white_small_square: Net Worth (Economy): **{str('{:,}'.format(Get_Server_Net_Worth(message.guild)))}**:fries:\n:white_small_square: Message Count: **{str('{:,}'.format(Get_Server_Messages(message.guild)))}**")
        await message.channel.send(embed=embedVar)
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")