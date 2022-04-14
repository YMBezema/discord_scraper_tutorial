import os
import random
import discord
from dotenv import load_dotenv
from dadjokes import get_post_reddit

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Set up bot client with full permissions
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Check if bot connection has been made, then write to stdout
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Welcome new members to the server through direct message
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Yo {member.name} welkom welkom'
    )

# Runs on every message sent in channels the bot has access to
@client.event
async def on_message(message):
    # If message was sent by the bot, stop
    if message.author == client.user:
        return
    # Respond to command with a random dad joke from the top posts of reddit.com/r/dadjokes
    if message.content == 'dad joke?':
        response = random.choice(get_post_reddit('DadJokes')) 
        await message.channel.send(response)
    # Otherwise log any message that gets posted in the channel to chat.log
    else:
        with open('chat.log', 'a') as f:
            f.write(f'{message.created_at} - {message.author}:\n{message.content}\n')

# Run client with the bot's token
client.run(TOKEN)

