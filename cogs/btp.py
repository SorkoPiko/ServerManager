import discord
from discord.ext import commands

class Cog(commands.Cog):
    def __init__(self, client):
        self.client=client


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded cog: {self.__name__}')

    

def setup(client):
    client.add_cog(Cog(client))