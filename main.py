import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "bot de test")

@bot.event
async def on_ready()
	print("Start")

bot.run('ODIzNTE2OTU5OTA2ODU2OTkx.YFh97w.7SknaliF7na4bShsCrvnE_7NcYs')