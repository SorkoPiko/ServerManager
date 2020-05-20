import discord
from discord.ext import commands

class Setup(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')
        ctx.send('I am now online!')

    #Commands
    @commands.command()
    @client.command()
    async def ping(ctx):
        await ctx.send(f':ping_pong: Pong! {round(client.latency * 1000)}ms :ping_pong:')
    
def setup(client):
    client.add_cog(Setup(client))