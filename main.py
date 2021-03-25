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

@client.command()
@commands.has_any_role(824784559735963688)
async def tmute(ctx, member : discord.Member, time=0,*, reason=None):
    if not member or time == 0 or time == str:
        await ctx.channel.send(embed=commanderror)
        return
    elif reason == None:
        reason = "Aucunes raisons fournies"

    muteRole = discord.utils.get(ctx.guild.roles, id=663076470180151339)
    await member.add_roles(muteRole)

    tempMuteEmbed = discord.Embed(colour=embedcolour, description=f"**Reason:** {reason}")
    tempMuteEmbed.set_author(name=f"{member} Has Been Muted", icon_url=f"{member.avatar_url}")
    tempMuteEmbed.set_footer(text=embedfooter)

    await ctx.channel.send(embed=tempMuteEmbed)

    tempMuteModLogEmbed = discord.Embed(color=embedcolour)
    tempMuteModLogEmbed.set_author(name=f"[MUTE] {member}", icon_url=f"{member.avatar_url}")
    tempMuteModLogEmbed.add_field(name="User", value=f"{member.mention}")
    tempMuteModLogEmbed.add_field(name="Moderator", value=f"{ctx.message.author}")
    tempMuteModLogEmbed.add_field(name="Reason", value=f"{reason}")
    tempMuteModLogEmbed.add_field(name="Duration", value=f"{str(time)}")
    tempMuteModLogEmbed.set_footer(text=embedfooter)
    modlog = client.get_channel(638783464438759464)
    await modlog.send(embed=tempMuteModLogEmbed)

    tempMuteDM = discord.Embed(color=embedcolour, title="Mute Notification", description="You Were Muted In **The Official Vanmanyo Discord Server**")
    tempMuteDM.set_footer(text=embedfooter)
    tempMuteDM.add_field(name="Reason", value=f"{reason}")
    tempMuteDM.add_field(name="Duration", value=f"{time}")

    userToDM = client.get_user(member.id)
    await userToDM.send(embed=tempMuteDM)

    await asyncio.sleep(time)
    await member.remove_roles(muteRole)

    unMuteModLogEmbed = discord.Embed(color=embedcolour)
    unMuteModLogEmbed.set_author(name=f"[UNMUTE] {member}", icon_url=f"{member.avatar_url}")
    unMuteModLogEmbed.add_field(name="User", value=f"{member.mention}")
    unMuteModLogEmbed.set_footer(text=embedfooter)
    modlog = client.get_channel(638783464438759464)
    await modlog.send(embed=unMuteModLogEmbed)

bot.run('ODIzNTE2OTU5OTA2ODU2OTkx.YFh97w.gch47GAXlnIhoGju2JvymnEd0Ps')