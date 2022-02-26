#{}mc_pfp (username) (background_number (0 for none)) (optional arg: starburst) - Generates you minecraft profile picture
from json import JSONDecodeError

import discord
import os
import requests
from PIL import Image
from io import BytesIO

import utils

def Get_Users_UUID(name):
    username = name
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
    response = requests.get(url)
    uuid = response.json()['id']
    return uuid

def Grab_Skin_File(name):
    uuid = Get_Users_UUID(name)
    response = requests.get(f"https://crafatar.com/skins/{uuid}.png")
    img = Image.open(BytesIO(response.content))
    img.save("Downloaded_Skin.png")
    return img

async def Cmd(language, serverlang, message, client):
    try:
        try:
            name = str(message.content).split(" ")[1]
            bg = str(message.content).split(" ")[2]
            starburst = "starburst" in str(message.content)
        except:
            await message.channel.send("Invalid args")
            return
        await message.channel.send("Please at least mention me :(")
        msgav = await message.channel.send("Generating...")
        skin = Grab_Skin_File(name)
        templ = Image.open("cmds/fun/image_data/Template.png")
        head = skin.crop((8, 9, 15, 16))
        templ.paste(head, (8, 4))
        headb = skin.crop((5, 9, 9, 16))
        templ.paste(headb, (5, 4))
        neck = skin.crop((20, 20, 28, 22))
        templ.paste(neck, (6, 11))
        templ.putpixel((6, 11), (255, 255, 255, 0))
        templ.putpixel((13, 11), (255, 255, 255, 0))
        body = skin.crop((22, 21, 26, 28))
        templ.paste(body, (8, 13))
        lh = skin.crop((44, 20, 47, 32))
        templ.paste(lh, (5, 13))
        rh = skin.crop((36, 52, 39, 64))
        templ.paste(rh, (12, 13))
        layer = skin.crop((37, 8, 48, 16))
        templ.convert("RGBA")
        layer.convert("RGBA")
        templ.paste(layer, (5, 3), layer)
        await msgav.edit(content="Generated, resizing and applying settings...")
        img = templ.resize((1000, 1000), Image.NEAREST)
        bge = Image.open(f"cmds/fun/image_data/empty.png")
        if(bg == 0):
            bag = Image.open(f"cmds/fun/image_data/empty.png")
            prop = bag.crop((0, 0, 1001, 1001))
            bge.paste(prop, (0, 0))
        if(bg != 0):
            try:
                bag = Image.open(f"cmds/fun/image_data/bg/{bg}.png")
                prop = bag.crop((0, 0, 1001, 1001))
                bge.paste(prop, (0, 0))
            except:
                await message.channel.send("Invalid background - all backgrounds are on my support server!")
        if(starburst):
            sb = Image.open("cmds/fun/image_data/starburst.png")
            sba = sb.crop((0, 0, 1001, 1001))
            bge.paste(sba, (0, 0), sba)
        sba = img.crop((0, 0, 1001, 1001))
        bge.paste(sba, (0, 0), sba)
        bge.save(f"all_profiles/{name}_{bg}_{starburst}.png")
        with BytesIO() as image_binary:
            bge.save(image_binary, 'PNG')
            image_binary.seek(0)
            await msgav.edit(content="Your avatar is below!")
            await message.channel.send(file=discord.File(fp=image_binary, filename='image.png'))
    except JSONDecodeError:
        await message.channel.send("Invalid nickname - Are you sure this is *Minecraft: Java Edition* username?")
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")