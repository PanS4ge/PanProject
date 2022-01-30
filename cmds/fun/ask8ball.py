#{}8ball (QUESTION) - Ask 8ball about your question...
import discord

async def Cmd(language, serverlang, message, client):
    try:
        responses = language[serverlang[str(message.guild.id)]]["kernel"]["8ballresponses"]
        msg8ball = await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["1st8ball"].replace(
            "{user_msg.replace(config[f'prefix_manager'] + '8ball ', '')}",
            user_msg.replace(config[f'prefix_manager'] + '8ball ', '')))
        await asyncio.sleep(1)
        await msg8ball.edit(content=language[serverlang[str(message.guild.id)]]["kernel"]["2nd8ball"].replace(
            "{user_msg.replace(config[f'prefix_manager'] + '8ball ', '')}",
            user_msg.replace(config[f'prefix_manager'] + '8ball ', '')))
        await asyncio.sleep(3)
        await msg8ball.edit(content=language[serverlang[str(message.guild.id)]]["kernel"]["3nd8ball"].replace(
            "{user_msg.replace(config[f'prefix_manager'] + '8ball ', '')}",
            user_msg.replace(config[f'prefix_manager'] + '8ball ', '')).replace(
            "{responses[random.randint(0, len(responses))]}", responses[random.randint(0, len(responses))]))
    except:
        await message.channel.send(language[serverlang[str(message.guild.id)]]["kernel"]["invalid_ask"])