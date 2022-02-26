import json
import discord

async def Send_Message(towho, msgcon, client):
    sent = False
    for guil in client.guilds:
        for mem in guil.members:
            if(mem.id == towho and sent == False):
                await mem.send(msgcon)
                sent = True

async def Create_Badge(emoji, name, desc, owners, client):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    addthis = {"id": len(badge['badge']), "emoji": emoji, "name": name, "description": desc, "owners": owners}
    for memid_add in owners:
        try:
            await Send_Message(memid_add, f"**Congratulations!**\nYou were given new badge!\n{badge['badge'][len(badge['badge'])]['emoji']} {badge['badge'][len(badge['badge'])]['name']}\nYou can see your badge on `?memberinfo`", client)
        except:
            pass
    badge['badge'].append(addthis)
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge, indent=4))
        cny.close()

async def Add_Badge(ide, towho, client):
    if (towho == "*"):
        return "forbidden"
    else:
        badge = {}
        with open(f"badges.json", "r") as cny:
            badge = json.loads(cny.read())
            cny.close()
        badge['badge'][ide]['owners'].append(towho)
        if not(Have_Badge(ide, towho)):
            try:
                await Send_Message(towho, f"**Congratulations!**\nYou were given new badge!\n{badge['badge'][ide]['emoji']} {badge['badge'][ide]['name']}\nYou can see your badge on `?memberinfo`", client)
            except:
                pass
        with open(f"badges.json", "w") as cny:
            cny.write(json.dumps(badge))
            cny.close()

async def Remove_Badge(ide, towho, client):
    if(towho == "*"):
        Clear_Badges(ide, client)
    else:
        badge = {}
        with open(f"badges.json", "r") as cny:
            badge = json.loads(cny.read())
            cny.close()
        badge['badge'][ide]['owners'].remove(towho)
        try:
            await Send_Message(towho, f"You lost badge! :(\n{badge['badge'][ide]['emoji']} {badge['badge'][ide]['name']}",
                               client)
        except:
            pass
        with open(f"badges.json", "w") as cny:
            cny.write(json.dumps(badge))
            cny.close()

def Have_Badge(ide, towho):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    return towho in badge['badge'][ide]['owners']

def Fetch_Badges(towho):
    badge = {}
    allbadges = []
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    for x in badge['badge']:
        if(towho in x['owners']):
            allbadges.append(x['emoji'])
    return allbadges

async def Clear_Badges(ide, client):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    for towho in badge['badge'][ide]['owners']:
        try:
            await Send_Message(towho, f"You lost badge due to purge! :(\n{badge['badge'][ide]['emoji']} {badge['badge'][ide]['name']}", client)
        except:
            pass
    badge['badge'][ide]['owners'] = []
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()