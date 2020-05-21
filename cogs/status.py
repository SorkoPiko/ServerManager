import discord
from discord.ext import commands
import random

class Status(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events

    #Commands
    @commands.command()
    async def setstatus(self, ctx, *, status):
        tip = random.choice(1, 5)
        if tip == 4:
            goodtip = '\n\n**TIP:** Did you know that you can change my status by DM?'
        else:
            goodtip = None
        global sstatus
        mygame = discord.Game('^help | https://discord.gg/T8P4PCS')
        if status == ('dnd' or 'do not disturb'):
            mystatus = discord.Status.dnd
            sstatus = 'Do Not Disturb'
        if status == 'idle':
            mystatus = discord.Status.idle
            sstatus = 'Idle'
        if status == ('offline' or 'invisible'):
            mystatus = discord.Status.offline
            sstatus = 'offline'
        if status == 'Offline':
            mystatus = discord.Status.online
            sstatus = 'Online'
        await self.client.change_presence(status=mystatus, activity=mygame)
        if goodtip == None:
            await ctx.send(f'`Status` changed to `{sstatus}`')
        else:
            await ctx.send(f'`Status` changed to `{sstatus}`{goodtip}')
def setup(client):
    client.add_cog(Status(client))