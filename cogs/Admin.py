import discord
from discord.ext import commands
import time

global mygame
mygame = discord.Game('^help | discord.gg/T8P4PCS | ^invite')

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=mygame)

    #Commands

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=99999999999999):
        perms = ctx.author.guild_permissions
        print(perms)
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

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'`Banned` {member.mention} with the reason `{reason}`.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'`Unbanned` {user.mention}')
                return

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Logging off...')
        time.sleep(1)
        await ctx.channel.purge(limit=2)
        await self.client.logout()

def setup(client):
    client.add_cog(Admin(client))
