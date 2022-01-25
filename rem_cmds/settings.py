#{}settings (welcome_channel/skip_scan/language) ... - Changes settings on server (options after selecting category)
import discord
import utils
import os
import json

async def Cmd(message, client : discord.Client):
    try:
            #try:
            args = message.content.split(" ")
            #except:
            #    await message.channel.send("options: welcome_channel/skip_scan/language")
            if(args[1].lower() == "welcome_channel"):
                welcomechan = {}
                with open("settings/welcome_channel.json", "r") as welcom:
                    welcomechan = json.loads(welcom.read())
                try:
                    # CHANNEL ID
                    if(args[2].lower() == "join_channel" or args[2].lower() == "leave_channel"):
                        chan = args[3].replace("<#", "").replace(">", "")
                        await message.channel.send(f"Set channel {client.get_channel(int(chan)).name} as {args[2].upper()}")
                        try:
                            welcomechan[str(message.guild.id)][args[2].lower()] = chan
                        except KeyError:
                            welcomechan[str(message.guild.id)] = {}
                            welcomechan[str(message.guild.id)][args[2].lower()] = chan

                        with open("settings/welcome_channel.json", "w") as welcom:
                            welcom.write(json.dumps(welcomechan))

                    # TRUE / FALSE
                    if(args[2].lower() == "image_welcome" or args[2].lower() == "image_leave"):
                        chan = "true" in args[3].lower()
                        await message.channel.send(f"Set {args[2].upper()} as {str(chan)}")
                        try:
                            welcomechan[str(message.guild.id)][args[2].lower()] = chan
                        except KeyError:
                            welcomechan[str(message.guild.id)] = {}
                            welcomechan[str(message.guild.id)][args[2].lower()] = chan
                        with open("settings/welcome_channel.json", "w") as welcom:
                            welcom.write(json.dumps(welcomechan, indent=4))
                except:
                    await message.channel.send("welcome_channel\nOptions:\nJoin_Channel -> expecting channel ping (when exists - overrides / to remove *REMOVE*)\nLeave_Channel -> expecting channel ping (when exists - overrides / to remove *REMOVE*)\nImage_Welcome -> expecting True/False\nImage_Leave -> expecting True/False")

                #for x in args:
                #    print(x.lower())

            if(args[1].lower() == "skip_scan"):
                    welcomechan = {}
                    with open("settings/dont_scan_links.json", "r") as welcom:
                        welcomechan = json.loads(welcom.read())
                    try:
                        if (args[2].lower() == "add"):
                            chan = args[3].replace("<#", "").replace(">", "")
                            await message.channel.send(f"Added channel {client.get_channel(int(chan)).name} to DONT_SCAN_LINKS list")
                            welcomechan.append(str(chan))
                            with open("settings/welcome_channel.json", "w") as welcom:
                                welcom.write(json.dumps(welcomechan))
                        if (args[2].lower() == "rem"):
                            chan = int(args[3].replace("<#", "").replace(">", ""))
                            await message.channel.send(f"Removed channel {client.get_channel(int(chan)).name} from DONT_SCAN_LINKS list")
                            welcomechan.remove(str(chan))
                            with open("settings/welcome_channel.json", "w") as welcom:
                                welcom.write(json.dumps(welcomechan), indent=4)
                    except:
                        await message.channel.send("skip_scan\nOptions:\nadd - expecting channel ping\nrem - expecting channel ping")

            if(args[1].lower() == "language"):
                    await message.channel.send("Later... Still working on language files... ")
    except IndexError:
        embedVar = discord.Embed()
        await message.channel.send("options: welcome_channel/skip_scan/language")
    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")