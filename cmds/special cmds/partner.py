#{}partner (add/rem) (guild id) - Adds/Removes partnership to server
import discord
import requests
import json

import BadgesManager
import utils


async def Cmd(language, serverlang, message, client):
    try:
        if(utils.has_sc_perms(message.author.id)):
            if(message.content.split(" ")[1] == "rem"):
                badge = {}
                with open(f"partnered_server_id.json", "r") as cny:
                    badge = json.loads(cny.read())
                    cny.close()
                badge['badges'].remove(message.content.split(" ")[2])
                try:
                    await client.get_channel(936200778102743081).send(
                    f"<:server_partner:928283450723672085> PARTNER ALERT!\nOur lost partner: {client.get_guild(message.content.split(' ')[2]).name}")
                except:
                    await message.channel.send("We lost a partner, but I can't get name.")
                with open(f"partnered_server_id.json", "w") as cny:
                    cny.write(json.dumps(badge, indent=4))
                    cny.close()
            elif(message.content.split(" ")[1] == "add"):
                badge = {}
                with open(f"partnered_server_id.json", "r") as cny:
                    badge = json.loads(cny.read())
                    cny.close()
                badge['badges'].append(message.content.split(" ")[2])
                linkinv = await client.get_guild(message.content.split(" ")[2]).text_channels[0].create_invite()
                await client.get_channel(936200778102743081).send(
                    f"<:server_partner:928283450723672085> PARTNER ALERT!\nOur new partner: {client.get_guild(message.content.split(' ')[2]).name}\nHere you can join (It's a random channel): {linkinv}")
                for member in client.get_guild(message.content.split(" ")[2]).members:
                    if (utils.has_permission(member, "ADMINISTRATOR")):
                        await BadgesManager.Add_Badge(10, member.id, client)
                with open(f"partnered_server_id.json", "w") as cny:
                    cny.write(json.dumps(badge, indent=4))
                    cny.close()
        else:
            await message.channel.send("Impossible for u!")
    except:
        await message.channel.send("Too less args")