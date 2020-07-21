import discord
from discord.ext import commands
import asyncio
from settings import myenv

global swearing_on
swearing_on = []

global mygame
mygame = discord.Game(f'{myenv.PREFIX}help | {myenv.SUPPORT_SERVER} | {myenv.PREFIX}{myenv.EXTRA_COMMAND}')

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    def auditLog(self, log):
        with open("cogs/AuditLog.txt", 'a') as file:
            file.write('\n' + log)

    #Events

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=mygame)

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.guild.id in swearing_on:
                if myenv.SWEAR_WORD1 in message.content:
                    await message.delete()
                    await message.channnel.trigger_typing()
                    await asyncio.sleep(0.05)
                    await message.channnel.send('No swearing. Sorry.', delete_after=5)
                elif myenv.SWEAR_WORD2 in message.content:
                    await message.delete()
                    await message.channnel.trigger_typing()
                    await asyncio.sleep(0.05)
                    await message.channnel.send('No swearing. Sorry.', delete_after=5)
                elif myenv.SWEAR_WORD3 in message.content:
                    await message.delete()
                    await message.channnel.trigger_typing()
                    await asyncio.sleep(0.05)
                    await message.channnel.send('No swearing. Sorry.', delete_after=5)
                elif myenv.SWEAR_WORD4 in message.content:
                    await message.delete()
                    await message.channnel.trigger_typing()
                    await asyncio.sleep(0.05)
                    await message.channnel.send('No swearing. Sorry.', delete_after=5)
        except AttributeError:
            pass

    #Commands

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int=999999999999999, user: discord.Member=None):
        messages = await ctx.channel.history(limit=amount+1).flatten()
        mess_len = len(messages)-1
        if mess_len == 1:
            await ctx.channel.purge(limit=1)
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send('`Cleared` 1  message', delete_after=3)
        elif mess_len > 100:
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            await ctx.send(f'You are clearing `100+ messages ({mess_len}).` Do you wish to proceed? (React with `:thumbsup:`). You have `60 seconds` to respond.', delete_after=60)
            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel and msg.content == 'yes'
            try:
                msg = await self.client.wait_for('message', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send('`Timed Out.`', delete_after=3)
            else:
                await ctx.channel.purge(limit=mess_len+1)
        else:
            await ctx.channel.purge(limit=mess_len+2)
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send(f'`Cleared` {mess_len} messages', delete_after=3)
        audit = f'{ctx.author} ({ctx.author.id}) cleared {mess_len} message(s) in channel #{ctx.channel} in guild {ctx.guild} at time {ctx.message.created_at} UTC.'
        self.auditLog(audit)
        
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            mes = ctx.message
            await mes.delete()
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send("`ERROR 403: Forbidden`\n`I`/`You` need to have `Manage Messages` permissions to use this.")
            await asyncio.sleep(10)
            await mymes.delete()

    @commands.command(aliases=['emojis'], description="Make the current channel an emoji list.")
    @commands.has_permissions(manage_emojis=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def emojilist(self, ctx, channel_pos: int=1):
        myemoji = ctx.guild.emojis
        overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(
                send_messages=False
                )
        }
        await ctx.send("`Cloning` the channel...", delete_after=3)
        channel = await ctx.channel.clone(name="emoji-list")
        await ctx.channel.delete()
        my1 = await channel.send('Done!\n`Editing` the channel...')
        await channel.edit(name="emoji-list", topic="This is the emoji list, where you can find this server's emojis.", position=channel_pos, nsfw=False, category=None, slowmode_delay=0, type=discord.ChannelType.text, reason=f"{ctx.author} made this channel an emoji list", overwrites=overwrites)
        my2 = await channel.send("Done!")
        await asyncio.sleep(3)
        await my2.delete()
        await my1.delete()
        for x in myemoji:
            #theemoji = myemoji[x]
            await channel.send(f'{x} -- `{x}`')
        audit = f"{ctx.author} ({ctx.author.id}) created an emoji list in channel #{channel} in guild {ctx.guild} at time {ctx.message.created_at} UTC."
        self.auditLog(audit)

    @emojilist.error
    async def emojilist_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            mes = ctx.message
            await mes.delete()
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send("`ERROR 403: Forbidden`\nEither:\n`I` need to have `Manage Messages` permissions to use this.\nOr:\n`You` need to have `Manage Emojis` permissions to use this.")
            await asyncio.sleep(10)
            await mymes.delete()

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def swearing(self, ctx, onoff: str='on'):
        if onoff == 'on':
            if ctx.guild.id in swearing_on:
                await ctx.channel.trigger_typing()
                await asyncio.sleep(0.05)
                await ctx.send('Your server is already has swearing disabled!', delete_after=5)
            else:
                swearing_on.append(ctx.guild.id)
                await ctx.channel.trigger_typing()
                await asyncio.sleep(0.05)
                await ctx.send('Done! Your server no longer supports swearing!', delete_after=5)
        elif onoff == 'off':
            if ctx.guild.id not in swearing_on:
                await ctx.channel.trigger_typing()
                await asyncio.sleep(0.05)
                await ctx.send('Your server already allows swearing!', delete_after=3)
            else:
                swearing_on.remove(ctx.guild.id)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.05)
        await ctx.send(f'`Kicked` {member.mention}')
        audit = f'{ctx.author} ({ctx.author.id}) kicked {member} in channel #{ctx.channel} in guild {ctx.guild} at time {ctx.message.created_at} UTC.'
        self.auditLog(audit)
        
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            mes = ctx.message
            await mes.delete()
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send("`ERROR 403: Forbidden`\n`I/`You` need to have `Kick Members` permissions to use this.")
            await asyncio.sleep(10)
            await mymes.delete()
            

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.05)
        await ctx.send(f'`Banned` {member.mention} with the reason `{reason}`.')
        audit = f'{ctx.author} ({ctx.author.id}) banned {member} in channel #{ctx.channel} in guild {ctx.guild} at time {ctx.message.created_at} UTC.'
        self.auditLog(audit)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            mes = ctx.message
            await mes.delete()
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send("`ERROR 403: Forbidden`\n`I`/`You` need to have `Ban Members` permissions to use this.")
            await asyncio.sleep(10)
            await mymes.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.trigger_typing()
                await asyncio.sleep(0.05)
                await ctx.send(f'`Unbanned` {user.mention}')
                audit = f'{ctx.author} ({ctx.author.id}) unbanned {member} in channel #{ctx.channel} in guild {ctx.guild} at time {ctx.message.created_at} UTC.'
                self.auditLog(audit)
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            mes = ctx.message
            await mes.delete()
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send("`ERROR 403: Forbidden`\n`I`/`You` need to have `Ban Members` permissions to use this.")
            await asyncio.sleep(10)
            await mymes.delete()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        mes = ctx.message
        #async with ctx.channel.typing():
            #await asyncio.sleep(0.1)
            #mymes = await ctx.send('Logging off...')
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.05)
        await ctx.send('Logging off...', delete_after=1)
        await mes.delete()
        audit = f"{ctx.author} ({ctx.author.id}) initiated shutdown in channel #{ctx.channel} in guild {ctx.guild} at time {ctx.message.created_at} UTC."
        self.auditLog(audit)
        await self.client.logout()

    @shutdown.error
    async def shutdown_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            mes = ctx.message
            await mes.delete()
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send(f"`ERROR 403: Forbidden`\n`You` need to be <@!{myenv.OWNER_ID}> to use this.")
            await asyncio.sleep(10)
            await mymes.delete()
            
    @commands.command(hidden=True)
    @commands.is_owner()
    async def allemoji(self, ctx):
        mes = ctx.message
        await mes.delete()
        allemoji = self.client.emojis
        for emoji in allemoji:
            await ctx.send(f"{emoji} -- `{emoji}` from {emoji.guild}")

    @allemoji.error
    async def allemoji_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            mes = ctx.message
            await mes.delete()
            await ctx.channel.trigger_typing()
            await asyncio.sleep(0.05)
            mymes = await ctx.send(f"`ERROR 403: Forbidden`\n`You` need to be <@!{myenv.OWNER_ID}> to use this.")
            await asyncio.sleep(10)
            await mymes.delete()

def setup(client):
    client.add_cog(Admin(client))
