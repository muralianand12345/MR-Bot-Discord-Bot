import discord,discord.ext
from discord import client
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import Command


class log(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Logs Ready")
    
def setup(client):
    client.add_cog(log(client))