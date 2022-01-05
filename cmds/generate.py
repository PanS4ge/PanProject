#{}generate ({}gen) win95 - Generates Valid Windows 95 Key||{}generate ({}gen) oem - Generates Valid OEM Key
import random
import time
import os

import discord

def RulesWin95(_1stseg_, _2ndseg_):
    if(len(_1stseg_) != 3):
        return False
    if(len(_2ndseg_) != 7):
        return False

    _1stseg_nospaces_ = str(_1stseg_[0]) + str(_1stseg_[1]) + str(_1stseg_[2])
    for x in range(10):
        if(x == 1 or x == 2):
            pass
        elif(str(x-1)*3 == _1stseg_nospaces_):
            return False
    if(_1stseg_[2] == 0 or _1stseg_[2] == 8 or _1stseg_[2] == 9):
        return False
    temp = 0
    for x in _2ndseg_:
        temp = temp + x
    if(temp % 7):
        return True
    else:
        return False

def RulesOEM(_1stseg_, _2ndseg_, _3rdseg_):
    if(len(_1stseg_) != 5):
        return False
    if(len(_2ndseg_) != 7):
        return False
    if(len(_3rdseg_) != 5):
        return False

    global temp
    temp = str(_1stseg_[0]) + str(_1stseg_[1]) + str(_1stseg_[2])
    if (not(1 < int(temp) and int(temp) < 366)):
        return False

    temp = ""
    temp = str(_1stseg_[3]) + str(_1stseg_[4])

    allowed = []
    for x in range(95, 99):
        allowed.append(x)
    allowed.append(1)
    allowed.append(2)
    allowed.append(3)

    if(not(int(temp) in allowed)):
        return False

    if(_2ndseg_[0] != 0):
        return False

    temp = 0
    for x in _2ndseg_:
        temp = temp + x
    if(temp % 7):
        return True

def GenerateWin95Key():
    _1stseggen_ = []
    _2ndseggen_ = []
    for x in range(3):
        _1stseggen_.append(random.randint(0, 9))
    for x in range(7):
        _2ndseggen_.append(random.randint(0, 9))
    if(RulesWin95(_1stseggen_, _2ndseggen_)):
        temp = ""
        for x in _1stseggen_:
            temp = temp + str(x)
        temp2 = ""
        for x in _2ndseggen_:
            temp2 = temp2 + str(x)
        return temp + "-" + temp2
    else:
        return None

def GenerateOEM():
    _1stseggen_ = []
    _2ndseggen_ = []
    _3rdseggen_ = []
    for x in range(5):
        _1stseggen_.append(random.randint(0, 9))
    for x in range(7):
        _2ndseggen_.append(random.randint(0, 9))
    for x in range(5):
        _3rdseggen_.append(random.randint(0, 9))

    if(RulesOEM(_1stseggen_, _2ndseggen_, _3rdseggen_)):
        temp = ""
        for x in _1stseggen_:
            temp = temp + str(x)
        temp2 = ""
        for x in _2ndseggen_:
            temp2 = temp2 + str(x)
        temp3 = ""
        for x in _3rdseggen_:
            temp3 = temp3 + str(x)
        yessir = str(temp) + "-OEM-" + str(temp2) + "-" + str(temp3)
        return yessir
    else:
        return None

async def Cmd(message, user_msg):
    try:
        if ("win95" in user_msg):
            try:
                allp = GenerateWin95Key()
                if(allp == None):
                    await Cmd(message, user_msg)
                else:
                    await message.channel.send("Your Windows 95 Key is *" + str(allp) + "*")
            except RecursionError:
                await message.channel.send("Sorry, try again later")
        elif ("oem" in user_msg):
            try:
                allp = GenerateOEM()
                if (allp == None):
                    await Cmd(message, user_msg)
                else:
                    await message.channel.send("Your OEM Key is *" + str(allp) + "*")
            except RecursionError:
                await message.channel.send("Sorry, try again later")
        else:
            with open("cmds//generate.py") as f:
                t = f.readline().replace("#", "")
                t = t.replace("{}", config['prefix'])
                t = t.replace("{HASH}", "#")
                await message.channel.send("Usage\n" + t)
            await message.channel.send("Usage:\n" + t)
    except Exception as e:
        await utils.save_error(user_msg, os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")