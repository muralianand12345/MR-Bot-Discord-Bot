import discord,discord.ext,random
import os
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Cog

rate=5
time=60

class uptime(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("heartbeat command Ready - cooldown {}/{}".format(rate,time))
    
    @commands.command(aliases=["hb","uptime","ut","up"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def heartbeat(self,ctx):
        uptime = os.popen('uptime -p').read()[:-1]
        embed = discord.Embed( title = "Heartbeat **{}**".format(uptime),color = discord.Colour.red(),timestamp=datetime.utcnow())
        embed.set_footer(text="Requested by {}".format(ctx.author.name))
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(uptime(client))