import discord
from discord.ext import commands
import time
import secrets
 
client = commands.Bot(command_prefix = '^')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def clear(ctx, amount=99999999999999):
    new_clear = amount+1
    await ctx.channel.purge(limit=new_clear)
    time.sleep(0.2)
    await ctx.send(f'I have cleared {amount} messages.')

@client.command(pass_context=True)
async def token(ctx, user: discord.User, *, message=None):
    tokensend = secrets.token_urlsafe(40)
    message = (f'Here\'s your bot verification token: {tokensend}')
    await client.send_message(user, message)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

client.run('Njk5NDIyODA0Mjk0MjM4MjQ4.Xrx8-A.WiCFhu2R-Me4XdZBaAn7vM-CPvQ')
