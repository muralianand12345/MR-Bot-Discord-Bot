import discord,discord.ext,json
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import Command

rate=5
time=60

class suggest(Cog):
    def __init__(self,client):
        self.client=client
    
    @Cog.listener()
    async def on_ready(self):
        print("Suggest command Ready - cooldown {}/{}".format(rate,time))

    @commands.command(aliases=["s"])
    @commands.guild_only()
    @commands.cooldown(rate,time,commands.BucketType.user)
    async def suggest(self,ctx, *,arg):
        with open ("/home/runner/Bot/report.json") as file:
            data=json.load(file)
            suggest_num=int(data["suggest_no"])
            suggest_num+=1
        data["suggest_no"]=int(suggest_num)
        with open ("/home/runner/Bot/report.json","w") as f:
            json.dump(data,f)
 
        channel_suggestion = self.client.get_channel(874992310042107904)
        channel_pepper = self.client.get_channel(892047619961024562)
        embed = discord.Embed( title = "💡 Suggestion No: {}".format(suggest_num),colour = discord.Colour.teal())
        embed.add_field( name = "Suggestion" , value = "{}".format(arg))
        embed.add_field( name = "Status" , value = "Your suggestion has been notified to 'admin/server developer' {}".format(ctx.author.mention))
        embed.set_footer(text = "Suggested By {}\nFrom {}".format(ctx.author.name,ctx.guild.name))
        emoji_1 = '\N{THUMBS UP SIGN}' 
        emoji_2 = '\N{THUMBS DOWN SIGN}'
        suggestion = await channel_suggestion.send("<@&868391773909684294> <@&868391788270981161>",embed=embed)
        pepper = await channel_pepper.send("<@&875690641982644254>",embed=embed)
        await suggestion.add_reaction(emoji_1)
        await suggestion.add_reaction(emoji_2)
        await pepper.add_reaction(emoji_1)
        await pepper.add_reaction(emoji_2)
        emcon=discord.Embed(title="suggestion No: {}".format(suggest_num), description="Your suggesstion has been successfully recorded by MR Bot service",colour=discord.Colour.teal())
        emcon.add_field( name = "status", value = "200")
        emcon.add_field( name = "suggestion by MR", value="Dont spam/misuse this service")
        emcon.set_footer(text="https://bit.ly/mrthebot")
        await ctx.reply("{}".format(ctx.author.mention),embed=emcon)

def setup(client):
    client.add_cog(suggest(client))
