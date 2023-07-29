import discord
from discord.ext import commands
import classes.embedBuilder as eb
from classes.strVenv import greetings
import random
import datetime
import os


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(random.choice(greetings))

    @commands.command()
    async def helloembed(self, ctx):
        await ctx.send(embed=eb.embedHello(ctx))

    @commands.command(aliases=['quote'])
    async def addquote(self, ctx, quote: str = None, author: discord.Member = None):
        if quote is None or author is None:
            await ctx.send(
                embed=eb.embedGeneric(ctx, "Quotes", "Here is the correct syntax: `$addquote 'text' @Author`"))
        else:
            with open('data/quotes/' + str(ctx.channel.guild.id), "a+") as f:
                f.write(f'"{quote}", {author.name}, {datetime.datetime.utcnow().strftime("%B %d %Y")}\n')
            await ctx.send(embed=eb.embedGeneric(ctx, "Quotes", "Quote added successfully."))

    @commands.command(aliases=['lquote'])
    async def quotelist(self, ctx):
        if not os.path.isfile('data/quotes/' + str(ctx.channel.guild.id)):
            await ctx.send(embed=eb.embedGeneric(ctx, "Quotes", "No quotes have been added for this server yet."))
        else:
            lines = open('data/quotes/' + str(ctx.channel.guild.id)).read().split('\n')
            embed = eb.embedGeneric(ctx, "Quotes", "Here is every quote created on the server.")
            for i, line in enumerate(lines):
                if len(line) > 5:
                    embed.add_field(name=f"N°{i}", value=str(line), inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def topicimg(self, ctx, topic: str = None):
        if topic is None:
            await ctx.send(embed=eb.embedGeneric(ctx, "Quotes", "Please specify a topic."))
        else:
            topic = topic.lower()
            if topic not in os.listdir("data/img/topics") or topic == "example":
                await ctx.send(embed=eb.embedGeneric(ctx, "Quotes", "The topic you specified does not exist."))
                return
            await ctx.reply(embed=eb.embedImageTopic(topic, getRandomLineFromFile(f"data/img/topics/{topic}")))

# yeah I know it's duplicated code but circular imports are a pain to fix!
def getRandomLineFromFile(filename: str):
    return random.choice(open(filename).read().splitlines())