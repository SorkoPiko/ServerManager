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
        messages = await ctx.channel.purge(limit=amount)
        mess_len = len(messages)
        if amount == 1:
            await ctx.send('`Cleared` 1  message')
        else:
            message_end = await ctx.send(f'`Cleared` {mess_len} messages')
        message_end.delete(delay=3)
        await ctx.channel.purge(limit=1)
        print(f'{ctx.author} cleared {mess_len} messages in channel #{ctx.channel} in guild {ctx.guild}.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'`Kicked` {member.mention}')
        print(f'{ctx.author} kicked {member} in guild {ctx.guild}.')
        if ctx.command_failed == True:
            await ctx.send('`Command Failed. Sorry.`')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'`Banned` {member.mention} with the reason `{reason}`.')
        print(f'{ctx.author} banned {member} in guild {ctx.guild}.')
        if ctx.command_failed == True:
            await ctx.send('`Command Failed. Sorry.`')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'`Unbanned` {user.mention}')
                print(f'{ctx.author} unbanned {member} in guild {ctx.guild}.')
                return
            if ctx.command_failed == True:
                await ctx.send('`Command Failed. Sorry.`')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Logging off...')
        time.sleep(1)
        await ctx.channel.purge(limit=2)
        await self.client.logout()

def setup(client):
    client.add_cog(Admin(client))
