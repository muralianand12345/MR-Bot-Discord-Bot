import discord
import discord.ext
import random
import requests
from discord.ext import commands
from discord.ext.commands import Cog
from datetime import datetime
from cogs.autoreport import report

rate=5
time=60

class weather(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Weather command Ready - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["w","wet","wr"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def weather(self,ctx,*,city=None):
        if city == None:
            await ctx.reply("Please provide a city to get weather report")
        else:
            loc = city
            api = ['61efa4b9e592ffa98d8df76ce0da3a4f','f34a1fb82c344f95c666479bea986884','bf5026fdfc56d95fc10c014435f6c45f']
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(loc,random.choice(api))
            response = requests.get(url)
            data = response.json()
            status = data['cod']
            
        if status == 200:
            #async with ctx.message.channel.typing(): 
            city_name = data['name']
            city_description = data['weather'][0]['description']
            city_temp = data['main']['temp']
            city_temp_cel = str(round(city_temp - 273.15))
            city_min_temp = data['main']['temp_min']
            city_max_temp = data['main']['temp_max']
            city_humidity = data['main']['humidity']
            city_lat = data['coord']['lat']
            city_lon = data['coord']['lon']
            city_visibility = data['visibility']
            city_wind = data['wind']['speed']
        
            embed = discord.Embed(title="Weather report of {}".format(city_name),color=discord.Colour.green(),timestamp=datetime.utcnow())
            embed.add_field( name = "Description" , value = "**{}**".format(city_description)         , inline=False)
            embed.add_field( name = "Temperature (C)" , value = "**{}**".format(city_temp_cel)            , inline=False)
            embed.add_field( name = "Humidity (%)"    , value = "**{}**".format(city_humidity)            , inline=False)
            embed.add_field( name = "Coordinates" , value = "**{}**,**{}**".format(city_lat,city_lon) , inline=False)
            embed.add_field( name = "visibility"  , value = "**{}**".format(city_visibility)          , inline=False)
            embed.add_field( name = "Wind (km/h)"        , value = "**{}**".format(city_wind)                , inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text="Requested by {}".format(ctx.author.name))
            #send = await ctx.send(embed=embed)
            async with ctx.message.channel.typing():
                pass
            await ctx.send(embed=embed) 
        
        elif status == '404':
            async with ctx.message.channel.typing():
                pass
            await ctx.reply("City not found")
            
        
        else:
            await ctx.reply("Error code : {} **starting auto report service**".format(status))
            server_name=ctx.guild.name 
            author=ctx.author.name
            author_id=ctx.author.id
            channel_name=ctx.channel.name 
            channel_id=ctx.channel.id
            message_content=ctx.message.content
            status_code=status
            message_id=ctx.message.id
            rep_by="ss command"
            chn = self.client.get_channel(875690555621924864)
            await chn.send(embed=report(server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())
            await ctx.send(embed=report(server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())
def setup(client):
    client.add_cog(weather(client))
