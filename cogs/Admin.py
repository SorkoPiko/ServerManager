import discord
from discord.ext import commands

global mygame
mygame = discord.Game('^help | discord.gg/T8P4PCS | ^invite')

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events

    @commands.Cog.listener()
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=mygame)

    #Commands

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=99999999999999):
        new_clear = amount+1
        await ctx.channel.purge(limit=new_clear)
        if amount == 1:
            await ctx.send(f'`Cleared` {amount} message')
        else:
            await ctx.send(f'`Cleared` {amount} messages')
        time.sleep(3)
        await ctx.channel.purge(limit=1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'`Kicked` {member.mention}')


def setup(client):
    client.add_cog(Admin(client))
