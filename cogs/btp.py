import discord
from discord.ext import commands

class Cog(commands.Cog):
    def __init__(self, client):
        self.client=client

    @command.command()
	async def get_token(self, ctx, name, client_id, prefix, *, owners: discord.Member):
    	tokensend = secrets.token_urlsafe(40)
    	#Regenerate token if it already exists, very low chance though
    	if tokensend in verification_tokens or bot_info:
        	tokensend = secrets.token_urlsafe(40)
    	verification_tokens[ctx.author] = tokensend
    	for owner in owners.split(' '):
    	    verification_tokens[owner] = tokensend
    	bot_info[tokensend] = f'{owners} {ctx.author} {name} {client_id} {prefix}'
    	message = (f'Here\'s your bot verification token: {tokensend}/nEnter it in <#!730530957160874121>')
    	for owner in owners.split(' '):
    	    await owner.send(message)

def setup(client):
    client.add_cog(Cog(client))