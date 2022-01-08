#{}clear_links_db - Clears link database from links that are in 90% similar (only owner)
import discord
import utils
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

async def Cmd(message):
    if(not(utils.is_owner_of_bot(message.author.id))):
        return await message.channel.send("I refuse.")
    linbefore = []
    links = []
    errors = 0
    cntlinks = 0
    with open("link.txt", "r") as re:
        for x in re.readline():
            links.append(x)
            linbefore.append(x)
        cntlinks = len(links)
    msgcl = await message.channel.send("Clearing... 0/5 rounds")
    for rnd in range(5):
        await msgcl.edit(content=f"Clearing... {rnd}/5 rounds - Link count {cntlinks} -> {len(links)}")
        for x in range(len(links)):
            try:
                if(similar(links[x-1], links[x]) >= 0.9):
                    links.pop(x)
            except:
                errors = errors + 1
    await msgcl.edit(content=f"Cleared {cntlinks - len(links)} similar links.\nCurrent count -> {len(links)}\nCreating backup & saving new link db...")
    with open("link.txt", "a") as linkk:
        for x in links:
            linkk.write(x)
    with open("linksbefore.txt", "a") as linkk:
        for x in linbefore:
            linkk.write(x)
    await msgcl.edit(content=f"Work is done")
