from operator import mod
import discord
import discord.ext
import json
import asyncio
from cogs.autoreport import report
from discord.utils import get 
from discord.ext import commands
from discord.ext.commands import Cog,has_guild_permissions
from datetime import datetime, time
from exception import mod

rate=5
time=60

class mute(Cog):
    def __init__(self,client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print("Mute Command Ready! - cooldown {}/{}".format(rate,time))
        
    @commands.command(aliases=["mute"])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    #@commands.has_any_role(868391773909684294,868391776329805886,868391773213442088)
    @commands.bot_has_permissions(manage_roles=True,embed_links=True)
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def suspend(self,ctx, member: discord.Member=None, time=None, *,reason=None):
        
       if not member:
           await ctx.reply("Hello mod, You have'nt mentioned anyone to mute it seems. Wanna mute everyone? If i do so my developer will drive a stake through my heart.")
           return 
    
       if member.guild_permissions.manage_messages and ctx.author.guild_permissions.administrator:
        await ctx.reply("***Warning you are muting a mod***")
         
        if not time:
            reason = "None"
            muted = get(ctx.guild.roles, name="Muted")
            if not muted:
                muted = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            await member.add_roles(muted, reason=reason)
            with open ("/home/runner/Bot/report.json") as file:
                data=json.load(file)
                suspend_num=int(data["suspend_no"])
                suspend_num+=1
            data["suspend_no"]=int(suspend_num)
            with open ("/home/runner/Bot/report.json","w") as f:
                 json.dump(data,f)

            muted_embed = discord.Embed(title=f"Case No: '#{suspend_num}'",description = "Suspended user {} by {}".format(member.mention,ctx.author.mention),colour=discord.Colour.orange(),timestamp=datetime.utcnow())
            muted_embed.add_field(name = "Case No"      ,value = "{}".format(suspend_num))
            muted_embed.add_field(name = "Reason"       ,value = "{}".format(reason)     )
            muted_embed.add_field(name = "Duration"     ,value = "until unmutes")
            muted_embed.set_footer(text= "Think made a mistake?. Feel free to raise a ticket.**-ticket**")
            if ctx.guild.id == 868390640944300032:
                mod_log = discord.Embed(title=f"Case No: '#{suspend_num}'",description = "Suspended user {} by {}".format(member.mention,ctx.author.mention),colour=discord.Colour.orange(),timestamp=datetime.utcnow())
                mod_log.add_field(name = "Case No"         ,value="{}".format(suspend_num))
                mod_log.add_field(name = "Reason"          ,value="{}".format(reason)             ,inline = False)
                mod_log.add_field(name = "Duration"        ,value="Auto lifted at 00:00 UTC"               ,inline = False)
                mod_log.add_field(name = "Suspended In"    ,value="{}".format(ctx.channel.name)   ,inline = False)
                mod_log.add_field(name = "User ID"         ,value="{}".format(member.id)          ,inline = True)
                mod_log.add_field(name = "Channel ID"      ,value="{}".format(ctx.channel.id)     ,inline = True)
                mod_log_channel = self.client.get_channel(869200831717736478)
                await mod_log_channel.send(embed=mod_log)
            await ctx.send(embed=muted_embed)

        else:
            if not reason:
                await ctx.reply("Proceeding without reason")
                reason = "No reason specified"
            try:
                
                seconds = time[:-1]
                sec = int(seconds)
                dur = time[-1]
                dur=dur.lower()            
                if dur == "s" or dur == "sec" or dur == "seconds":
                    sec = sec * 1
                elif dur == "m" or dur == "min" or dur == "minute" or dur == "minutes":
                    sec = sec * 60
                elif dur == "h" or dur == "hour" or dur == "hours":
                    sec = sec * 60 * 60
                elif dur == "d" or dur == "days" or dur =="day":
                    sec = sec * 86400
                else:
                    await ctx.reply("You have specified some duration which i could'nt even find in google. R u from any other planet??\nI accept durations s/m/h/d only ")
                    return 
            except Exception as e:
                await ctx.reply("oops!, I accept durations s/m/h/d  😂😂😂 ")
                return 
  
            muted = get(ctx.guild.roles, name="Muted")
            if not muted:
                muted = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                  await channel.set_permissions(muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            
  
            await member.add_roles(muted, reason=reason)
            with open ("/home/runner/Bot/report.json") as file:
                data=json.load(file)
                suspend_num=int(data["suspend_no"])
                suspend_num+=1
            data["suspend_no"]=int(suspend_num)
            with open ("/home/runner/Bot/report.json","w") as f:
                json.dump(data,f)

            muted_embed = discord.Embed(title=f"Case No:'#{suspend_num}'",description = "Suspended user {} by {}".format(member.mention,ctx.author.mention),colour=discord.Colour.orange(),timestamp=datetime.utcnow())
            muted_embed.add_field(name = "Reason"       ,value="{}".format(reason)             ,inline = False)
            muted_embed.add_field(name = "Duration"     ,value="{}".format(time)               ,inline = False)
            muted_embed.set_footer(text= "Think made a mistake?. Feel free to raise a ticket.**-ticket**")
            if ctx.guild.id == 868390640944300032:
                
                mod_log = discord.Embed(title=f"Case No:'#{suspend_num}'",description = "Suspended user {} by {}".format(member.mention,ctx.author.mention),colour=discord.Colour.orange(),timestamp=datetime.utcnow())
                mod_log.add_field(name = "Reason"          ,value="{}".format(reason)             ,inline = False)
                mod_log.add_field(name = "Duration"        ,value="{}".format(time)               ,inline = False)
                mod_log.add_field(name = "Suspended In"    ,value="{}".format(ctx.channel.name)   ,inline = False)
                mod_log.add_field(name = "User ID"         ,value="{}".format(member.id)          ,inline = True)
                mod_log.add_field(name = "Channel ID"      ,value="{}".format(ctx.channel.id)     ,inline = True)
                mod_log_channel = self.client.get_channel(869200831717736478)
                await mod_log_channel.send(embed=mod_log)
            
            await ctx.send(embed=muted_embed)
            await asyncio.sleep(sec)
            muted = get(ctx.guild.roles, name="Muted")
            target = await ctx.guild.fetch_member(int(member.id))
            if not target:
               await ctx.reply("Cant't find user. Check wheather user is still in {}".format(ctx.guild.name))
            try:
              if muted in target.roles:
                    if ctx.guild.id == 868390640944300032:
                        mod_log = discord.Embed(title=f"Unmute Details",description = "Released User {} suspended by {}".format(target.mention,ctx.author.mention),colour=discord.Colour.green(),timestamp=datetime.utcnow())
                        mod_log.add_field(name = "Reason"          ,value="{}".format(reason)             ,inline = False)
                        mod_log.add_field(name = "Duration"        ,value="{}".format(time)               ,inline = False)
                        mod_log.add_field(name = "Suspended In"    ,value="{}".format(ctx.channel.name)   ,inline = False)
                        mod_log.add_field(name = "User ID"         ,value="{}".format(member.id)          ,inline = True)
                        mod_log.add_field(name = "Channel ID"      ,value="{}".format(ctx.channel.id)     ,inline = True)
                        mod_log_channel = self.client.get_channel(869200831717736478)
                        await mod_log_channel.send(embed=mod_log)
                    
                    embed = discord.Embed(title="Unmute Details ",description = "Released user {} Successfully!".format(target.mention),colour=discord.Colour.green(),timestamp=datetime.utcnow())
                    embed.add_field(name = "Suspended By" ,value = "{}".format(ctx.author.mention) ,inline = False)
                    embed.add_field(name = "Reason"       ,value = "{}".format(reason)             ,inline = False)
                    embed.add_field(name = "Duration"     ,value = "{}".format(time)               ,inline = True)
                    embed.add_field(name = "Method"       ,value = "Automatic lift"                ,inline = True)
                    embed.set_footer(text= "Think made a mistake?. Feel free to raise a ticket.**-ticket**")
                    await member.remove_roles(muted)
                    await ctx.channel.send(embed=embed)
                    
            except:
                await ctx.reply("Error occured **Auto report service has been Triggered")
                server_name=ctx.guild.name 
                author=ctx.author.name
                author_id=ctx.author.id
                channel_name=ctx.channel.name 
                channel_id=ctx.channel.id
                status_code="No status"
                message_content=ctx.message.content
                message_id=ctx.message.id
                rep_by="suspend command"
                chn = self.client.get_channel(875690555621924864)
                await chn.send(embed=(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())
                await ctx.send(enbed=(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())


       elif member.guild_permissions.manage_messages and ctx.author.guild_permissions.manage_messages:
            await ctx.reply("***You cant mute a mod***")
            return
###################################################################  user  mute ##################################################################

       else:
        if not time:
            reason = "None"
            muted = get(ctx.guild.roles, name="Muted")
            if not muted:
                muted = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            await member.add_roles(muted, reason=reason)
            with open ("/home/runner/Bot/report.json") as file:
                data=json.load(file)
                suspend_num=int(data["suspend_no"])
                suspend_num+=1
            data["suspend_no"]=int(suspend_num)
            with open ("home/runner/Bot/report.json","w") as f:
                 json.dump(data,f)

            muted_embed = discord.Embed(title=f"Case No: '#{suspend_num}'",description = "Suspended user {} by {}".format(member.mention,ctx.author.mention),colour=discord.Colour.orange(),timestamp=datetime.utcnow())
            muted_embed.add_field(name = "Case No"      ,value = "{}".format(suspend_num))
            muted_embed.add_field(name = "Reason"       ,value = "{}".format(reason)     )
            muted_embed.add_field(name = "Duration"     ,value = "until unmutes")
            muted_embed.set_footer(text= "Think made a mistake?. Feel free to raise a ticket.**-ticket**")
            if ctx.guild.id == 868390640944300032:
                mod_log = discord.Embed(title=f"Case No: '#{suspend_num}'",description = "Suspended user {} by {}".format(member.mention,ctx.author.mention),colour=discord.Colour.orange(),timestamp=datetime.utcnow())
                mod_log.add_field(name = "Case No"         ,value="{}".format(suspend_num))
                mod_log.add_field(name = "Reason"          ,value="{}".format(reason)             ,inline = False)
                mod_log.add_field(name = "Duration"        ,value="Until unmutes"                 ,inline = False)
                mod_log.add_field(name = "Suspended In"    ,value="{}".format(ctx.channel.name)   ,inline = False)
                mod_log.add_field(name = "User ID"         ,value="{}".format(member.id)          ,inline = True)
                mod_log.add_field(name = "Channel ID"      ,value="{}".format(ctx.channel.id)     ,inline = True)
                mod_log_channel = self.client.get_channel(869200831717736478)
                await mod_log_channel.send(embed=mod_log)
            await ctx.send(embed=muted_embed)

        else:
            if not reason:
                await ctx.reply("Proceeding without reason")
                reason = "No reason specified"
            try:
                
                seconds = time[:-1]
                sec = int(seconds)
                dur = time[-1]
                dur = dur.lower()
                if dur == "s" or dur == "sec" or dur == "seconds":
                    sec = sec * 1
                elif dur == "m" or dur == "min" or dur == "minute" or dur == "minutes":
                    sec = sec * 60
                elif dur == "h" or dur == "hour" or dur == "hours":
                    sec = sec * 60 * 60
                elif dur == "d" or dur == "days" or dur =="day":
                    sec = sec * 86400

                else:
                    await ctx.reply("You have specified some duration which i could'nt even find in google. R u from any other planet??\nI accept durations s/m/h/d only ")
                    return 
            except Exception as e:
                await ctx.reply("oops!, I tried searching all over internet but i could'nt find the time you specified. Iam trying to say that time specified is invalid. 😂😂😂 ")
                return 
  
            muted = get(ctx.guild.roles, name="Muted")
            if not muted:
                muted = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                  await channel.set_permissions(muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            
  
            await member.add_roles(muted, reason=reason)
            with open ("/home/runner/Bot/report.json") as file:
                data=json.load(file)
                suspend_num=int(data["suspend_no"])
                suspend_num+=1
            data["suspend_no"]=int(suspend_num)
            with open ("/home/runner/Bot/report.json","w") as f:
                json.dump(data,f)

            muted_embed = discord.Embed(title=f"Case No:'#{suspend_num}'",description = "Suspended user {} by {}".format(member.mention,ctx.author.mention),colour=discord.Colour.orange(),timestamp=datetime.utcnow())
            muted_embed.add_field(name = "Reason"       ,value="{}".format(reason)             ,inline = False)
            muted_embed.add_field(name = "Duration"     ,value="{}".format(time)               ,inline = False)
            muted_embed.set_footer(text= "Think made a mistake?. Feel free to raise a ticket.**-ticket**")
            if ctx.guild.id == 868390640944300032:
                
                mod_log = discord.Embed(title=f"Case No:'#{suspend_num}'",description = "Suspended user {} by {}".format(member.mention,ctx.author.mention),colour=discord.Colour.orange(),timestamp=datetime.utcnow())
                mod_log.add_field(name = "Reason"          ,value="{}".format(reason)             ,inline = False)
                mod_log.add_field(name = "Duration"        ,value="{}".format(time)               ,inline = False)
                mod_log.add_field(name = "Suspended In"    ,value="{}".format(ctx.channel.name)   ,inline = False)
                mod_log.add_field(name = "User ID"         ,value="{}".format(member.id)          ,inline = True)
                mod_log.add_field(name = "Channel ID"      ,value="{}".format(ctx.channel.id)     ,inline = True)
                mod_log_channel = self.client.get_channel(869200831717736478)
                await mod_log_channel.send(embed=mod_log)
            
            await ctx.send(embed=muted_embed)
            await asyncio.sleep(sec)
            muted = get(ctx.guild.roles, name="Muted")
            target = await ctx.guild.fetch_member(int(member.id))
            if not target:
               await ctx.reply("Cant't find user. Check wheather user is still in {}".format(ctx.guild.name))
            try:
              if muted in target.roles:
                    if ctx.guild.id == 868390640944300032:
                        mod_log = discord.Embed(title=f"Unmute Details",description = "Released User {} suspended by {}".format(target.mention,ctx.author.mention),colour=discord.Colour.green(),timestamp=datetime.utcnow())
                        mod_log.add_field(name = "Reason"          ,value="{}".format(reason)             ,inline = False)
                        mod_log.add_field(name = "Duration"        ,value="{}".format(time)               ,inline = False)
                        mod_log.add_field(name = "Suspended In"    ,value="{}".format(ctx.channel.name)   ,inline = False)
                        mod_log.add_field(name = "User ID"         ,value="{}".format(member.id)          ,inline = True)
                        mod_log.add_field(name = "Channel ID"      ,value="{}".format(ctx.channel.id)     ,inline = True)
                        mod_log_channel = self.client.get_channel(869200831717736478)
                        await mod_log_channel.send(embed=mod_log)
                    
                    embed = discord.Embed(title="Unmute Details",description="Released user {} Successfully!".format(target.mention),colour=discord.Colour.green(),timestamp=datetime.utcnow())
                    embed.add_field(name = "Suspended By" ,value = "{}".format(ctx.author.mention) ,inline = False)
                    embed.add_field(name = "Reason"       ,value = "{}".format(reason)             ,inline = False)
                    embed.add_field(name = "Duration"     ,value = "{}".format(time)               ,inline = True)
                    embed.add_field(name = "Method"       ,value = "Automatic lift"                ,inline = True)
                    embed.set_footer(text= "Think made a mistake?. Feel free to raise a ticket.**-ticket**")
                    await member.remove_roles(muted)
                    await ctx.channel.send(embed=embed)
                    
            except:
                await ctx.reply("Error occured **Auto report service has been Triggered")
                server_name=ctx.guild.name 
                author=ctx.author.name
                author_id=ctx.author.id
                channel_name=ctx.channel.name 
                channel_id=ctx.channel.id
                status_code="No status"
                message_content=ctx.message.content
                message_id=ctx.message.id
                rep_by="suspend command"
                chn = self.client.get_channel(875690555621924864)
                await chn.send(embed=(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())
                await ctx.send(enbed=(self.client,server_name,channel_name,channel_id,author,author_id,message_content,status_code,message_id,rep_by).autoreport())


    
def setup(client):
    client.add_cog(mute(client))
