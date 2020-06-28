#!/usr/bin/env python3

import discord
from discord.ext import commands, tasks
import time
import secrets
import os
from settings import myenv

#token = os.environ.get('SM_TOKEN')
#print(token)

client = commands.Bot(command_prefix = commands.when_mentioned_or('^'))
global tuidle
global mygame
mygame = discord.Game(f'{myenv.PREFIX}help | {myenv.SUPPORT_SERVER} | {myenv.PREFIX}{myenv.EXTRA_COMMAND}')

@client.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    if member.guild.id == 723044268620644403:
        await member.add_roles(member.guild.get_role(723667695295266886))
    elif member.guild.id == 709904664472059965:
        if member.bot:
            await member.add_roles(member.guild.get_role(709905242837483550))
    elif member.guild.id == 725613389933445171:
        if member.bot:
            await member.add_roles(member.guild.get_role(725938115360981018))

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=mygame)

@client.command()
async def token(ctx, member: discord.Member):
    user = member.id
    tokensend = secrets.token_urlsafe(40)
    message = (f'Here\'s your bot verification token: {tokensend}')
    await user.send(message)
    tuidle = 300

@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.trigger_typing()
    time.sleep(0.05)
    await ctx.send(f'`Loaded` {extension}')
    tuidle = 300

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        mes = ctx.message
        await mes.delete()
        await ctx.channel.trigger_typing()
        time.sleep(0.05)
        mymes = await ctx.send(f"`ERROR 403: Forbidden`\nYou need to be <@!{myenv.OWNER_ID}> to use this.")
        time.sleep(10)
        await mymes.delete()

@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.channel.trigger_typing()
    time.sleep(0.05)
    mymes = await ctx.send(f'`Unloaded` {extension}')
    time.sleep(5)
    await mymes.delete()
    tuidle = 300


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        mes = ctx.message
        await mes.delete()
        await ctx.channel.trigger_typing()
        time.sleep(0.05)
        mymes = await ctx.send(f"`ERROR 403: Forbidden`\nYou need to be <@!{myenv.OWNER_ID}> to use this.")
        time.sleep(10)
        await mymes.delete()

@client.command()
async def guide(ctx):
    await ctx.channel.trigger_typing()
    time.sleep(0.05)
    await ctx.send("Here's a link for my guide:\nhttps://docs.google.com/document/d/1IMvLL7D0hfpRCXJRZCFZGGGWDZY5Eu1SeSOEXeishCw/edit?usp=sharing")

@client.command()
async def invite(ctx):
    await ctx.channel.trigger_typing()
    time.sleep(0.05)
    await ctx.send('Click here to invite me!\nhttps://discord.com/api/oauth2/authorize?client_id=699422804294238248&permissions=8&scope=bot')

def check_btp():
    def predicate(ctx):
        return ctx.guild.id == 709904664472059965
    return commands.check(predicate)

def check_game_server():
    def predicate(ctx):
        return ctx.guild.id == 725613389933445171
    return commands.check(predicate)

@client.command()
@check_game_server()
async def vote(ctx, time, *, game):
    votetext = f'{ctx.author} requested the game {game} at time {time}.'
    vote_collector = 609544328737456149
    await vote_collecter.send(votetext)
    await ctx.message.delete()
    await ctx.send(f'Thank you! Your vote has been successfully collected and sent to {vote_collecter.mention}.', delete_after=3)


@client.command()
@check_btp()
async def addbot(ctx):
    pass

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(myenv.BOT_TOKEN)
