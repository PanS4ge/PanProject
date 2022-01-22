#{}exec - Run code (Only Owner)
import discord
import os
import utils


async def Cmd(message, client):
    try:
        if("await " in message.content):
            try:
                if (utils.is_owner_of_bot(message.author.id)):
                    evalDone = await exec(str(message.content).replace(str(message.content).split(" ")[0], "").replace("await ", ""))

                    embedEval = discord.Embed(title=":white_check_mark: Exec!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",
                                        value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f"{evalDone}")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for owner")
            except Exception as e:
                if (utils.is_owner_of_bot(message.author.id)):
                    embedEval = discord.Embed(title=":negative_squared_cross_mark: Exec!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",
                                        value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f":x: {e} :x:")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for owner")
        else:
            try:
                if(utils.is_owner_of_bot(message.author.id)):
                    evalDone = exec(str(message.content).replace(str(message.content).split(" ")[0], ""))

                    embedEval = discord.Embed(title=":white_check_mark: Exec!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got", value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f"{evalDone}")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for owner")
            except Exception as e:
                if (utils.is_owner_of_bot(message.author.id)):
                    embedEval = discord.Embed(title=":negative_squared_cross_mark: Exec!", color=0x2eb42b)
                    embedEval.add_field(name=":inbox_tray: Got",value=f"{str(message.content).replace(str(message.content).split(' ')[0], '')}")
                    embedEval.add_field(name=":outbox_tray: Back", value=f":x: {e} :x:")
                    await message.channel.send(embed=embedEval)
                else:
                    await message.channel.send("Only for owner")
    except:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")