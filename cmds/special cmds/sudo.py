#{}sudo (ACTIVATED) - Ignore perm check for sc (Only sc)
import os
import utils


async def Cmd(language, serverlang, message, client):
    try:
        if(utils.has_sc_perms(message.author.id)):
            try:
                with open("insudomode", "w") as ism:
                    ism.write(message.content.split(" ")[1])
                await message.channel.send(f"Sudo mode: {message.content.split(' ')[1]}")
            except Exception as exhugdsbopaz:
                await message.channel.send(f"Error occured\n{exhugdsbopaz}")
        else:
            await message.channel.send("You cannot activate superuser")
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")