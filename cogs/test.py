import aiocron
import cogs.autoreport
import discord
from cogs.autoreport import report
from discord.ext.commands import Cog
from discord.ext import commands
from cogs.quotes import todaysquotes

tquote,tauthor=todaysquotes()

class test(Cog):
    def __init__(self,client):
        self.client=client
        self.tquote=tquote
        self.tauthor=tauthor

    @Cog.listener()
    async def on_ready(self):
        print("Test ready")
    
    @commands.command()
    async def test(self,ctx):

            status="404"

            server_name=ctx.guild.name

            author=ctx.author.name

            author_id=ctx.author.id

            channel_name=ctx.channel.name

            channel_id=ctx.channel.id

            message_content=ctx.message.content

            status_code=status

            message_id=ctx.message.id

            rep_by="ticket command"

            chn = self.client.get_channel(875690555621924864)
            print("chn")
            await ctx.send(embed=report(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())



def setup(client):
    client.add_cog(test(client))
    
