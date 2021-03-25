import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "*r", description = "bot de test")

@bot.event
async def on_ready():
	print("Start")

@bot.command()
async def commands(ctx):
	embed=discord.Embed(title="Liste des commandes", url="https://steelfri.fr", description="Voici la liste des commandes du bot", color=0x4cf6eb)
	embed.set_footer(text="Esclavre de Steelfri - Communauté Steelfri / Team 031", icon_url = "https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
	await ctx.send(embed = embed)

bot.run('ODIzNTE2OTU5OTA2ODU2OTkx.YFh97w.gjtF2alodiH2hPX6A6yv7bQqmJ4')