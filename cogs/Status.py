import discord
from discord.ext import commands
import random
from settings import myenv
import time

global tuidle
global mygame
mygame = discord.Game(f'{myenv.PREFIX}help | {myenv.SUPPORT_SERVER} | {myenv.PREFIX}{myenv.EXTRA_COMMAND}')


class Status(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    #Commands
    @commands.command(hidden=True, aliases=['status'])
    @commands.is_owner()
    async def setstatus(self, ctx, *, status):
        tip = random.randrange(1, 5)
        if tip == 4:
            goodtip = '\n\n**TIP:** Did you know that you can change my status by DM?'
        else:
            goodtip = None
        global sstatus
        global mystatus
        if status == ('dnd' or 'do not disturb'):
            mystatus = discord.Status.dnd
            sstatus = 'Do Not Disturb'
        if status == 'idle':
            mystatus = discord.Status.idle
            sstatus = 'Idle'
        if status == ('offline' or 'invisible'):
            mystatus = discord.Status.offline
            sstatus = 'Offline'
        if status == 'online':
            mystatus = discord.Status.online
            sstatus = 'Online'
        await self.client.change_presence(status=mystatus, activity=mygame)
        if goodtip == None:
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send(f'`Status` changed to `{sstatus}`')
        else:
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send(f'`Status` changed to `{sstatus}`{goodtip}')
        await asyncio.sleep(5)
        await mymes.delete()
        tuidle = 300
        
    @setstatus.error
    async def setstatus_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            mes = ctx.message
            await mes.delete()
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send(f"`ERROR 403: Forbidden`\n`You` need to be <@!{myenv.OWNER_ID}> to use this.")
            await asyncio.sleep(10)
            await mymes.delete()

def setup(client):
    client.add_cog(Status(client))
