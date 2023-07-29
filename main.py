# bot.py
import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import sys
import random
import datetime
import classes.databaseMgt as db
from classes.strVenv import activities
import classes.embedBuilder as eb

import classes.embedBuilder
from classes.playerClass import Player
from classes.cogs.rpg import savePlayers

# Cog setups
from classes.cogs.help import HelpCog
from classes.cogs.rpg import RPGCog
from classes.cogs.fun import FunCog

def getRandomActivity():
    return discord.Game(name=random.choice(activities)+" | $help")


intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None, activity=getRandomActivity())
botHasStarted = False

@bot.event
async def on_ready():
    global botHasStarted
    print(f'Logged in as {bot.user}')
    if not botHasStarted:
        # Things to do on startup
        await db.initDB()
        await bot.add_cog(HelpCog(bot))
        await bot.add_cog(RPGCog(bot))
        await bot.add_cog(FunCog(bot))
        await sendImagesForSubscribedTopics()
        saveP.start()
        botHasStarted = True

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    try:
        await bot.process_commands(message)
    except Exception as e:
        await message.channel.send("Oopsie doopsie ! I made a fuckie wuckie ! Be sure to send a message to my owner so I don't make fucky wuckies anymore ! ^^")

    # Le funni
    if message.content.lower().endswith('quoi'):
        await message.channel.send(message.author.mention + " feur")
    if message.content.lower().endswith('non'):
        await message.channel.send(message.author.mention + " bril")
    if message.content.lower().endswith('ouais'):
        await message.channel.send(message.author.mention + " stern")
    if message.content.lower().endswith('sob'):
        await message.channel.send(message.author.mention + " rement")
    if "ratio" in message.content.lower():
        await message.channel.send(message.author.mention + " Contre-ratio")

    if message.content.startswith('$update'):
        await message.channel.send('Updated the slash commands list successfully')
        await bot.tree.sync()

@tasks.loop(minutes=5)
async def saveP():
    print(f'[{datetime.datetime.now().strftime("%X")}] - Automatically saved player data.')
    await savePlayers()

@tasks.loop(hours=12)
async def sendImagesForSubscribedTopics():
    # TODO: add a command to actually subscribe to the topic since you can't. really do that rn. please don't say
    #  anything
    chanlist = [{"chanId": 1134923462855626833, "topic": "lanz"}]
    for couple in chanlist:
        await sendTopicImgToSpecifiedChannel(couple.get("chanId"), couple.get("topic"))

async def sendTopicImgToSpecifiedChannel(chanId, topic):
    # Assuming the topic already exists as this is an... in-house solution
    channel = bot.get_channel(chanId)
    await channel.send(embed=eb.embedImageTopic(topic, getRandomLineFromFile(f"data/img/topics/{topic}")))

def getRandomLineFromFile(filename: str):
    return random.choice(open(filename).read().splitlines())


bot.run(TOKEN)
