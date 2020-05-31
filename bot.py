import discord
from discord.ext import commands
import time
import secrets
import os
 
client = commands.Bot(command_prefix = ('^' or '@ServerManager#9610'))

global tuidle
global mygame
mygame = discord.Game('^help | discord.gg/T8P4PCS | ^invite')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=mygame)

@client.command()
async def clear(ctx, amount=99999999999999):
    new_clear = amount+1
    await ctx.channel.purge(limit=new_clear)
    if amount == 1:
        await ctx.send(f'`Cleared` {amount} message')
    else:
        await ctx.send(f'`Cleared` {amount} messages')
    time.sleep(3)
    await ctx.channel.purge(limit=1)
    tuidle = 300


@client.command()
async def token(ctx, member: discord.Member):
    user = member.id
    tokensend = secrets.token_urlsafe(40)
    message = (f'Here\'s your bot verification token: {tokensend}')
    await user.send(message)
    tuidle = 300

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'`Kicked` {member.mention}')
    tuidle = 300

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'`Banned` {member.mention} with the reason `{reason}`.')
    tuidle = 300

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'`Unbanned` {user.mention}')
            return
    tuidle = 300

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'`Loaded` {extension}')
    tuidle = 300

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'`Unloaded` {extension}')
    tuidle = 300

@client.command()
async def guide(ctx):
    await ctx.send("Here's a link for my guide:\nhttps://docs.google.com/document/d/1IMvLL7D0hfpRCXJRZCFZGGGWDZY5Eu1SeSOEXeishCw/edit?usp=sharing")

@client.command()
async def invite(ctx):
    await ctx.send('Click here to invite me! https://discord.com/api/oauth2/authorize?client_id=699422804294238248&permissions=8&scope=bot')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Njk5NDIyODA0Mjk0MjM4MjQ4.Xrx8-A.WiCFhu2R-Me4XdZBaAn7vM-CPvQ')
