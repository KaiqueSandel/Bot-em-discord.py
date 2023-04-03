from discord.ext import commands,tasks
import discord
from discord import app_commands
import logging
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix="k.",intents=discord.Intents.all(),application_id=int(os.getenv("BOT_ID")))

async def main():
    async with bot:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')

        
        TOKEN = os.getenv("DISCORD_TOKEN")
        await bot.start(TOKEN)

asyncio.run(main())

