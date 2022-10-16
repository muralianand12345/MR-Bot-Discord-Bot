import discord
from discord.ext import commands
from discord.ext.commands import Cog,bot_has_permissions

rate=5
time=60

class ban(Cog):
    def __init__(self,client):
        self.client=client
     
    @Cog.listener()
    async def on_ready(self):
        print("Ban Command Ready! - cooldown {}/{}".format(rate,time))

    @commands.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    async def ban(self,ctx, member: discord.Member=None,*,reason=None):
        if not member:
            await ctx.reply("**Kindly mention a user**")
        elif member.id == ctx.author.id:
            await ctx.reply("***If you want yourself to be banned..kindly contact server administrator***")
        elif member.guild_permissions.ban_members or member.guild_permissions.kick_members:
            emcon=discord.Embed(title="Wait... R u kidding me?? you can't ban a mod ❌",description="If you face any issues. kindly contact your server developer or use -report",colour=discord.Colour.red())
            await ctx.reply(embed=emcon)        
        elif not reason:
            await ctx.reply("**Hello! mod kindly specify a reason for ban**")
        else:
            embed=discord.Embed(title="Banned user",colour=discord.Colour.red())
            embed.add_field(name = "Account Name"  , value = "{}".format(member.name)          , inline=True)
            embed.add_field(name = "Tag"           , value = "{}".format(member.discriminator) , inline=True)
            embed.add_field(name = "Top Role"      , value = "{}".format(member.top_role)      , inline=True)
            embed.add_field(name = "No Of Roles"   , value = "{}".format(len(member.roles)-1)  , inline=True)
            embed.add_field(name = "ID"            , value = "{}".format(member.id)            , inline=True)
            embed.add_field(name = "Member Since"  , value = "{}".format(member.created_at.strftime("%d/%m/%Y"))  , inline = True)
            embed.add_field(name = "credits"       , value = "{}".format(ctx.author.mention))
            embed.add_field(name = "Reason"        , value = "{}".format(reason))
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="user -serverinfo(si) to check banned members of server")
            if ctx.guild.id == 868390640944300032:
                mod_log=self.client.get_channel(869200831717736478)
                await mod_log.send(embed=embed)
                await ctx.send(embed=embed)
                await member.send(embed=embed)
                await ctx.guild.ban(member)

def setup(client):
    client.add_cog(ban(client))

