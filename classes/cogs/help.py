import discord
from discord.ext import commands
import classes.embedBuilder as eb

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = eb.embedGeneric(ctx, "Help commands", "Shows various help commands")
        embed.add_field(name="❓ - Show this help", value="`$help`", inline=True)
        embed.add_field(name="🎮 - Fun commands", value="`$helpfun`", inline=True)
        embed.add_field(name="⚔️ - RPG commands", value="`$helprpg`", inline=True)
        embed.add_field(name="⚙️ - Other commands", value="`$helpmisc`", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def helpfun(self, ctx):
        embed = eb.embedGeneric(ctx, "🎮 - Fun commands", "Various fun commands.")
        embed.add_field(name="`$hello`", value="Say hello to the bot.", inline=True)
        embed.add_field(name="`$helloembed`", value="Say hello to the bot, this time with the power of embeds.", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def helprpg(self, ctx):
        embed = eb.embedGeneric(ctx, "⚔️ - RPG commands", "Commands to venture in the world of Kitenia.")
        embed.add_field(name="`$createplayer`", value="Create your player account.", inline=True)
        embed.add_field(name="`$playerlist`", value="Get a list of all players on the server.", inline=True)
        await ctx.send(embed=embed)