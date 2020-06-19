#!/usr/bin/env python3

import discord
from discord.ext import commands, tasks
import time
import secrets
import os
from settings import myenv

#token = os.environ.get('SM_TOKEN')
#print(token)

client = commands.Bot(command_prefix = ['^', '@ServerManager#9610 '])
global tuidle
global mygame
mygame = discord.Game(f'{myenv.PREFIX}help | {myenv.SUPPORT_SERVER} | {myenv.PREFIX}invite')

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

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(myenv.BOT_TOKEN)
