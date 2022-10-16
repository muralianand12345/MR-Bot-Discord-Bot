import cogs.autoreport,discord,requests
from cogs.autoreport import report
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime

rate=5
time=60

class songinfo(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Song Info Command Ready! - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["lyric","lyrics","songl","song","songlyric"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def ss(self,ctx,*,query=None):
        if not query:
            await ctx.reply("please specify song name.")
        else:
            url_search = "https://genius.p.rapidapi.com/search"
            querystring = {"q":"{}".format(query)}
            
            headers = {
                'x-rapidapi-host': "genius.p.rapidapi.com",
                'x-rapidapi-key': "c84d2547b6mshad464c105d1312ap1924acjsn76dd4c7120be"
            }

            response = requests.request("GET", url_search, headers=headers, params=querystring)
            res = response.json()
            status=res['meta']['status']
            if status == 200:
                try:
                    title=res['response']['hits'][0]['result']['full_title']
                    thumbnail = res['response']['hits'][0]['result']['header_image_thumbnail_url']
                    url = res['response']['hits'][0]['result']['url']
                    id = res['response']['hits'][0]['result']['id']
                    artist_name = res['response']['hits'][0]['result']['primary_artist']['name']
                
                    url_song = "https://genius.p.rapidapi.com/songs/{}".format(id)
                    headers = {
                    'x-rapidapi-host': "genius.p.rapidapi.com",
                    'x-rapidapi-key': "c84d2547b6mshad464c105d1312ap1924acjsn76dd4c7120be"
                    }

                    resp = requests.request("GET", url_song, headers=headers)
                    res_1=resp.json()
                    media= res_1['response']['song']['media'][0]['url']

                    embed = discord.Embed(title="Song Details",colour=discord.Colour.gold())
                    embed.add_field(name="Title",value="{}".format(title))
                    embed.add_field(name="Artist",value="{}".format(artist_name))
                    embed.add_field(name="Lyrics",value="{}".format(url),inline=False)
                    embed.add_field(name="Song",value="{}".format(media))
                    embed.set_thumbnail(url=thumbnail)
                    embed.set_footer(text="https://bit.ly/mrthebott")
                    await ctx.send(embed=embed)
                except:
                    embed=discord.Embed(title="Oops, Song not found 😿 😿",Colour=discord.Colour.red())
                    file = discord.File("/home/kali/pythonbot/download.jpeg",filename="cat.jpeg")
                    embed.set_footer(text="https://bit.ly/mrthebot")
                    embed.set_thumbnail(url="attachment://cat.jpeg")
                    await ctx.reply(file=file,embed=embed)
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
                await chn.send(embed=report(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())   
                await ctx.send(embed=report(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())   

def setup(client):
    client.add_cog(songinfo(client))
