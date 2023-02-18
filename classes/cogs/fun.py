import discord
from discord.ext import commands
import classes.embedBuilder as eb
from classes.strVenv import greetings
import random

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(random.choice(greetings))

    @commands.command()
    async def helloembed(self, ctx):
        await ctx.send(embed=eb.embedHello(ctx))