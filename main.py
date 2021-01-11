import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="t", description=None)

@bot.event
async def on_ready():
    print("Le bot est prêt")

@bot.command()
async def close(ctx):
    await ctx.send("Le bot va s'éteindre")
    await bot.close()

bot.run("ton token")
