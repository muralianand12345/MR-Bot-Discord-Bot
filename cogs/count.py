import cogs.autoreport,discord
from cogs.autoreport import report
from discord.ext.commands import Cog
from discord.ext import commands

rate=5
time=60

class count(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Count Command Ready! - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["c"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def count(self,ctx):
        embed = discord.Embed(title = "Total members in {} : {}\nWe are currenty serving {} servers".format(ctx.guild.name,ctx.guild.member_count,len(self.client.guilds)),color=discord.Colour((0xffff00)))
        embed.set_footer(text="In time of test, family is best.")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(count(client))    
  

