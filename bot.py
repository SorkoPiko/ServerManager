#!/usr/bin/env python3

try:
    import discord
    from discord.ext import commands, tasks
    import asyncio
    import secrets
    import os
    from settings import myenv
except Exception:
    import subprocess
    subprocess.run(["python3", "-m", "pip", "install", "-r" "requirements.txt"])
#token = os.environ.get('SM_TOKEN')
#print(token)

global verification_tokens
global bot_info
bot_info = {}
verification_tokens = {}

client = commands.Bot(command_prefix = commands.when_mentioned_or(myenv.PREFIX))
global tuidle
global mygame
mygame = discord.Game(f'{myenv.PREFIX}help | {myenv.SUPPORT_SERVER} | {myenv.PREFIX}{myenv.EXTRA_COMMAND}')

def check_btp():
    def predicate(ctx):
        return ctx.guild.id == 709904664472059965
    return commands.check(predicate)

@client.event
async def on_message(message):
    if message.channel.id == 732445949820928021 or message.channel.id == 735768096152879114:
        if message.channel.id == 732445949820928021:
            log = client.get_channel(730575039677857842)
        elif message.channel.id == 735768096152879114:
            log = client.get_channel(710293107773538326)
        await log.send(f'{message.content} `sent in `{message.channel.mention}` by `{message.author.mention}. Message ID: {message.id}')
        for embed in message.embeds:
            await log.send(f'Message ID: {message.id}. Embed: ', embed=embed)
        for attachment in message.attachments:
            file = await attachment.to_file()
            await log.send(f'Message ID: {message.id}. Attachment: ', file=file)
    elif message.channel.id == 730530957160874121:
            if ' my bot invite link is https://discord.com/oauth2/authorize' in message.content:
                await message.channel.send(f'Seriously, {message.author.mention}! You don\'t have to make your message EXACTLY like shown!')
            elif ' my bot invite link is https://discordapp.com/oauth2/authorize' in message.content:
                await message.channel.send(f'Seriously, {message.author.mention}! You don\'t have to make your message EXACTLY like shown!')
    elif message.content.startswith('^thumb'):
        channel = message.channel
        await channel.send('`React` with 👍')

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
            #Add Robos roles for bots in the BTP
            roles = []
            roles.append(member.guild.get_role(709905242837483550))
            roles.append(member.guild.get_role(731303770654375937))
            roles.append(member.guild.get_role(735006808326013020))
            await member.edit(nick=f'{member.name} | !help', roles=roles)
    elif member.guild.id == 725613389933445171:
        if member.bot:
            await member.add_roles(member.guild.get_role(725938115360981018))

#@client.command()
#@check_btp()
#async def token(ctx, member: discord.Member):
#    tokensend = secrets.token_urlsafe(40)
#    message = (f'Here\'s your bot verification token: {tokensend}')
#    await member.send(message)

@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.channel.trigger_typing()
    await asyncio.sleep(0.05)
    await ctx.send(f'`Loaded` {extension}')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        mes = ctx.message
        await mes.delete()
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.05)
        await ctx.send(f"`ERROR 403: Forbidden`\nYou need to be <@!{myenv.OWNER_ID}> to use this.", delete_after=10)

@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.channel.trigger_typing()
    await asyncio.sleep(0.05)
    mymes = await ctx.send(f'`Unloaded` {extension}')
    await asyncio.sleep(5)
    await mymes.delete()

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        mes = ctx.message
        await mes.delete()
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.05)
        mymes = await ctx.send(f"`ERROR 403: Forbidden`\nYou need to be <@!{myenv.OWNER_ID}> to use this.")
        await asyncio.sleep(10)
        await mymes.delete()

@client.command()
async def guide(ctx):
    await ctx.channel.trigger_typing()
    await asyncio.sleep(0.05)
    await ctx.send("Here's a link for my guide:\nhttps://docs.google.com/document/d/1IMvLL7D0hfpRCXJRZCFZGGGWDZY5Eu1SeSOEXeishCw/edit?usp=sharing")

@client.command()
async def invite(ctx):
    await ctx.channel.trigger_typing()
    await asyncio.sleep(0.05)
    await ctx.send('Click here to invite me!\nhttps://discord.com/api/oauth2/authorize?client_id=699422804294238248&permissions=8&scope=bot')

def check_game_server():
    def predicate(ctx):
        return ctx.guild.id == 725613389933445171
    return commands.check(predicate)

@client.command()
@check_game_server()
async def vote(ctx, vote_collecter: discord.Member, time, *, game):
    votetext = f'{ctx.author.mention} requested the game {game} at time {time}.'
    await vote_collecter.send(votetext)
    await ctx.message.delete()
    await ctx.send(f'Thank you! Your vote has been successfully collected and sent to {vote_collecter.mention}.', delete_after=3)

@client.command()
@check_btp()
async def get_token(ctx, name, client_id, prefix, *, owners: discord.Member):
    tokensend = secrets.token_urlsafe(40)
    #Regenerate token if it already exists, very low chance though
    if tokensend in verification_tokens or bot_info:
        tokensend = secrets.token_urlsafe(40)
    verification_tokens[ctx.author] = tokensend
    for owner in owners.split(' '):
        verification_tokens[owner] = tokensend
    bot_info[tokensend] = f'{owners} {ctx.author} {name} {client_id} {prefix}'
    message = (f'Here\'s your bot verification token: {tokensend}/nEnter it in <#!730530957160874121>')
    for owner in owners.split(' '):
        await owner.send(message)

@client.command()
@check_btp()
async def addbot(ctx, token):
    if_verified = verification_tokens.get[ctx.author]
    if if_verified == token:
        bot_info.get(token)

client.load_extension('jishaku')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

import aiohttp

def runclient():
    try:
        client.run(myenv.BOT_TOKEN)
    except aiohttp.client_exceptions.ClientConnectorError:
        print('Bot failed connecting.')
        #retry = input('Retry connecting? yes/no ')
        #if retry == 'yes':
            #print('Retrying...')
            #try:
                #client.run(myenv.BOT_TOKEN)
            #except aiohttp.client_exceptions.ClientConnectorError:
                #print('Bot failed connecting. Terminating...')
        #else:
           #print('Terminating...')
    #except RuntimeError:
        #print('RuntimeError. Terminating...')

runclient()
