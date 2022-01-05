import json

def Create_Badge(emoji, name, desc, owners):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    addthis = {"id": len(badge['badge']), "emoji": emoji, "name": name, "description": desc, "owners": owners}
    badge['badge'].append(addthis)
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

def Add_Badge(ide, towho):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    badge['badge'][ide]['owners'].append(towho)
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

def Remove_Badge(ide, towho):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    badge['badge'][ide]['owners'].remove(towho)
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()

def Have_Badge(ide, towho):
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

def Clear_Badges(ide):
    badge = {}
    with open(f"badges.json", "r") as cny:
        badge = json.loads(cny.read())
        cny.close()
    badge['badge'][ide]['owners'] = []
    with open(f"badges.json", "w") as cny:
        cny.write(json.dumps(badge))
        cny.close()