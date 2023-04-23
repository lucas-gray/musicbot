import discord
from discord.ext import commands
import music


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

def read_token(filename):
    file = open(filename, "r")
    token = file.read().strip()
    file.close()
    return token

def main():
    cogs = [music]
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Bot(command_prefix='!', intents=intents)
    for i in range(len(cogs)):
        cogs[i].setup(client)
    filename = "token.txt"
    client.run(read_token(filename))

if __name__ == "__main__":
    main()
