import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/play"):
        await message.channel.send("Hell no, that shit is trash.")
    if message.content.startswith("fuck you"):
        await message.channel.send("fuck you!")

def read_token(filename):
    file = open(filename, "r")
    token = file.read().strip()
    file.close()
    return token

def main():
    filename = "token.txt"
    client.run(read_token(filename))

if __name__ == "__main__":
    main()
