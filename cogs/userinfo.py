from discord import message
import cogs.autoreport,discord
from cogs.autoreport import report
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime
from cogs.autoreport import report

rate=5
time=60 

class userinfo(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Info Command Ready! - cooldown {}/{}".format(rate,time))
    
 
    @commands.command(aliases=["inf","userinfo","userinf","ui","iu"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def info(self,ctx,member: discord.Member=None):
        if member == None :
            member = ctx.author
        if member == self.client.user:
           return
        if member.is_on_mobile() == True:
            mobile="Mobile Discord BOII"
        else:
            mobile="Desktop/Web"
        
        if member.bot: 
            bot = "yes"
        else:
            bot = "No"
        
        try: 
            try:
               if member.id == 871808426240520253:
                  activity = "Listening to help"
               else:
                  activity = str(member.activity.name)
            except:
               activity = str(member.activity)
            #activity = str(member.activity)
            embed = discord.Embed(title = "User Information - {}".format(member.display_name),colour=discord.Colour((0x1abc9c)),timestamp=datetime.utcnow())
            embed.add_field(name = "Account Name"  , value = "{}".format(member.name)          , inline=True)
            embed.add_field(name = "Tag"           , value = "{}".format(member.discriminator) , inline=True)
            embed.add_field(name = "Top Role"      , value = "{}".format(member.top_role)      , inline=True)
            embed.add_field(name = "Current Status", value = "{}".format(str(member.status)) , inline=True) 
            embed.add_field(name = "Is Bot"        , value = "{}".format(bot)                  , inline=True)
            embed.add_field(name = "Device Type"   , value = "{}".format(mobile)               , inline=True)
            embed.add_field(name = "Mutual servers", value = "{}".format(len(member.mutual_guilds)))
            embed.add_field(name = "No Of Roles"   , value = "{}".format(len(member.roles)-1)  , inline=True)
            embed.add_field(name = "ID"            , value = "{}".format(member.id)            , inline=True)
            embed.add_field(name = "Current Activity" , value = "{}".format(activity) , inline = True)
            embed.add_field(name = "Member Since"     , value = "{}".format(member.created_at.strftime("%d/%m/%Y"))  , inline = True)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("500 - Internal Error Occured")
            await ctx.send("***Triggering Automatic Report service***")
            server_name=ctx.guild.name
            channel_name=ctx.channel.name
            channel_id=ctx.channel.id 
            author=ctx.author
            author_id=ctx.author.id
            message_content=ctx.message.content
            status="500 Internal Error - possibly Device Type"
            message_id=ctx.message.id
            rep_by="User Info Command"
            await ctx.send(embed=report(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status,message_id,rep_by).autoreport())
            log=self.client.get_channel(875690555621924864)
            await log.send(embed=report(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status,message_id,rep_by).autoreport())
            
def setup(client):
    client.add_cog(userinfo(client))
            
