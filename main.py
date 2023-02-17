# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sys
import random

from classes.strVenv import greetings
import classes.embedBuilder

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

bot.run(TOKEN)