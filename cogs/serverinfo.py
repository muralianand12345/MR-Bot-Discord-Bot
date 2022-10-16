import discord
from cogs.autoreport import report
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime

rate=5
time=60

class serverinfo(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Server Info Command Ready! - cooldown {}/{}".format(rate,time))
    
    @commands.group(invoke_without_command=True,aliases=["si","serverinfo","infoserver"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def server(self,ctx):
        await self.client.wait_until_ready()
        off=0
        on=0
        for x in ctx.guild.members:
            if x.status == discord.Status.offline:
                off+=1
            else:
                on+=1

        server = discord.Embed(title = "Server Information".format(ctx.guild.name),colour=discord.Colour.green(),timestamp=datetime.utcnow())
        server.add_field(name = "Name"                       , value = "{}".format(ctx.guild.name))
        server.add_field(name = "Description"                , value = "{}".format(ctx.guild.description))
        server.add_field(name = "Owned By"                   , value = "{}".format(ctx.guild.owner))   
        server.add_field(name = "Region"                     , value = "{}".format(ctx.guild.region))
        server.add_field(name = "Members"                    , value = "{}".format(ctx.guild.member_count))
        server.add_field(name = "Online Members"             , value = "{}".format(on))
        server.add_field(name = "Offline Members"            , value = "{}".format(off))
        server.add_field(name = "Roles"                      , value = "{}".format(len(ctx.guild.roles)))
        server.add_field(name = "Category"                   , value = "{}".format(len(ctx.guild.categories)))
        server.add_field(name = "Channels"                   , value = "{}".format(len(ctx.guild.channels)))
        server.add_field(name = "Text Channels"              , value = "{}".format(len(ctx.guild.text_channels)))
        server.add_field(name = "Voice Channels"             , value = "{}".format(len(ctx.guild.voice_channels)))
        server.add_field(name = "Bans"                       , value = "{}".format(len(await ctx.guild.bans())))
        server.add_field(name = "Created On"                 , value = "{}".format(ctx.guild.created_at.strftime("%d/%m/%Y")))
        server.add_field(name = "ID"                         , value = "{}".format(ctx.guild.id))
        server.add_field(name = "Invites"                    , value = "{}".format(len(await ctx.guild.invites()))) 
        server.set_footer(text = "https://bit.ly/mrthebot")
        server.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=server)
        return server

    @server.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    @commands.guild_only()
    async def bans(self,ctx):
        bans = await ctx.guild.bans()
        name=["{0.name}#{0.discriminator} - {0.id}\n".format(ban.user) for ban in bans]
        #tag =["{0.discriminator}".format(ban.user) for ban in bans]
        embed = discord.Embed(title = "Server Ban List",colour=discord.Colour.red())
        embed.add_field(name="Account Details" , value = "{}".format("\n".join(name))) 
        await ctx.send(embed=embed) 


def setup(client):
    client.add_cog(serverinfo(client))
