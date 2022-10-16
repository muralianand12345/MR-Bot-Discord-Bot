import cogs.autoreport
import discord
import json
from datetime import datetime
from cogs.autoreport import report
from discord.ext.commands import Cog
from discord.ext import commands

rate=5
time=60

class report(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Report Command Ready - cooldown {}/{}".format(rate,time))
    
    @commands.command(aliases=["r"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def report(self,ctx,*,args):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(875691031004327996)
        with open ("/home/runner/Bot/report.json") as file:
            data=json.load(file)
            report_num=int(data["report_no"])
            report_num+=1

        embed = discord.Embed(title = "Report - '#{}'".format(report_num), description = "Your Report Has been Submitted Successfully By Mr Bot Service!!", colour = discord.Colour((0xe91e63)),timestamp=datetime.utcnow())
        embed.add_field (name = "Report Number"         , value = "{}".format(report_num)          , inline = False)
        embed.add_field (name = "Issue/Bug/problem"     , value = "{}".format(args)                , inline = False)
        embed.add_field (name = "Reported from" , value = "{}".format(ctx.guild.name)    )
        embed.add_field (name = "Reported By"   , value = "{}".format(ctx.author.mention)  )
        embed.set_footer(text = "{} **Thanks for reporting!!!. We will verify it .Have a nice day!**".format(ctx.author.name))
        backend = discord.Embed(title = "Report - '#{}'".format(report_num)  , description = "Someone has reported!", colour = discord.Colour((0xe91e63)))
        backend.add_field (name = "Report Number" , value = "{}".format(report_num))
        backend.add_field (name = "Issue/Bug"     , value = "{}".format(args)                , inline = False)
        backend.add_field (name = "Reported from" , value = "{}".format(ctx.guild.name)      , inline = False)
        backend.add_field (name = "Reported By"   , value = "User  : {}\nId  : {}\n"   .format(ctx.author.name,ctx.author.id)     , inline = False)
        backend.add_field (name = "Reported In"   , value = "Channel  : {}\nId  : {}\n".format(ctx.channel.name,ctx.channel.id)    , inline = False)
        data["report_no"]=int(report_num)
        with open("/home/runner/Bot/report.json","w") as file:
            json.dump(data,file)
        await ctx.send(embed=embed)
        await channel.send("<@&875690641982644254>",embed=backend)
 
def setup(client):
    client.add_cog(report(client))
