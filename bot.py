import discord
import asyncio
import gamedig
import os
from dotenv import load_dotenv

# 📥 Načtení proměnných z .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_TYPE = os.getenv("SERVER_TYPE")
SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = int(os.getenv("SERVER_PORT"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def update_status():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            result = gamedig.query(
                type=SERVER_TYPE,
                host=SERVER_IP,
                port=SERVER_PORT
            )
            player_count = len(result['players'])
            activity = discord.Game(name=f"Online: {player_count} hráčů")
        except Exception:
            activity = discord.Game(name="Server offline")
        await client.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(60)

@client.event
async def on_ready():
    print(f'✅ Přihlášen jako {client.user.name}')

client.loop.create_task(update_status())
client.run(TOKEN)
