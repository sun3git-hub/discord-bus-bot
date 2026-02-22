import discord
from discord.ext import commands
import subprocess
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot起動完了")

@bot.command()
async def 次のバス(ctx):
    result = subprocess.run(
        ["python", "next_bus.py"],
        capture_output=True,
        text=True
    )
    await ctx.send(result.stdout)

bot.run(TOKEN)