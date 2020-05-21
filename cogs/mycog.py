import discord
from discord.ext import commands

class Setup(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        mygame = ('on ' + str(client.servers + ' | ^help'))
        await client.change_presence(status=discord.Status.idle, activity=discord.Game())
        print('Bot is online.')

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! {round(self.client.latency * 1000)}ms :ping_pong:')

        return
    
def setup(client):
    client.add_cog(Setup(client))
