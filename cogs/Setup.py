import asyncio
import discord
from discord.ext import commands
import time

class Setup(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.05)
        await ctx.send(f':ping_pong: Pong! {round(self.client.latency * 1000)}ms :ping_pong:')

        return
    
def setup(client):
    client.add_cog(Setup(client))
