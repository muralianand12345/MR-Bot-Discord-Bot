import discord
from discord.ext import commands
from discord.ext.commands import Cog 

rate=5
time=60

class avatar(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("AV Command ready - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["avatar","dp","profile"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def av(self,ctx,*,member : discord.Member=None):
        if member == None:
            member=ctx.author
            av=member.avatar_url
            emcon=discord.Embed(title="{}".format(ctx.author.name),colour=member.top_role.colour)
            emcon.set_image(url=av)
        else:
            av = member.avatar_url
            emcon=discord.Embed(title="{}".format(member.name),description="Looking good uh!",colour=member.top_role.colour)
            emcon.set_image(url=av)
        await ctx.send(embed=emcon)

def setup(client):
    client.add_cog(avatar(client))
