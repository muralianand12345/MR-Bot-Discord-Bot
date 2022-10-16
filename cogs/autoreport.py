import discord
from discord.ext.commands import Cog
class report(Cog): 
    def __init__(self,client,server_name,channel_name,channel_id,author,author_id,message_content,status,message_id,rep_by):
        self.client=client
        self.server_name=server_name
        self.channel_name=channel_name
        self.channel_id=channel_id
        self.author=author
        self.author_id=author_id
        self.message_content=message_content 
        self.status=status 
        self.message_id=message_id 
        self.rep_by=rep_by

    @Cog.listener()
    async def on_ready(self):
        print("Autoreport Service Ready!")
    
    def autoreport(self):
        
        problem = discord.Embed(title = "Automatic Report Service On Duty  - Fatal Error",colour=discord.Colour.red())
        problem.add_field(name = "Server"         ,value = "{}".format(self.server_name)     )
        problem.add_field(name = "channel name"   ,value = "{}".format(self.channel_name)    )
        problem.add_field(name = "channel id"     ,value = "{}".format(self.channel_id)      )
        problem.add_field(name = "Author name"    ,value = "{}".format(self.author)          )
        problem.add_field(name = "author id"      ,value = "{}".format(self.author_id)       )
        problem.add_field(name = "message content",value = "{}".format(self.message_content) )
        problem.add_field(name = "Status Code"    ,value = "{}".format(self.status)          )
        problem.add_field(name = "Message id"     ,value = "{}".format(self.message_id)      )
        problem.add_field(name = "reported in"    ,value = "{}".format(self.rep_by)          )
        problem.set_footer(text = "your error has been successfully reported to developer\nIn case not fixed kindly report mannually using '-report'command")
        return problem

def setup(client):
    client.add_cog(report(client,server_name=None,channel_name=None,channel_id=None,author=None,author_id=None,message_content=None,status=None,message_id=None,rep_by=None))
