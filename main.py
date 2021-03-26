import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "*", description = "bot de test", help_command=None)

@bot.event
async def on_ready():
	print("Start")

@bot.command()
async def help(ctx, arg=None):
	if arg == "moderation":
		embed=discord.Embed(title="Liste des commandes de modération", url="https://steelfri.fr", description="Voici la liste des commandes destinées aux modérateurs :\n", color=0x4cf6eb)
		embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031", icon_url = "https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
		embed.add_field(name="Modération :", value="`*tmute`, `*tban`, `*ban`, `*kill`", inline=False)
		
		await ctx.send(embed = embed)

	elif arg == "fun":
		embed=discord.Embed(title="Liste des commandes fun", url="https://steelfri.fr", description="Voici la liste des commandes amusantes :\n", color=0x4cf6eb)
		embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031", icon_url = "https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
		embed.add_field(name="Fun :", value="`*anti-mouton`", inline=False)

		await ctx.send(embed = embed)

	elif arg == "others":
		embed=discord.Embed(title="Liste des autres commandes", url="https://steelfri.fr", description="Voici la liste des commandes non catégorisées :\n", color=0x4cf6eb)
		embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031", icon_url = "https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
		embed.add_field(name="Autres :", value="`*help`", inline=False)

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

#https://stackoverflow.com/questions/61321062/discord-py-tempmute-command edit par moi je savais pas faire le truc du temps rip
@client.command()
@commands.has_any_role(824784559735963688)

time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}

def convert_time_to_seconds(time):
    try:
        return int(time[:-1]) * time_convert[time[-1]]
    except:
        return time

async def tmute(ctx, member : discord.Member, time=0,*, reason=None):
    if not member or time == 0 or time == str:
        await ctx.channel.send(embed=commanderror)
        return
    elif reason == None:
        reason = "Aucunes raisons fournies"

    muteRole = discord.utils.get(ctx.guild.roles, id=824784923726053376)

    await member.add_roles(muteRole)

    tembed=discord.Embed(title="Mute Temporaire", url="https://steelfri.fr", description=f"{member} a été mute :\n", color=0x4cf6eb)
		tembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031", icon_url = "https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
		tembed.add_field(name="Membre Mute :", value=f"`{member}`", inline=True)
		tembed.add_field(name="Raison :", value=f"`{reason}`", inline=True)


    await ctx.channel.send(embed=tembed)

    tembed=discord.Embed(title=f"Logs TMute - {member.mention}", url="https://steelfri.fr", description=f"Information sur le mute :\n", color=0x4cf6eb)
		tembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031", icon_url = "https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
		tembed.add_field(name="Membre Mute :", value=f"`{member}`", inline=True)
		tembed.add_field(name="Raison :", value=f"`{reason}`", inline=True)
		tembed.add_field(name="Modérateur :", value=f"`{ctx.message.author}")
		tembed.add_field(name="Durée :", value=f"`{str(time)}`")

    modlog = client.get_channel(824791678522097685)
    await modlog.send(embed=tempMuteModLogEmbed)
    
bot.run('ODIzNTE2OTU5OTA2ODU2OTkx.YFh97w.gch47GAXlnIhoGju2JvymnEd0Ps')