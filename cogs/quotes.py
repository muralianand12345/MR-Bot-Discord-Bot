from os import name
import discord,discord.ext,json,requests
from datetime import datetime
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands import Cog
rate=5
time=30

def randomquotes():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    rquote = data[0]['q']
    rauthor = data[0]['a']
    return rquote,rauthor

def todaysquotes():
    response = requests.get("https://zenquotes.io/api/today")
    data = json.loads(response.text)
    tquote = data[0]['q']
    tauthor = data[0]['a']    
    return tquote,tauthor 

class quotes(Cog):
    def __init__(self,client):
        self.client=client
        
    @Cog.listener()
    async def on_ready(self):
        print("Quotes Command Ready - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["rquote","quote","i","ins"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def inspire(self,ctx):
        chn=ctx.message.channel
        async with chn.typing():
            rquote,rauthor=randomquotes()
            emcon=discord.Embed(title="Quodophile",color=discord.Colour.blue(),timestamp=datetime.utcnow())
            emcon.add_field(name="Your Quote Is Here".format(ctx.author.mention),value="{}".format(rquote))
            emcon.add_field(name="Author",value="{}".format(rauthor))
            emcon.add_field(name="status",value="Requested by {}".format(ctx.author.mention),inline=False)
            file = discord.File("/home/runner/Bot/cogs/rq.jpg",filename="rq.jpeg")
            emcon.set_image(url="attachment://rq.jpeg")
            await ctx.send(file=file,embed=emcon)

    @commands.command(aliases=["it","inst","dq","tq","quo","quodophile","qp","tquote"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def inspiretoday(self,ctx):
            chn=ctx.message.channel
            async with chn.typing():
                pass
            tquote,tauthor=todaysquotes()
            emcon=discord.Embed(title="Quote Of The Day!!!",color=discord.Colour.blue(),timestamp=datetime.utcnow())
            emcon.add_field(name="Your Quote Is Here".format(ctx.author.mention),value="{}".format(tquote))
            emcon.add_field(name="Author",value="{}".format(tauthor))
            emcon.add_field(name="status",value="Requested by {}".format(ctx.author.mention),inline=False)
            emcon.set_image(url="https://st2.depositphotos.com/3680349/8294/v/600/depositphotos_82946422-stock-illustration-believe-in-yourself-typography-poster.jpg")
            await ctx.send(embed=emcon)
            

def setup(client):
    client.add_cog(quotes(client))
