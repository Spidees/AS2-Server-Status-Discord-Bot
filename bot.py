import socket
import struct
import os
import asyncio
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = int(os.getenv("SERVER_PORT"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()

def query_server(ip, port, timeout=3):
    A2S_INFO_HEADER = b'\xFF\xFF\xFF\xFFTSource Engine Query\x00'
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(timeout)
        s.sendto(A2S_INFO_HEADER, (ip, port))
        data, _ = s.recvfrom(4096)

        if data[4] == 0x41:
            # challenge request
            challenge = struct.unpack('<i', data[5:9])[0]
            full_request = A2S_INFO_HEADER + struct.pack('<i', challenge)
            s.sendto(full_request, (ip, port))
            data, _ = s.recvfrom(4096)

        if data[4] != 0x49:
            raise ValueError("Neplatná A2S odpověď (nezačíná 0x49)")

        i = 6  # po hlavičce

        def read_string(data, offset):
            end = data.index(0, offset)
            return data[offset:end].decode('utf-8', errors='ignore'), end + 1

        name, i = read_string(data, i)
        map_name, i = read_string(data, i)
        folder, i = read_string(data, i)
        game, i = read_string(data, i)
        i += 2  # skip game ID (2 bajty)

        players = data[i]
        max_players = data[i + 1]

        return name, players, max_players

class VRisingBot(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = None

    async def setup_hook(self):
        asyncio.create_task(self.update_status_and_embed())

    async def on_ready(self):
        print(f"✅ Přihlášen jako {self.user.name}")

    async def update_status_and_embed(self):
        await self.wait_until_ready()
        channel = self.get_channel(CHANNEL_ID)

        while True:
            try:
                name, players, max_players = query_server(SERVER_IP, SERVER_PORT)
                activity = discord.Game(name=f"{players} / {max_players} players")
                embed = discord.Embed(title=name, description=f"**{players} / {max_players} hráčů online**", color=0x00ff00)
            except Exception as e:
                activity = discord.Game(name="Server offline")
                embed = discord.Embed(title="Server offline", description="❌ Nepodařilo se připojit", color=0xff0000)

            await self.change_presence(status=discord.Status.online, activity=activity)

            try:
                if self.message and self.message.channel == channel:
                    await self.message.edit(embed=embed)
                else:
                    self.message = await channel.send(embed=embed)
            except:
                pass

            await asyncio.sleep(60)

client = VRisingBot(intents=intents)
client.run(TOKEN)
