from json import JSONDecodeError

import discord
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

import utils

def Grab_Skin_File(member):
    response = requests.get(member.displayAvatarURL)
    img = Image.open(BytesIO(response.content))
    #img.save("Downloaded_avatar.png")
    return img

def get_welcome(member : discord.member):
    try:
        templ = "avavav.png"
        av = Grab_Skin_File(member)
        grad = "GradientAV.png"
        av = av.resize((256, 256), Image.NEAREST)
        grab = av.crop(0, 0, 257, 257)
        templ.paste(grab, (0, 0))
        grab = grad.crop(0, 0, 513, 257)
        templ.paste(grab, (0, 0))
        draw = ImageDraw.Draw(templ)
        font = ImageFont.truetype("sans-serif.ttf", 28)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((500, 50), f"{member.name}#{str(member.discriminator)}", fill="black", anchor="rm", font=font)
        font = ImageFont.truetype("sans-serif.ttf", 16)
        draw.multiline_text((500, 100), f"Welcome on server {member.guild}!\nFeel free to chat with others!", font=font)
        return templ
    except Exception as e:
        utils.noas_save_error("Welcome pic generator", os.path.basename(__file__), e)

def get_leave(member : discord.member):
    try:
        templ = "avavav.png"
        av = Grab_Skin_File(member)
        grad = "GradientAV.png"
        av = av.resize((256, 256), Image.NEAREST)
        grab = av.crop(0, 0, 257, 257)
        templ.paste(grab, (0, 0))
        grab = grad.crop(0, 0, 513, 257)
        templ.paste(grab, (0, 0))
        draw = ImageDraw.Draw(templ)
        font = ImageFont.truetype("sans-serif.ttf", 28)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((500, 50), f"{member.name}#{str(member.discriminator)}", fill="black", anchor="rm", font=font)
        font = ImageFont.truetype("sans-serif.ttf", 16)
        draw.multiline_text((500, 100), f"He left our server :(\nHow sad :(", font=font)
        return templ
    except Exception as e:
        utils.noas_save_error("Leave pic generator", os.path.basename(__file__), e)

