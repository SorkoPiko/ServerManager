import dsiscord
from discord.ext import commands

class Status(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events

    #Commands
    @commands.command()
    async def status(self, ctx, status):
        if status == 'dnd':
            mystatus = discord.Status.dnd
        if status == 'idle':
            mystatus = discord.Status.idle
        if status == 'offline':
            mystatus = discord.Status.offline
        if status == 'online':
            mystatus = discord.Status.online
        await client.change_presence(status=mystatus)
        await ctx.send('`Status` changed')

def setup(client):
    client.add_cog(Status(client))