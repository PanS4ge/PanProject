#{}to_fix - sends message from #fix_tracker
import discord

async def Cmd(language, serverlang, message, client):
    tofixmsg = await client.get_channel(928629647250423818).fetch_message(928629856332283915)
    await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["tofix"].replace("{tofixmsg.content}", tofixmsg.content).replace("{tofixmsg.author}", tofixmsg.author.name))