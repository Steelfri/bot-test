import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "*", description = "bot de test", help_command=None)

@bot.event
async def on_ready():
	print("Start")

@bot.command()
async def help(ctx, arg=None):
	if arg == "moderation":
		embed=discord.Embed(title="Liste des commandes", url="https://steelfri.fr", description="Voici la liste des commandes du bot :\n", color=0x4cf6eb)
		embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031", icon_url = "https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
		embed.add_field(name="Modération", value="`*help moderation`", inline=True)
		embed.add_field(name="Fun", value="`*help fun`", inline=True)
		embed.add_field(name="Autres", value="`*help others`", inline=True)
		embed.add_field(name="ㅤ", value="[Twitch](https://twitch.tv/steelfri)", inline=True)
		embed.add_field(name="ㅤ", value="[Twitter](https://twitter.com/031_steelfri/)", inline=True)

		await ctx.send(embed = embed)

	else:
		embed=discord.Embed(title="Liste des commandes", url="https://steelfri.fr", description="Voici la liste des commandes du bot :\n", color=0x4cf6eb)
		embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031", icon_url = "https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
		embed.add_field(name="Modération", value="`*help moderation`", inline=True)
		embed.add_field(name="Fun", value="`*help fun`", inline=True)
		embed.add_field(name="Autres", value="`*help others`", inline=True)
		embed.add_field(name="ㅤ", value="[Twitch](https://twitch.tv/steelfri)", inline=True)
		embed.add_field(name="ㅤ", value="[Twitter](https://twitter.com/031_steelfri/)", inline=True)

		await ctx.send(embed = embed)

bot.run('ODIzNTE2OTU5OTA2ODU2OTkx.YFh97w.gS-i6KWJyXMXJyhtkaQtcYNSRVs')