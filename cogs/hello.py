import discord,discord.ext,random
from discord.ext import commands
from discord.ext.commands import Cog

rate=5
time=60
welcome = ["boo!","there!","mate","Howdy, howdy ,howdy!","partner!","sunshine!","It only takes a minute to say 'Hello', but it can make a big difference in someones day!","Saying hello doesn't have an ROI. It's about building relationships","If you're brave enough to say goodbye, life will reward you with a new hello.","I want to be your favorite hello and hardest goodbye","hi there","Whats up!","buddy!","how was your day!","buddy! Just felt like sharing a smile with you today","Whats special!","How are you?","Hope you are doing great!","A little note to say hello and let you know I care.","Just a note to say hello and wish that you have good times to come your way.","The two hardest things to say in life are hello for the first time and goodbye for the last","I know you are busy. It is good to be busy, but do say hello once in a while.","Are pigs flying? I haven't heard from you in a while. Hello!","Just to let you know that you can call from an iPhone to an Android. Hello!","When I stop thinking about you, I start missing you. When are we catching up?","Dont scold me my developer made me like this."]


class hello(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Hello Ready - cooldown {}/{}".format(rate,time))
    """
    @Cog.listener()
    async def on_message(self,message):
        if message.guild.id == 868390640944300032:
            lower=message.content.lower()
            if lower.startswith("hello") or lower.startswith("hi") or lower.startswith("hai"):
                await message.channel.send('{} hello,{}'.format(message.author.mention,random.choice(welcome)))
    """   
            
    @commands.command(aliases=["hai","hi","haii","haiii"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def hello(self,ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else :
            async with ctx.message.channel.typing():
                pass
            await ctx.send('{} hello,{}'.format(ctx.author.mention,random.choice(welcome)))

def setup(client):
    client.add_cog(hello(client))