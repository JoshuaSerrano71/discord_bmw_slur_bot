import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

slurs = ["SYBAU NGA", "Nigger said bmw", "Nigga", "Fuck you", "bitch", 'MODS BAN THIS MOTHERFUCKER, HE SAID THE B SLUR', 'i hate you']

@bot.event
async def on_ready():
    print(f'Bot is online: {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "bmw" in message.content.lower():
        # Reply directly to the user's message
        await message.reply(random.choice(slurs), mention_author=True)

    await bot.process_commands(message)

bot.run(TOKEN)
