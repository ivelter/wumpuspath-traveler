import discord
from discord.ext import commands, tasks
import pickle
import classes.embedBuilder as eb
from classes.playerClass import Player
from classes.playerClass import getPlayerByID
import datetime

class RPGCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pcreate'])
    async def createplayer(self, ctx):
        if ctx.author.id in [p.memberID for p in Player.playerList]:
            await ctx.send(embed=eb.embedGeneric(context=ctx,
                                                                   title="Project Wumpuspath Traveler : Account creation",
                                                                   text="Looks like you already have an account."))
        else:
            a = Player(ctx)
            await ctx.send(
                embed=eb.embedGenericThumb(ctx, "Project Wumpuspath Traveler : Account creation",
                                                             "Your account has been created successfully ! Welcome to the world of Kitenia.",
                                                             "https://cdn.discordapp.com/attachments/1054708746774904914/1076256340344844318/checkmark.png"))
            await savePlayers()

    @commands.command(aliases=['plist'])
    async def playerlist(self, ctx):
        if len(Player.playerList) == 0:
            await ctx.send(embed=eb.embedGeneric(context=ctx,
                                                 title="Project Wumpuspath Traveler - Player List",
                                                 text="No players have made an account thus far."))
        else:
            embed = eb.embedGeneric(context=ctx, title="Project Wumpuspath Traveler - Player List", text="Here are the players that have ventured through the world of Kitenia thus far :")
            for p in sorted(Player.playerList, key=lambda player: int(player.level), reverse=True):
                embed.add_field(name=p.shortSTR(), value="Level " + str(p.level), inline=True)
            await ctx.send(embed=embed)

    @commands.command(aliases=['pinfo'])
    async def playerinfo(self, ctx, m:discord.Member=None):
        if m is not None:
            if m.id not in [p.memberID for p in Player.playerList]:
                await ctx.send(embed=eb.embedGeneric(context=ctx, title=f"Project Wumpuspath Traveler - {m.display_name}'s info", text="This player doesn't have an account."))
            else:
                player = getPlayerByID(m.id)
                embed = eb.embedGeneric(context=ctx, title=f"Project Wumpuspath Traveler - {player.memberDisplayName}'s info", text=player)
                await ctx.send(embed=embed)
        else:
            await ctx.send(embed=eb.embedGeneric(context=ctx,title=f"Project Wumpuspath Traveler - Player info",text="You must specify a member when using this command."))

async def savePlayers():
    #with open('./data/players.pkl', 'wb') as outp:  # Overwrites any existing file.
    #    await pickle.dump(Player.playerList, outp, pickle.HIGHEST_PROTOCOL)
    print("🗿🏳️‍🌈 moai supports lgbt rights")
