import discord
from discord.ext import commands
import json

with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

def is_owner_of_bot(memid):
    return memid in config['owners']

async def save_error(msg, file, ex):
    with open('cmds/error.json', 'r', encoding='utf-8') as f:
        err = json.load(f)
    data = {"message": msg, "crashed_file": file, "error": str(ex)}
    err["errors"].append(data)

    with open('cmds/error.json', 'w', encoding='utf-8') as f:
        json.dump(err, f, ensure_ascii=False, indent=4)

def noas_save_error(msg, file, ex):
    with open('cmds/error.json', 'r', encoding='utf-8') as f:
        err = json.load(f)
    data = {"message": msg, "crashed_file": file, "error": str(ex)}
    err["errors"].append(data)

    with open('cmds/error.json', 'w', encoding='utf-8') as f:
        json.dump(err, f, ensure_ascii=False, indent=4)

async def check_perms_if(ctx, member):
    """ Custom (weird) way to check permissions when handling moderation commands """
    try:
        # Self checks
        if member.id == ctx.author.id:
            return False
        if member.id == ctx.bot.user.id:
            return False

        # Check if user bypasses
        if ctx.author.id == ctx.guild.owner.id:
            return False

        # Now permission check
        if member.id in config["owners"]:
            if ctx.author.id not in config["owners"]:
                return False
            else:
                pass
        if member.id == ctx.guild.owner.id:
            return False
        if ctx.author.top_role == member.top_role:
            return False
        if ctx.author.top_role < member.top_role:
            return False
        return True
    except Exception as e:
        return False

async def Let_Load_Backup(ctx):
    try:
        if ctx.author.id == ctx.guild.owner.id:
            return True
        elif(ctx.author.top_role.permissions.administrator):
            return True
        else:
            return False
    except:
        return False

async def check_perms(ctx, member, cmd):
    """ Custom (weird) way to check permissions when handling moderation commands """
    try:
        # Self checks
        if member.id == ctx.author.id:
            return await ctx.channel.send(f"You can't {cmd} yourself")
        if member.id == ctx.bot.user.id:
            return await ctx.channel.send("So that's what you think of me huh..? sad ;-;")

        # Check if user bypasses
        if ctx.author.id == ctx.guild.owner.id:
            return False

        # Now permission check
        if member.id in config["owners"]:
            if ctx.author.id not in config["owners"]:
                return await ctx.channel.send(f"I can't {cmd} my creator ;-;")
            else:
                pass
        if member.id == ctx.guild.owner.id:
            return await ctx.channel.send(f"You can't {cmd} the owner, lol")
        if ctx.author.top_role == member.top_role:
            return await ctx.channel.send(f"You can't {cmd} someone who has the same permissions as you...")
        if ctx.author.top_role < member.top_role:
            return await ctx.channel.send(f"Nope, you can't {cmd} someone higher than yourself.")
        return True
    except Exception as e:
        return await ctx.channel.send(f"Can't run my permission check bro. Try again later.\n" + e)

async def admin_perms(ctx, member):
    """ Custom (weird) way to check permissions when handling moderation commands """
    try:
        if member.id in config["owners"]:
            pass
        elif member.id != ctx.guild.owner.id:
            return await ctx.channel.send(f"This command is only for SERVER OWNER")
        return True
    except Exception as e:
        return await ctx.channel.send(f"Can't run my permission check bro. Try again later.\n" + e)

def admin_perms_if(member):
    """ Custom (weird) way to check permissions when handling moderation commands """
    try:
        if member.id in config["owners"]:
            pass
        elif member.id != ctx.guild.owner.id:
            return False
        return True
    except Exception as e:
        return False



