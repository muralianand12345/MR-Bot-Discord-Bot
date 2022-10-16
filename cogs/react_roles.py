import discord
from discord.ext import commands
from discord.utils import get 
from discord.ext.commands import Cog,has_permissions 

class reaction(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_reaction_add(self,reaction,user):
        if reaction.emoji == "🪔":
            role = get(user.guild.roles, id=905652706612490271)
            await user.add_roles(role)
   
    @Cog.listener()
    async def on_reaction_remove(self,reaction,user):
        if reaction.emoji == "🪔":
            role = get(user.guild.roles, id=905652706612490271)
            await user.remove_roles(role)

    @commands.command()
    @commands.guild_only()
    @has_permissions(administrator=True)
    async def rect(self,ctx):
        if ctx.guild.id == 868390640944300032:
        	embed=discord.Embed(title="Festival Of Lights - LE",color=discord.Colour.green())
        	a=await ctx.send(embed=embed)
        	await a.add_reaction("🪔")

def setup(client):
    client.add_cog(reaction(client))
