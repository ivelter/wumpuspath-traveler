# bot.py
import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import sys
import random
import pickle
import datetime

import classes.embedBuilder
from classes.playerClass import Player
from classes.cogs.rpg import savePlayers

# Cog setups
from classes.cogs.help import HelpCog
from classes.cogs.rpg import RPGCog
from classes.cogs.fun import FunCog

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)
botHasStarted = False

@bot.event
async def on_ready():
    global botHasStarted
    print(f'Logged in as {bot.user}')
    if not botHasStarted:
        # Things to do on startup
        if os.path.isfile('./data/players.pkl'):
            await loadPlayers()
        await bot.add_cog(HelpCog(bot))
        await bot.add_cog(RPGCog(bot))
        await bot.add_cog(FunCog(bot))
        saveP.start()
        botHasStarted = True

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

async def loadPlayers():
    with open('./data/players.pkl', 'rb') as inp:
        Player.playerList = pickle.load(inp)

@tasks.loop(minutes=5)
async def saveP():
    print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] - Automatically saved player data.')
    await savePlayers()

bot.run(TOKEN)