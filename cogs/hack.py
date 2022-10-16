import discord
import random
from discord import member
from discord.ext import commands
from discord.ext.commands import Cog
from cogs.userinfo import userinfo
from asyncio import sleep
from datetime import datetime

rate=1
time=60

class hacker(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Hack command Ready! - cooldown {}/{}".format(rate,time))
    
    @commands.command(aliases=["heck"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    @commands.guild_only()
    async def hack(self,ctx,member: discord.Member=None):
        if not member:
            await ctx.reply("Mention a target")
            return
        if member.id == ctx.author.id:
            await ctx.reply("I can't hack you Iam frightened")
            return
        emcon=discord.Embed(title="Received order",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon1=discord.Embed(title="Preparing for battle",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon2=discord.Embed(title="Initializing attack vectors",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon3=discord.Embed(title="Started to Gather Information about target",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon4=discord.Embed(title="sending echo request to target",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon5=discord.Embed(title="Received **code-8** from target.  ***Hurray!!, host is up***",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon6=discord.Embed(title="Initializing Network scanners",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon7=discord.Embed(title="Initializing vulnerability scanners",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon8=discord.Embed(title="Searching social media profiles",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon9=discord.Embed(title="Deep diving in dark web",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon10=discord.Embed(title="searching for data leaks",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon11=discord.Embed(title="Acquired Infomation about the target",description="Attack mode : sniper",color=discord.Colour.orange(),timestamp=datetime.utcnow())
        
        emcon12=discord.Embed(title="Processing acquired information",description="Attack mode : sniper",color=discord.Colour.orange(),timestamp=datetime.utcnow())
        
        emcon13=discord.Embed(title="**All Set** ***Going Active***",description="Attack mode : sniper",color=discord.Colour.orange(),timestamp=datetime.utcnow())
        emcon26=discord.Embed(title="**All Set** ***Going Active***",description="Attack mode : sniper",color=discord.Colour.gold(),timestamp=datetime.utcnow())
        emcon27=discord.Embed(title="**All Set** ***Going Active***",description="Attack mode : sniper",color=discord.Colour.teal(),timestamp=datetime.utcnow())
        
        emcon14=discord.Embed(title="locating towers",description="Attack mode : sniper",color=discord.Colour.orange(),timestamp=datetime.utcnow())
        
        emcon15=discord.Embed(title="Breaching into towers",description="Attack mode : sniper",color=discord.Colour.orange(),timestamp=datetime.utcnow())
        
        emcon16=discord.Embed(title="Mayday! Mayday! found target in tower {}".format(random.randrange(1,500)),description="Attack mode : sniper",color=discord.Colour.dark_red(),timestamp=datetime.utcnow())
        
        emcon17=discord.Embed(title="Inflating cell tower ",description="Attack mode : sniper",color=discord.Colour.blurple(),timestamp=datetime.utcnow())
        
        emcon18=discord.Embed(title="Injecting payload stagers 10%".format(random.randrange(1,15)),description="Attack mode : sniper",color=discord.Colour.dark_red(),timestamp=datetime.utcnow())
        
        emcon19=discord.Embed(title="Injecting payload stagers 27%".format(random.randrange(16,45)),description="Attack mode : sniper",color=discord.Colour.dark_red(),timestamp=datetime.utcnow())
        
        emcon20=discord.Embed(title="Injecting payload stagers 44%".format(random.randrange(50,70)),description="Attack mode : sniper",color=discord.Colour.dark_red(),timestamp=datetime.utcnow())
        
        emcon21=discord.Embed(title="Injecting payload stagers 88%".format(random.randrange(75,89)),description="Attack mode : sniper",color=discord.Colour.dark_red(),timestamp=datetime.utcnow())
        
        emcon22=discord.Embed(title="Injecting payload stagers 100%",description="Attack mode : sniper",color=discord.Colour.dark_red(),timestamp=datetime.utcnow())
        
        emcon23=discord.Embed(title="Waiting for reverse connection",description="Attack mode : sniper",color=discord.Colour.dark_red(),timestamp=datetime.utcnow())
        
        emcon24=discord.Embed(title="Defense positions ready",description="Attack mode : Cluster Bomb",color=discord.Colour.dark_red(),timestamp=datetime.utcnow())
    
        emcon25=discord.Embed(title="Target has been hecked successsfully!",color=discord.Colour.purple(),timestamp=datetime.utcnow())
        emcon25.add_field(name="Hacked By",value="{}".format(ctx.author.mention))
        emcon25.add_field(name="Victim",value="{}".format(member.mention))
        emcon25.add_field(name="Attack style",value="Head shot with sniper")
        emcon25.add_field(name="Attack Mode",value="Hell as Active")
        emcon25.add_field(name="Damage Report",value="{} cell has been hacked with stagers and infected every possible devices in the network with worms and trojans. I messed with av and firewall and left only discord to see this message. simply to say victim is F****d up.".format(member.mention))    
        emcon25.add_field(name="suggestion",value="Be careful with {}".format(ctx.author.mention))
        emcon25.set_author(name="{}".format(member.name))
        emcon25.set_thumbnail(url="https://thumbs.dreamstime.com/b/skull-gangster-hat-cigar-black-background-quality-illustration-made-vector-skull-gangster-hat-cigar-186046449.jpg")
        emcon25.set_footer(text="Just for fun. your data is never touched by us")
        if member.bot: 
            bot = "yes"
        else:
            bot = "No"
        if member.is_on_mobile() == True:
           mob="Mobile"
        else:
           mob="Desktop"
        activity = str(member.activity)
        embed = discord.Embed(title = "Data Breached - {}".format(member.display_name),colour=discord.Colour((0x1abc9c)),timestamp=datetime.utcnow())
        embed.add_field(name = "Network Carrier"  , value = "{}".format(member.name)          , inline=True)
        embed.add_field(name = "Identifier"           , value = "{}".format(member.discriminator) , inline=True)
        embed.add_field(name = "Working as"      , value = "{}".format(member.top_role)      , inline=True)
        embed.add_field(name = "Network Status", value = "{}".format(str(member.status)) , inline=True) 
        embed.add_field(name = "Is Bot"        , value = "{}".format(bot)                  , inline=True)
        embed.add_field(name = "Device tapped"        , value = "{}".format(mob)                  , inline=True)
        embed.add_field(name = "Mutual contacts"        , value = "{}".format(len(member.mutual_guilds))                  , inline=True)
        embed.add_field(name = "No Of professions"   , value = "{}".format(len(member.roles)-1)    , inline=True)
        embed.add_field(name = "IMEI Number"            , value = "{}".format(member.id)            , inline=True)
        embed.add_field(name = "Info from Backdoor Listener" , value = "{}".format(activity) , inline = True)
        embed.add_field(name = "Device Manufactured on"     , value = "{}".format(member.created_at.strftime("%d/%m/%Y"))  , inline = True)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="Just for fun. your data is never touched by us")
        
        a=await ctx.send(embed=emcon)
        await sleep(1)
        await a.edit(embed=emcon1)
        await sleep(1)
        await a.edit(embed=emcon2)
        await sleep(1)
        await a.edit(embed=emcon3)
        await sleep(2)
        await a.edit(embed=emcon4)
        await sleep(2)
        await a.edit(embed=emcon5)
        await sleep(3)
        await a.edit(embed=emcon6)
        await sleep(1)
        await a.edit(embed=emcon7)
        await sleep(1)
        await a.edit(embed=emcon8)
        await sleep(1)
        await a.edit(embed=emcon9)
        await sleep(1)
        await a.edit(embed=emcon10)
        await sleep(1)
        await a.edit(embed=emcon11)
        await sleep(1)
        await a.edit(embed=emcon12)
        await sleep(3)

        await a.edit(embed=emcon26)
        await a.edit(embed=emcon27)
        await a.edit(embed=emcon13)
        await sleep(2)

        await a.edit(embed=emcon14)
        await sleep(1)
        await a.edit(embed=emcon15)
        await sleep(1)
        await a.edit(embed=emcon16)
        await sleep(2)
        await a.edit(embed=emcon17)
        await sleep(1)
        await a.edit(embed=emcon18)
        await sleep(1)
        await a.edit(embed=emcon19)
        await sleep(2)
        await a.edit(embed=emcon20)
        await sleep(2)
        await a.edit(embed=emcon21)
        await sleep(2)
        await a.edit(embed=emcon22)
        await sleep(3)
        await a.edit(embed=emcon23)
        await sleep(3)
        await a.edit(embed=emcon24)
        await sleep(2)
        await a.edit(embed=emcon25)
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(hacker(client)) 
