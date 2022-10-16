import discord,requests
import json
import asyncio
from cogs.autoreport import report
from discord.ext import commands
from discord.utils import get
import discord.ext.commands
from datetime import datetime
from discord.ext.commands import Cog
rate=5
time=60

class ticket(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Ticket Command Ready! - cooldown {}/{}".format(rate,time))

    
    @commands.command(aliases=["tiket","tic","raise"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    @commands.bot_has_permissions(manage_roles=True,manage_channels=True,embed_links=True)
    async def ticket(self,ctx,argv=None):
        try:
            if not argv:
                argv="new"
            lower=argv.lower()
            if lower == "new":
                guild=ctx.guild
                role=get(guild.roles,name="TICKET")
                member=ctx.author
                if not role:
                  await guild.create_role(name="TICKET")
                else:
                    with open("/home/runner/Bot/ticket.json") as file:
                        data=json.load(file)
                    ticket_no=int(data["ticket_num"])
                    ticket_no=ticket_no+1 
  
                    overwrites = {
                        guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        guild.me: discord.PermissionOverwrite(read_messages=True),
                        role: discord.PermissionOverwrite(view_channel=True,read_messages=True,send_messages=True,embed_links=True,attach_files=True,add_reactions=True,external_emojis=True,read_message_history=True,use_external_emojis=True),
                        member: discord.PermissionOverwrite(view_channel=True,read_messages=True,send_messages=True,embed_links=True,attach_files=True,add_reactions=True,external_emojis=True,read_message_history=True,use_external_emojis=True) 
                        }
                    create_channel = await guild.create_text_channel(name="Ticket-{}".format(ticket_no),overwrites=overwrites)
                    issue=discord.Embed(title="Ticket - '#{}'".format(ticket_no), description="{} Describe your issue here".format(member.mention), colour=discord.Colour.dark_magenta(),timestamp=datetime.utcnow())
                    issue.set_footer(text="https://bit.ly/mrthebott")
                    channel_new=self.client.get_channel(int(create_channel.id))
                    msg=await channel_new.send("{}".format(role.mention),embed=issue)

                    data["channel_id"].append(create_channel.id)
                    data["ticket_num"]=int(ticket_no)
                    with open("/home/runner/Bot/ticket.json","w") as f:
                        json.dump(data,f)
                    emcon=discord.Embed(title="Ticket Created",description="{} Your ticket has been created successfully".format(member.mention),colour=discord.Colour.dark_magenta(),timestamp=datetime.utcnow())
                    emcon.add_field(name="Ticket No",value="{}".format(ticket_no))
                    emcon.add_field(name="Excepted resolve within", value="1 Day")
                    await ctx.reply(embed=emcon)
  
            elif lower == "close":
                channel=ctx.channel.id
                with open("/home/runner/Bot/ticket.json") as file:
                    data=json.load(file)
                if ctx.channel.id in data["channel_id"]:
                    def check(message):
                        return message.channel == ctx.channel and message.content.lower() == "y"
                    try:
                        emcon=discord.Embed(title="Ticket closure confirmation",description="Confirm ticket closure? (y/n)",colour=discord.Colour.blurple(),timestamp=datetime.utcnow())
                        await ctx.send(embed=emcon)
                        await self.client.wait_for('message',check=check,timeout=60)
                        await ctx.send("Closing ticket in 10 seconds...")
                        await asyncio.sleep(5)
                        await ctx.send("Closing ticket in 5 seconds...")
                        await asyncio.sleep(5)
                        await ctx.channel.delete()
                        index=data["channel_id"].index(channel)
                        del data["channel_id"][index]

                        with open("~/Bot/ticket.json","w") as file:
                            json.dump(data,file)

                    except asyncio.TimeoutError:
                            emcon = discord.Embed(title="Ticket Clousure Info", description="Ticket closure aborted/failed.Please run the command again.", colour=discord.Colour.blurple())
                            await ctx.send(embed=emcon)    
        except:
            await ctx.reply("Error occured..**Triggering automatic report service**")
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
            await chn.send(embed=report(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())
            
            await ctx.send(embed=report(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())            

def setup(client):
    client.add_cog(ticket(client))

