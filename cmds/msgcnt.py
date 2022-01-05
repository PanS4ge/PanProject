#{}msgcnt - Check your message count!
import json
import discord

async def Cmd(message):
    with open(f"msgcount/{str(message.guild.id)}.json", "r") as cny:
        cnt = json.loads(cny.read())
        try:
            if (cnt[str(message.author.id)] != 0):
                cnt[str(message.author.id)] = int(cnt[str(message.author.id)]) + 1
                await message.channel.send(f"Your message count is {cnt[str(message.author.id)]}")
        except:
            await message.channel.send(f"Can't check your progress, at least this message will let me! Try again :D")