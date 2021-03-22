import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "bot de test")

@bot.event
async def on_ready():
	print("Start")

@bot.command()
async def coucou(ctx):
	await ctx.send("Hellow there")

@bot.command()
async def serverInfo(ctx):
	server = ctx.guild
	numberOfChannel = len(server.text_channels)
	numberOfVoice = len(server.voice_channels)
	numberOfMember = server.member_count
	name = server.name 
	numberofchannels = numberOfChannel + numberOfVoice
	message = f"**{name}**\nNombre de membres : *{numberOfMember}*\nNombre de channels : *{numberofchannels}*\nSalons textuels : *{numberOfChannel}*\nSalons vocaux : *{numberOfVoice}*"
	await ctx.send(message)

bot.run('ODIzNTE2OTU5OTA2ODU2OTkx.YFh97w.nHa0Mfy9i437EECuDDDjP4bkQYQ')