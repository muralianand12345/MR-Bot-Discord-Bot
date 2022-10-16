import cogs.autoreport,discord
import discord
from discord.utils import get 
from cogs.autoreport import report
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime

rate=5
time=60

class ar(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Add role command ready! - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["ar"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def addrole(self,ctx, member: discord.Member=None,*,role: discord.Role=None):
        trole = get(ctx.guild.roles, name="{}".format(role))
        target = await ctx.guild.fetch_member(int(member.id))
    
        if not member or not role:
            await ctx.reply("*Kindly specify a user and a role")
        elif trole in target.roles:
            await ctx.reply("*{} already has role {}*".format(member.display_name,role.name))
        elif member and role:
            try:
            	await member.add_roles(role)
            	embed=discord.Embed(title="Operation Successful",description="Congrats {} you now have {} role".format(member.mention,role.mention),colour=discord.Colour.green())
            	embed.set_footer(text="https://bit.ly/mrthebot")
            	await ctx.send(embed=embed)
            except:
                embed=discord.Embed(title="Operation Unsuccessful",description="{} The role you are trying to assign must be lower/dominated by role that MR.BOT have.".format(ctx.author.mention),colour=discord.Colour.red())
                embed.set_footer(text="https://bit.ly/mrthebot")
                await ctx.send(embed=embed)
 
class rr(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Remove Role command Ready! - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["rr"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def removerole(self,ctx, member: discord.Member, role: discord.Role):
        trole = get(ctx.guild.roles, name="{}".format(role))
        target = await ctx.guild.fetch_member(int(member.id))
        if not member:
            await ctx.reply("I searched for {} in whole {} members unfortunately i can't find a valid member.".format(member,ctx.guild.member_count))
        elif not role:
            await ctx.reply("kindly mention a role!")
        elif trole not in target.roles:
            await ctx.reply("*{} does not have role {}*".format(member.display_name,role))
        elif member and role:
            try:
                await member.remove_roles(role)
                embed=discord.Embed(title="Operation Successful",description="Role {} has been removed from {}".format(role.mention,member.mention),colour=discord.Colour.green())
                embed.set_footer(text="https://bit.ly/mrthebot")
                await ctx.send(embed=embed)
            except:
                embed=discord.Embed(title="Operation Unsuccessful",description="{} The role you are trying to remove must be lower/dominated by role that MR.BOT have.".format(ctx.author.mention),colour=discord.Colour.red())
                embed.set_footer(text="https://bit.ly/mrthebot")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ar(client))
    client.add_cog(rr(client))
