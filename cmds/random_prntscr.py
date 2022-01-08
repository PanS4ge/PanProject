#{}random_prntsc - Sorry bro, god bless your eyes
import os
import discord
import time

import requests
import configparser
import string
from bs4 import BeautifulSoup
from functools import reduce

from discord.utils import get

import random

import utils

headers = {
    "ACCEPT" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "ACCEPT-LANGUAGE": "en-US,en;q=0.9",
    "DEVICE-MEMORY": "8",
    "DOWNLINK": "10",
    "DPR": "1",
    "ECT": "4g",
    "HOST": "prnt.sc",
    "REFERER": "https://www.google.com/",
    "RTT": "50",
    "SEC-FETCH-DEST": "document",
    "SEC-FETCH-MODE": "navigate",
    "SEC-FETCH-SITE": "cross-site",
    "SEC-FETCH-USER": "?1",
    "UPGRADE-INSECURE-REQUESTS": "1",
    "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "VIEWPORT-WIDTH": "1920",
}

def get_image_and_save(website_url, image_url):
    try:
        html_content = requests.get(website_url + image_url, headers=headers).content
        soup = BeautifulSoup(html_content, "lxml")
        ourimageurl = soup.find(id='screenshot-image')['src']
        image = requests.get(ourimageurl).content
        return image
    except:
        return "Image was prob removed, good 4 u!"
        #print (image_url + " was removed probably.")

async def Cmd(message):
    try:
        await message.channel.send("Sorry, bro. God bless your eyes! Hope it isn't that bad!")
        randomurl = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))
        if(get_image_and_save("prnt.sc/", randomurl) == "Image was prob removed, good 4 u!"):
            await message.channel.send(get_image_and_save("prnt.sc/", randomurl) + "\nI tried to give you " + randomurl)
        else:
            file = get_image_and_save("prnt.sc/", randomurl)
            await message.channel.send(file=file)
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")
