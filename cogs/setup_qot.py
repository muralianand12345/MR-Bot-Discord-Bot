import discord
from discord.ext import commands
from discord.utils import get 
from discord.ext.commands import has_permissions,Cog
from discord.ext.commands.core import bot_has_guild_permissions, bot_has_permissions
from cogs.quotes import todaysquotes
rate=1
time=3600

tquote,tauthor=todaysquotes()

class setupqot(Cog):
    def __init__(self,client):
        self.client=client
        self.tquote=tquote
        self.tauthor=tauthor
    
    @Cog.listener()
    async def on_ready(self):
        print("QOT setup command Ready!!! - cooldown {}/{}".format(rate,time))
    
    @commands.command(aliases=["qot"])
    @commands.guild_only()
    @has_permissions(administrator=True)
    @bot_has_permissions(manage_roles=True,manage_channels=True,embed_links=True,read_messages=True,send_messages=True)
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def setup(self,ctx):
        await self.client.wait_until_ready()
        await ctx.reply("Initalizing QOT Process...") 
        guild=ctx.guild 
        create_role = await guild.create_role(name="Quodophile")
        role = get(guild.roles,name="Quodophile")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True,embed_links=True),
            role: discord.PermissionOverwrite(read_messages = True , add_reactions = True , send_messages = False , use_external_emojis = True)
        }
        channel = await guild.create_text_channel('📜Quote of the day', overwrites=overwrites)
        role_file = open('role.txt','a')
        role_file.write(str(role.id))
        role_file.write('\n')
        channel = self.client.get_channel(channel.id)
        channel_file = open('channel.txt','a')
        channel_file.write(str(channel.id))
        channel_file.write('\n')
        pin = await channel.send("***Invite me in your server***\n\n 'https://bit.ly/mrthebott'")         
        embed = discord.Embed(title = "Quote Of The Day!!!", description = "{}\t{}".format(self.tquote,self.tauthor), colour=discord.Colour.blue())
        embed.add_field(name="About", value="\n\nNote this channel Quote-of-the day only visible to those who have quodophile role so kindly set up reaction roles for role-quodophile.This channel receives quote of the day at UTC 00:00(everyday)\n\nCurrently in {} servers.We are non-profital servers. Help us grow.\nInvite me in your server **https://bit.ly/mrthebott**".format(len(self.client.guilds)))
        embed.set_footer(text="Invite me in your server **https://bit.ly/mrthebott**")
        await channel.send(embed=embed)
        await ctx.send("<#{}> and role <@&{}> has been created and setted up successfully!".format(channel.id,role.id))
        

def setup(client):
    client.add_cog(setupqot(client))
