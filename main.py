import discord
from discord.ext import commands
import asyncio
import music

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

def read_token(filename):
    file = open(filename, "r")
    token = file.read().strip()
    file.close()
    return token

async def main():
    await music.setup(client)
    async with client:
        await client.start(read_token("token.txt"))

asyncio.run(main())
