import discord
from discord.ext import commands
from discord.utils import get
import discord.ext.commands
from datetime import datetime
from discord.ext.commands import Cog
rate=5
time=60

class unmute(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Unmute command Ready - cooldown {}/{}".format(rate,time))
    
    @commands.command(aliases=["unmute","umute"])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_roles=True)
    #@commands.has_any_role(868391773909684294,868391776329805886,868391773213442088)
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def lift(self,ctx,member: discord.Member=None):  
        muted = get(ctx.guild.roles, name="Muted")
        target = await ctx.guild.fetch_member(int(member.id))
        if not member:
            await ctx.reply("Mention any user to lift")
        elif muted not in target.roles:
            await ctx.reply("{} is not muted.".format(member.mention))
        else:
            if ctx.guild.id == 868390640944300032:
                mod_log = discord.Embed(title = "Release Details", description = "Released User {}".format(member.mention),colour=discord.Colour.random(),timestamp=datetime.utcnow())
                mod_log.add_field(name = "Method"   ,value="Overrided by {}".format(ctx.author.mention)   ,inline = False)
                mod_log_channel = self.client.get_channel(869200831717736478)
                await mod_log_channel.send(embed=mod_log)
  
            muted = get(ctx.guild.roles, name="Muted")
            embed = discord.Embed(title="Overriding automated lifting ",description="Lifted user {} Successfully!".format(member.mention),colour=discord.Colour.random(),timestamp=datetime.utcnow())
            embed.add_field(name  = "Method"       ,value = "Overridded By {}".format(ctx.author.mention) ,inline = False)
            embed.set_footer(text= "Think made a mistake?. Feel free to contact admin/server developer")
            remove = await member.remove_roles(muted)
            await ctx.send(embed=embed) 

def setup(client):
    client.add_cog(unmute(client))
