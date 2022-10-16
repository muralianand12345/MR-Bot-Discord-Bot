import discord,discord.ext
from discord import client
from discord.ext import commands
from discord.ext.commands import Cog, context
from discord.ext.commands import Command

rate=5
time=60

class help(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Help command Ready - cooldown {}/{}".format(rate,time))

    @commands.group(invoke_without_command=True,aliases=["hm","mh","modhelp","mod","hmod","modh"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def helpmod(self,ctx):
            async with ctx.channel.typing(): 
                pass
            orange = discord.Colour.orange()
            emcon = discord.Embed( title="Help Menu", description="**Use -helpmod <command> for extended helpmod menu.**", colour = orange)
            emcon.add_field(name = "-qot"          , value = "Sets up channel for Quote-of-The-Day")
            emcon.add_field(name = "-ping"         , value = "Shows latency."                             ) #, inline=False)
            emcon.add_field(name = "-tquote"       , value = "Get quote of the day"                  ) #, inline=False)
            emcon.add_field(name = "-hello"        , value = "wave hello"                                 ) #, inline=False)
            emcon.add_field(name = "-hack"         , value = "Hacks specified user account(just for fun)" )
            emcon.add_field(name = "-rquote"       , value = "Get inspirational quotes."                      ) #, inline=False)
            emcon.add_field(name = "-weather"      , value = "Weather report of a place"                  ) #, inline=False)
            emcon.add_field(name = "-heartbeat"    , value = "Returns up time of server."                 ) #, inline=False)
            emcon.add_field(name = "-info"         , value = "Get info about users"                       ) #, inline=False)
            emcon.add_field(name = "-image"        , value = "Get images reg ur search"                   ) #, inline=False)
            emcon.add_field(name = "-server"       , value = "Get info about server"                      ) #, inline=False)
            emcon.add_field(name = "-suggest"      , value = "Suggest idea's/thought's nd make us better" ) #, inline=False)
            emcon.add_field(name = "-count"        , value = "Wanna check count of your nuclear family?"  ) #, inline=False)
            emcon.add_field(name = "-report"       , value = "Report Bug's/Issues's/Problem"              ) #, inline=False)
            emcon.add_field(name = "-av"           , value = "Get avatar of particular user/yourself"     ) #, inline=False)
            emcon.add_field(name = "-ticket"       , value = "Creates ticket support for helps/issues"    ) #, inline=False)
            emcon.add_field(name = "-searchsong"   , value = "Gets song information including lyrics"     )
            emcon.add_field(name = "-imdb"         , value = "Get imdb search results"                    ) #, inline=False)
            emcon.add_field(name = "-kick"         , value = "Kick a member from server"                  )
            emcon.add_field(name = "-ban"         , value = "Bans a member from server"                  )
            emcon.add_field(name = "-addrole(ar)"  , value = "Assign role to user"                        )
            emcon.add_field(name = "-removerole(rr)",value = "Remove role from user"                      )
            emcon.set_footer(text="https:-bit.ly/mrthebot")
            await ctx.send(embed = emcon)
            
    
    @helpmod.command(aliases=["p"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def ping(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "ping", description = "check latency of the server..", colour=discord.Colour.orange() )
            emcon.add_field(name = "**Syntax**", value = "**-ping**")
            await ctx.send(embed = emcon)
            
    @helpmod.command(aliases=["i","tquotes"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def tquote(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "Inspirational Quotes", description = "Hear inspirational and motivational quotes", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-inspire**")
            await ctx.send(embed = emcon)

    @helpmod.command(aliases=["hi","hai","haii"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def hello(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "Hello Hai Hi", description = "Wish tony a hello.", colour=discord.Colour.orange() )
            emcon.add_field(name = "**Syntax**", value = "**-hello\n-hai\n-hi**")
            await ctx.send(embed=emcon)

    @helpmod.command(aliases=["it","rquotes"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def rquote(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
          return
        else:
            emcon = discord.Embed(title = "Today's Inspirational Quotes" , description = "Hear today's motivational/inspirtional quotes", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-inspiretoday**")
            await ctx.send(embed=emcon)

    @helpmod.command(aliases=["img"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def image(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "Image" , description = "get's images from google", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**~image < image name >**")
            await ctx.send(embed=emcon)

    @helpmod.command(aliases=["wt","wet","location","loc"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def weather(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "Weather Report" , description = "Check weather report of places.", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-weather < place name >**")
            await ctx.send(embed=emcon)

    @helpmod.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def heartbeat(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "Heartbeat", description = "Shows uptime of server", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-heartbeat**")
            await ctx.send(embed=emcon)

    @helpmod.command(aliases=["rep"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def report(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "Report", description = "Report Problem's/Bug's/Issues's", colour=discord.Colour.orange())
            emcon.add_field(name = "**SyntaxX**", value = "**-report < issue >**")
            await ctx.send(embed=emcon)

    @helpmod.command(aliases=["inf"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def info(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "Information", description = "Get information about your as well as user's", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-info or -info <mention user>**")
            await ctx.send(embed=emcon)

    @helpmod.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def server(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "Server Information", description = "Get Stats and info's  about current discord server", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-server**")
            await ctx.send(embed=emcon)

    @helpmod.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def ticket(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
           return
        else:
            emcon = discord.Embed(title = "Ticket Support", description = "creates tickets reg issues. The server administrator can add members to TICKET role to get pinged.", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-ticket new - to open a new ticket\n-ticket close - to close ticket (use this command in ticket channel in which you  want to close.**")
            await ctx.send(embed=emcon)

    @helpmod.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def imdb(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "IMDb", description = "Get IMDb results of songs/movie/tvshows etc...", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-imdb <search query>")
            emcon.add_field(name = "**syntax**", value = "**-imdb mission impossible")
            await ctx.send(embed=emcon)

    @helpmod.command(aliases=["ar","ad"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def addrole(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "AddRole", description = "Adds role to user. The role must be dominated by 'Mr Bot' role. Only members/roles with administrator role are allowed to use this command.", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-ar <mention_user> <mention_role>**")
            await ctx.send(embed=emcon)

    @helpmod.command(aliases=["rr"])
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def removerole(ctx):
        if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
            return
        else:
            emcon = discord.Embed(title = "RemoveRole", description = "Removes specific role from user.The role must be dominated by role 'Mr Bot'. Only members/roles with administrator role are allowed to use this command.", colour=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-rr <mention_user> <mention_role>**")
            await ctx.send(embed=emcon)
    
    @helpmod.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def kick(ctx):
            emcon = discord.Embed(title = "Server Kick", description = "Kicks a member from server", color=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-kick <mention member> <reason(must)>**")
            await ctx.send(embed=emcon)

    @helpmod.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def ban(ctx):
            emcon = discord.Embed(title = "Server Ban", description = "Bans a member from server", color=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-ban <mention-user> <Reason-must>**")
            await ctx.send(embed=emcon)
    
    @helpmod.command()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def qot(ctx):
            emcon = discord.Embed(title = "QOT", description = "Note: Only members who have administrator privileage in server can execute this command.\nsets up a private channel 'Quote-of-the-day' and a role 'Quodophile'. The channel created receives daily quotes at 00:00 UTC (05:30 IST) and members who have role 'Quodophile' (role which created during setup) would able to get daily quotes.", color=discord.Colour.orange())
            emcon.add_field(name = "**Syntax**", value = "**-qot**")
            await ctx.send(embed=emcon)

def setup(client):
    client.add_cog(help(client))
