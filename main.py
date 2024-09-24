import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
token = str(os.getenv("TOKEN"))

# Load the token from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Define the intents
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance
bot = commands.Bot(intents=intents, command_prefix="/") # replace Bot with AutoShardedBot when over 2500 servers

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    await bot.change_presence(activity=discord.Game(name="Discord"))

    # Loads commands from the extensions
    await bot.load_extension("utils")
    await bot.load_extension("channels")
    print("Loaded extensions successfully!")

    sync_channel = bot.get_channel(int(config["sync_channel_id"]))
    await sync_channel.send('Syncing...')
    synced_commands = await bot.tree.sync()
    await sync_channel.send(f'Synced {len(synced_commands)} commands!')
    print("Synced the commands")

# Run the bot
bot.run(token)
