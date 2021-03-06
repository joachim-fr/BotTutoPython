import discord #On importe la librairie
import config.json
from discord.ext import commands

bot = commands.Bot(command_prefix=config.prefix, description=None) #On définit le préfixe du bot

@bot.event
async def on_ready():
    print("Le bot est prêt") #On lance le bot

@bot.command()
async def close(ctx): #Commande pour éteindre le bot
    await ctx.send("Le bot va s'éteindre")
    await bot.close()
    
@bot.command()
async def test(ctx):
    await ctx.send("Test")

bot.run(config.token) #Le bot va se lancer grâce au token
