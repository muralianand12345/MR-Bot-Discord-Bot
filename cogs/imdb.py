import cogs.autoreport,discord,requests
from cogs.autoreport import report
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime, time

rate=5
time=60

class movie(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("IMDb command Ready! - cooldown {}/{}".format(rate,time))
    
    @commands.command(aliases=["rating","find","movie"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def imdb(self,ctx,*,search=None):
        if not search:
            await ctx.reply("**Please provide a search query. check //help imdb for more.**")
        else:
            try: 
                url = "https://imdb8.p.rapidapi.com/auto-complete"
                querystring = {"q":"{}".format(search)}
                headers = {
                'x-rapidapi-host': "imdb8.p.rapidapi.com",
                'x-rapidapi-key': "c84d2547b6mshad464c105d1312ap1924acjsn76dd4c7120be"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)

                data=response.json()
                tot=len(data["d"])
                title=data["d"][0]["l"]
                type=data["d"][0]["q"]
                rank=data["d"][0]["rank"]
                art=data["d"][0]["s"]
                year=data["d"][0]["y"]

                emcon=discord.Embed(title="IMDB - {}".format(search),description="Displaying 1 Of {} Results...".format(tot),colour=discord.Colour.green())
                emcon.add_field(name="Title", value="{}".format(title))
                emcon.add_field(name="Type" , value="{}".format(type))
                emcon.add_field(name="Actor/Singer", value="{}".format(art), inline=False)
                emcon.add_field(name="Rank",value="{}".format(rank))
                emcon.add_field(name="Year Released", value="{}".format(year))
                emcon.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/1200px-IMDB_Logo_2016.svg.png")
                emcon.set_footer(text="https://bit.ly/mrthebot")
                await ctx.send("{}".format(ctx.author.mention),embed=emcon)
            except:
                await ctx.reply("**oops!, could'nt find your search!!!. Issue?? Feel Free to report. //report < isuue >**")

def setup(client):
    client.add_cog(movie(client))