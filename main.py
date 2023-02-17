# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sys
import random

from classes.strVenv import greetings
import classes.embedBuilder
from classes.playerClass import Player

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    try:
        await bot.process_commands(message)
    except:
        await message.channel.send("Oopsie doopsie ! I made a fuckie wuckie ! Be sure to send a message to my owner so I don't make fucky wuckies anymore ! ^^")
    if message.content.startswith('$update'):
        await message.channel.send('Updated the slash commands list successfully')
        await bot.tree.sync()

@bot.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings))

@bot.command()
async def helloembed(ctx):
    await ctx.send(embed=classes.embedBuilder.embedHello(ctx))

@bot.command()
async def createplayer(ctx):
    if ctx.author.id in [p.memberID for p in Player.playerList]:
        await ctx.send(embed=classes.embedBuilder.embedGeneric(context=ctx,title="Project Wumpuspath Traveler : Account creation",text="Looks like you already have an account."))
    else:
        a = Player(ctx)
        await ctx.send(embed=classes.embedBuilder.embedGenericThumb(ctx, "Project Wumpuspath Traveler : Account creation","Your account has been created successfully ! Welcome to the world of Kitenia.","https://cdn.discordapp.com/attachments/1054708746774904914/1076256340344844318/checkmark.png"))

bot.run(TOKEN)