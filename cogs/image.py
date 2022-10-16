import discord,requests
from discord.ext import commands
from discord.utils import get
import discord.ext.commands
from datetime import datetime
from discord.ext.commands import Cog
rate=5
time=60

class image(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Image command Ready! - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["img"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def image(self,ctx,*,ser=None):
        if not ser:
            await ctx.reply("**oops!, please specify image to search**")
        else:
            url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"
            querystring = {"q":"{}".format(ser),"pageNumber":"1","pageSize":"1","autoCorrect":"true","safeSearch":"true"}
            headers = {
            'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
            'x-rapidapi-key': "c84d2547b6mshad464c105d1312ap1924acjsn76dd4c7120be"
            }
            print("After header")
            response = requests.request("GET", url, headers=headers, params=querystring)
            res = response.json()
            tar=res['value'][0]['url']
            if ctx.guild.id == 868390640944300032:
                await ctx.reply("**{} Please use ~image command**".format(ctx.author.mention))
            else:
                await ctx.reply("{}".format(tar))
    
def setup(client):
    client.add_cog(image(client))