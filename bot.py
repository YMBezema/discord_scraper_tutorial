import os
import random
import discord
from dotenv import load_dotenv

from dadjokes import get_post_reddit

intents = discord.Intents.default()
intents.members = True


#print(random.choice(get_post_reddit('DadJokes')))

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Yo {member.name} welkom welkom'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'dad joke?':
        response = random.choice(get_post_reddit('DadJokes')) 
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(TOKEN)

