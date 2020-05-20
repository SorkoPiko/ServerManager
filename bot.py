import discord
from discord.ext import commands
import time
import secrets
import os
 
client = commands.Bot(command_prefix = ('^' or '@ServerManager'))

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount=99999999999999):
    new_clear = amount+1
    await ctx.channel.purge(limit=new_clear)
    if amount == 1:
        await ctx.send(f'`Cleared` {amount} message.')
        else:
            await ctx.send(f'`Cleared` {amount} messages.')
    time.sleep(3)
    await ctx.channel.purge(limit=1)


@client.command(pass_context=True)
async def token(ctx, user: discord.User, *, message=None):
    tokensend = secrets.token_urlsafe(40)
    message = (f'Here\'s your bot verification token: {tokensend}')
    await ctx.send_message(user, message)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'`Kicked` {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'`Banned` {member.mention} with the reason `{reason}`.')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'`Unbanned` {user.mention}')
            return

@client.command()
async def spam(ctx, user_id=300475086547451914):
    user = client.get_user(user_id)
    for x in range(100):
        await user.send('USE ME NOW')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[: - 3]}')

client.run('Njk5NDIyODA0Mjk0MjM4MjQ4.Xrx8-A.WiCFhu2R-Me4XdZBaAn7vM-CPvQ')
