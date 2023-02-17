import discord
from discord.ext import commands
from classes.strVenv import githubUrl

def getUsernameAndDS(context) -> str:
    return context.author.name + '#' + context.author.discriminator

def embedHello(context):
    embed = discord.Embed(title="Hello there, " + context.author.display_name,
                          url="",
                          description="Be sure to like and subscribe so you can get more hello theres.",
                          color=0xFF5733)
    embed.set_author(name=getUsernameAndDS(context), icon_url=context.author.avatar.url)
    embed.set_footer(text=context.message.created_at.strftime("%A, %B %d %Y | %H:%M:%S"))
    return embed