import discord
from discord.ext import commands
from classes.strVenv import githubUrl
import datetime

def getFullUsername(context) -> str:
    return context.author.name

def getFullDate(context) -> str:
    return context.message.created_at.strftime("%A, %B %d %Y | %X")

def embedHello(context) -> discord.Embed:
    embed = discord.Embed(title="Hello there, " + context.author.display_name,
                          url="",
                          description="Be sure to like and subscribe so you can get more hello theres.",
                          color=0xFF5733)
    embed.set_author(name=getFullUsername(context), icon_url=context.author.avatar.url)
    embed.set_footer(text=getFullDate(context))
    return embed

def embedGeneric(context, title, text) -> discord.Embed:
    embed = discord.Embed(title=title,
                          url="",
                          description=text,
                          color=0xFF5733)
    embed.set_author(name=getFullUsername(context), icon_url=context.author.avatar.url)
    embed.set_footer(text=datetime.datetime.now().strftime("%A, %B %d %Y | %X"))
    return embed

def embedGenericThumb(context, title, text, thumbUrl) -> discord.Embed:
    return embedGeneric(context,title,text).set_thumbnail(url=thumbUrl)

def embedImageTopic(topic, imgUrl) -> discord.Embed:
    embed = discord.Embed(
        title=topic,
        url=imgUrl
    )
    embed.set_image(url=imgUrl)
    return embed

