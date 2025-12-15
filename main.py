import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot online & semua command siap 🚀")

# load command dari folder commands
from commands.balance import balance
from commands.gacha import gacha

bot.tree.add_command(balance)
bot.tree.add_command(gacha)

bot.run(TOKEN)
