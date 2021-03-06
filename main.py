import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="*", description="bot de test", help_command=None, intents=intents)

muted_list = []
banned_list = []

@bot.event
async def on_ready():
    print("Start")


@bot.event
async def on_member_join(member):
    if member.id in muted_list:
        for role in member.guild.roles:
            if role.name == "Muted":
                await member.add_roles(role)
    if member.id in banned_list:
        for role in member.guild.roles:
            if role.name == "Banned":
                await member.add_roles(role)


@bot.command()
async def help(ctx, arg=None):
    if arg == "moderation":
        embed = discord.Embed(title="Liste des commandes de modération", url="https://steelfri.fr",
                              description="Voici la liste des commandes destinées aux modérateurs :\n", color=0x4cf6eb)
        embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                         icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
        embed.add_field(name="Modération :", value="`*tmute`, `*tban`, `*ban`, `*kill`", inline=False)

        await ctx.send(embed=embed)

    elif arg == "fun":
        embed = discord.Embed(title="Liste des commandes fun", url="https://steelfri.fr",
                              description="Voici la liste des commandes amusantes :\n", color=0x4cf6eb)
        embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                         icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
        embed.add_field(name="Fun :", value="`*anti-mouton`", inline=False)

        await ctx.send(embed=embed)

    elif arg == "others":
        embed = discord.Embed(title="Liste des autres commandes", url="https://steelfri.fr",
                              description="Voici la liste des commandes non catégorisées :\n", color=0x4cf6eb)
        embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                         icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
        embed.add_field(name="Autres :", value="`*help`", inline=False)

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Liste des commandes", url="https://steelfri.fr",
                              description="Voici la liste des commandes du bot :\n", color=0x4cf6eb)
        embed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                         icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
        embed.add_field(name="Modération", value="`*help moderation`", inline=True)
        embed.add_field(name="Fun", value="`*help fun`", inline=True)
        embed.add_field(name="Autres", value="`*help others`", inline=True)
        embed.add_field(name="ㅤ", value="[Twitch](https://twitch.tv/steelfri)", inline=True)
        embed.add_field(name="ㅤ", value="[Twitter](https://twitter.com/031_steelfri/)", inline=True)

        await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role(824784559735963688)
async def tmute(ctx, member: discord.Member, time: int, aac, *, reason=None):
    guild = ctx.guild
    global muted_list

    if aac not in ["s", "m", "h", "d"]:
        eembed = discord.Embed(title="Erreur", url="https://steelfri.fr", description=f"Une erreur est survenue:\n",
                               color=0x4cf6eb)
        eembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                          icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
        eembed.add_field(name="Erreur :", value=f"Un champ est mal entré", inline=True)
        return await ctx.send(embed=eembed)

    if member.id in muted_list:
        eembed = discord.Embed(title="Erreur", url="https://steelfri.fr", description=f"Une erreur est survenue:\n",
                               color=0x4cf6eb)
        eembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                          icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
        eembed.add_field(name="Erreur :", value=f"Le membre est déjà mute", inline=True)
        return await ctx.send(embed=eembed)

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            muted_list.append(member.id)

            tembed = discord.Embed(title="Mute Temporaire", url="https://steelfri.fr",
                                   description=f"{member} a été mute :\n", color=0x4cf6eb)
            tembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                              icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
            tembed.add_field(name="Membre Mute :", value=f"`{member}`", inline=True)
            tembed.add_field(name="Raison :", value=f"`{reason}`", inline=True)
            await ctx.send(embed=tembed)

            if aac == "s":
                await asyncio.sleep(time)

            elif aac == "m":
                await asyncio.sleep(time * 60)

            elif aac == "h":
                await asyncio.sleep(time * 60 * 60)

            elif aac == "d":
                await asyncio.sleep(time * 60 * 60 * 24)

            else:
                eembed = discord.Embed(title="Erreur", url="https://steelfri.fr",
                                       description=f"Une erreur est survenue:\n", color=0x4cf6eb)
                eembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                                  icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
                eembed.add_field(name="Erreur :", value=f"Un champ est mal entré", inline=True)
                await ctx.send(embed=eembed)

            await member.remove_roles(role)
            muted_list.remove(member.id)

            uembed = discord.Embed(title="Unmute", url="https://steelfri.fr", description=f"{member} a été mute :\n",
                                   color=0x4cf6eb)
            uembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                              icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
            uembed.add_field(name="Membre Unmute :", value=f"`{member}`", inline=True)
            await ctx.send(embed=uembed)

            return


@bot.command()
@commands.has_any_role(824784559735963688)
async def tban(ctx, member: discord.Member, time: int, aac, *, reason=None):
    guild = ctx.guild
    global muted_list

    if aac not in ["s", "m", "h", "d"]:
        eembed = discord.Embed(title="Erreur", url="https://steelfri.fr", description=f"Une erreur est survenue:\n",
                               color=0x4cf6eb)
        eembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                          icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
        eembed.add_field(name="Erreur :", value=f"Un champ est mal entré", inline=True)
        return await ctx.send(embed=eembed)

    if member.id in muted_list:
        eembed = discord.Embed(title="Erreur", url="https://steelfri.fr", description=f"Une erreur est survenue:\n",
                               color=0x4cf6eb)
        eembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                          icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
        eembed.add_field(name="Erreur :", value=f"Le membre est déjà mute", inline=True)
        return await ctx.send(embed=eembed)

    for role in guild.roles:
        if role.name == "Banned":
            await member.add_roles(role)
            banned_list.append(member.id)

            tembed = discord.Embed(title="Ban Temporaire", url="https://steelfri.fr",
                                   description=f"{member} a été mute :\n", color=0x4cf6eb)
            tembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                              icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
            tembed.add_field(name="Membre Ban :", value=f"`{member}`", inline=True)
            tembed.add_field(name="Raison :", value=f"`{reason}`", inline=True)
            await ctx.send(embed=tembed)

            if aac == "s":
                await asyncio.sleep(time)

            elif aac == "m":
                await asyncio.sleep(time * 60)

            elif aac == "h":
                await asyncio.sleep(time * 60 * 60)

            elif aac == "d":
                await asyncio.sleep(time * 60 * 60 * 24)

            else:
                eembed = discord.Embed(title="Erreur", url="https://steelfri.fr",
                                       description=f"Une erreur est survenue:\n", color=0x4cf6eb)
                eembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                                  icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
                eembed.add_field(name="Erreur :", value=f"Un champ est mal entré", inline=True)
                await ctx.send(embed=eembed)

            await member.remove_roles(role)
            banned_list.remove(member.id)

            uembed = discord.Embed(title="Unban", url="https://steelfri.fr", description=f"{member} a été unban :\n",
                                   color=0x4cf6eb)
            uembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                              icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
            uembed.add_field(name="Membre Unban :", value=f"`{member}`", inline=True)
            await ctx.send(embed=uembed)

            return

@bot.command()
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    bembed = discord.Embed(title="Ban", url="https://steelfri.fr", description=f"{user.name} a été ban perm :\n",
                           color=0x4cf6eb)
    bembed.set_footer(text="Esclave de Steelfri - Communauté Steelfri / Team 031",
                           icon_url="https://media.discordapp.net/attachments/736631083185078302/824098862783397928/image0.png?width=559&height=559")
    bembed.add_field(name="Membre Ban Perm :", value=f"`{user.name}`", inline=True)
    bembed.add_field(name="Raison :", value=f"`{reason}`", inline=True)
    await ctx.send(embed=bembed)

bot.run('ODIzNTE2OTU5OTA2ODU2OTkx.YFh97w.QDP4GZUe80DOWovMVqxcIpPmvN0')