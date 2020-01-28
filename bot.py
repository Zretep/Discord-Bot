import discord
import random
import youtube_dl
import time

from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio

token = "Enter Bot Token"

client = commands.Bot(command_prefix=".")
client.remove_command("help")

players = {}


@client.event
async def on_ready():
    print("Bot is online.")


@client.command()
async def dice(ctx):
    dice = random.randint(1, 6)
    embed = discord.Embed(title="Dice Roll", description=" ", color=0xff2600)
    if dice == 1:
        embed.set_thumbnail(url="https://www.imgur.com/f5s25Jf.png")
        embed.add_field(name="The dice lands on a ", value=1, inline=True)
    elif dice == 2:
        embed.set_thumbnail(url="https://www.imgur.com/tsX041R.png")
        embed.add_field(name="The dice lands on a ", value=2, inline=True)
    elif dice == 3:
        embed.set_thumbnail(url="https://www.imgur.com/ONBIzoc.png")
        embed.add_field(name="The dice lands on a ", value=3, inline=True)
    elif dice == 4:
        embed.set_thumbnail(url="https://www.imgur.com/Edk9gbN.png")
        embed.add_field(name="The dice lands on a ", value=4, inline=True)
    elif dice == 5:
        embed.set_thumbnail(url="https://www.imgur.com/OjZ5sY0.png")
        embed.add_field(name="The dice lands on a ", value=5, inline=True)
    else:
        embed.set_thumbnail(url="https://www.imgur.com/4B9ScO4.png")
        embed.add_field(name="The dice lands on a ", value=6, inline=True)

    await ctx.send(embed=embed)


@client.command()
async def share(ctx):
    guildID = str(ctx.message.guild.id)  # fetches guild id
    if ctx.author.voice and ctx.author.voice.channel:  # if user is in a voice channel
        # fetches channel id of author of message
        channelID = str(ctx.author.voice.channel.id)
    else:  # if user not connected to a voice channel
        await ctx.send("You are not connected to a voice channel")
        return
    shareURL = "https://www.discordapp.com/channels/"+guildID+"/"+channelID

    embed = discord.Embed(title=shareURL, url=shareURL,
                          description="Click the link to start sharing!", color=0xff2600)
    embed.set_author(name="Desktop Screen Share",
                     icon_url="REPLACE WITH LOGO")

    await ctx.send(embed=embed)


@client.command()
async def coin(ctx):
    coin = random.randint(0, 1)
    embed = discord.Embed(title="Coin Flip", description=" ", color=0xff2600)
    if coin == 0:
        embed.set_thumbnail(
            url="REPLACE WITH HEADS IMAGE")
        embed.add_field(name="The coin flips and it lads on ",
                        value="Heads", inline=True)
    else:
        embed.set_thumbnail(
            url="REPLACE WITH TAILS IMAGE")
        embed.add_field(name="The coin flips and it lads on ",
                        value="Tails", inline=True)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def noice(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(discord.FFmpegPCMAudio("lul.mp3"))   #broken needs to fix path

    time.sleep(4)

    await voice.disconnect()


@client.command(pass_context=True)
async def leave(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel")


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", color=0xff2600)
    embed.set_author(name="Zretep Bot",
                     icon_url="REPLACE WITH LOGO")
    embed.add_field(name=".share",
                    value="Create a link to start screen sharing(must be in voice channel)", inline=False)
    embed.add_field(name=".dice", value="Roll a 6 sided dice", inline=False)
    embed.add_field(name=".coin", value="Flips a coin", inline=False)

    await ctx.send(embed=embed)


client.run(token)
