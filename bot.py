import discord
from discord.ext import commands
import time
 
client = commands.Bot(command_prefix = ',')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command
async def help(ctx):
    await ctx.send('List of availible commands:\n^\help')

@client.command
async def clear(ctx, amount=99999999999999):
    new_clear = amount-1
    await ctx.channel.purge(limit=amount)
    time.sleep(0.2)
    await ctx.send(f'I have cleared {new_clear} messages.')

client.run('Njk5NDIyODA0Mjk0MjM4MjQ4.Xrx8-A.WiCFhu2R-Me4XdZBaAn7vM-CPvQ')
