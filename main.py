import os
import discord
import asyncio
import aiocron
from cogs.av import avatar 
import cogs.help
#from dotenv import load_dotenv
from discord.ext.commands import * 
from discord.ext import commands
#from discord.flags import Intents
from datetime import datetime
from cogs.autoreport import report
from cogs.quotes import todaysquotes
from alive import keep_alive
#from exception import mod


##############################################   Client Section ##############################################

intents=discord.Intents.all()
client=commands.Bot(command_prefix='-',intents=intents)
client.remove_command('help')

##############################################   Error handling   ##############################################

@client.event 
async def on_command_error(ctx,error):
 if isinstance(error,commands.CommandOnCooldown):
   msg = "*Slow it down bruh!\n{} Go get a coffee*\n**Command cooldown, releasing in {:.2f}s**".format(ctx.author.mention,error.retry_after)
   await ctx.reply(msg)

 elif isinstance(error, MissingPermissions):
    await ctx.reply("**you don't have proper privilege to execute this operation\nkindly contact server administrator**")

 elif isinstance(error, commands.BotMissingPermissions):
    emcon=discord.Embed(title = "Missing Permissions", value = "Requesting Permission",colour=discord.Colour.orange(),timestamp=datetime.utcnow())
    emcon.add_field(name = "status"      , value="Permissions error in execueting specific commands. kindly grant me required permissions to execute operations")
    emcon.add_field(name = "Server Name" , value="{}".format(ctx.guild.name))
    emcon.add_field(name = "Server ID"   , value="{}".format(ctx.guild.id))
    emcon.add_field(name = "Permission Required" , value="{}".format(error))
    emcon.set_footer(text="https://bit.ly/mrthebott")
    await ctx.guild.owner.send(embed=emcon)
 
 elif isinstance(error, BadArgument):
    await ctx.reply("*It seems you have mentioned wrong/invalid argument. kindly recheck your command*")

##############################################   On Ready ##############################################

@client.event
async def on_ready():
  print("Ready to rock and Roll!")

##############################################   DailyQuotes at UTC 00:00   ##############################################

@aiocron.crontab('30 18 * * *')
async def dailyquotes():
        """
        await client.wait_until_ready()
        guild = client.get_guild(868390640944300032)
        mod_log_channel = client.get_channel(869200831717736478)
        remove = discord.utils.get(guild.roles, id=899331881370271774)
        for x in guild.members:
            await x.remove_roles(remove)
        await mod_log_channel.send("Resetted <@&899331881370271774>  Role Successfully!!!")
        """
        tquote,tauthor=todaysquotes()
        f=open('channel.txt','r')
        channel_lines = f.readlines()
        log=client.get_channel(875690555621924864)
        channel_main = client.get_channel(904422414870511616)
        channel_murali = client.get_channel(872722629050638376)
        embed = discord.Embed(title = "Quote Of The Day!!!", description = f"{tquote} \t -{tauthor}", colour=discord.Colour.blue(),timestamp=datetime.utcnow())
        embed.set_footer(text="https://bit.ly/mrthebott")
        embed.set_thumbnail(url="https://media.istockphoto.com/photos/speech-bubble-on-blue-background-picture-id1009861190?b=1&k=20&m=1009861190&s=170667a&w=0&h=-gATf7bn0aGMv0Bfu7kh2oCOYV7YJBt0xJV72xLwwBw=")
        emcon = discord.Embed(title = "Quote Of The Day!!!", description = f"{tquote} \t -{tauthor}", colour=discord.Colour.blue(),timestamp=datetime.utcnow())
        emcon.set_footer(text="https://bit.ly/mrthebott")
        emcon.set_thumbnail(url="https://media.istockphoto.com/photos/speech-bubble-on-blue-background-picture-id1009861190?b=1&k=20&m=1009861190&s=170667a&w=0&h=-gATf7bn0aGMv0Bfu7kh2oCOYV7YJBt0xJV72xLwwBw=")
        v=await channel_main.send("<@&871748415179071579>",embed=embed)
        if v:
            head=discord.Embed(title = "Starting Validation",color=discord.Colour.orange(),timestamp=datetime.utcnow())
            await log.send(embed=head)

        for x in channel_lines:
            channel_2 = client.get_channel(int(x))
            try:
                embed = discord.Embed(title = "Quote Of The Day!!!", description = f"{tquote} \t -{tauthor}", colour=discord.Colour.blue(),timestamp=datetime.utcnow())
                embed.set_footer(text="https://bit.ly/mrthebott")
                embed.set_thumbnail(url="https://media.istockphoto.com/photos/speech-bubble-on-blue-background-picture-id1009861190?b=1&k=20&m=1009861190&s=170667a&w=0&h=-gATf7bn0aGMv0Bfu7kh2oCOYV7YJBt0xJV72xLwwBw=")
                await asyncio.sleep(7)
                verify=await channel_2.send(embed=embed)
                if verify:
                    await log.send("Quote Of The Day has been successfully send to {}".format(x))
                if not channel_2:
                    await log.send("**<@QOT channel id: {} is no longer valid. Can be removed.**".format(x))
                if not verify:
                    await log.send("***Critical Error..***")
                    await log.send("**Auto report service triggered**")
                    server_name="MR.Bot Lobby"
                    channel_name=channel_2.name
                    channel_id="{}".format(x)
                    author="NULL"
                    author_id="NULL"
                    message_content="QOT"
                    status="504"
                    message_id="NULL"
                    rep_by="Validation"
                    await log.send(embed=report(client,server_name,channel_name,channel_id,author,author_id,message_content,status,message_id,rep_by).autoreport())

            except:
                pass
        await asyncio.sleep(6)
        await channel_murali.send("<@&872722625699389470>",embed=embed)


##############################################   Cogs   ##############################################
for x in os.listdir('./cogs'):
    if x.endswith('.py'):
        client.load_extension(f'cogs.{x[:-3]}')

##############################################   Token   ##############################################   
keep_alive()
#load_dotenv()
#dingding= os.environ['.env']
client.run("") #mrbot