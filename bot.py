import discord
from discord.ext import commands
 
client = commands.Bot(command_prefix = ',')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('Njk5NDIyODA0Mjk0MjM4MjQ4.Xrx8-A.WiCFhu2R-Me4XdZBaAn7vM-CPvQ')