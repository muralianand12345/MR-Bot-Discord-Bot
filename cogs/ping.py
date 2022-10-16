import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands.cog import Cog
rate=5
time=60

class maincog(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Ping Ready - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["dingding"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def ping(self,ctx):
        await self.client.wait_until_ready()
        msg="Slow and steady wins the race."
        async with ctx.message.channel.typing():
            pass
        await ctx.send(f"**{round(self.client.latency * 1000)}ms behind your display lel**\n{msg}")
    
def setup(client):
    client.add_cog(maincog(client))
