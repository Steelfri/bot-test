import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "bot de test")

@bot.event
async def on_ready():
	print("Start")

bot.run('ODIzNTE2OTU5OTA2ODU2OTkx.YFh97w.nHa0Mfy9i437EECuDDDjP4bkQYQ')