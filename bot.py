# importing libraries
import os
import discord
from dotenv import load_dotenv

#loading the token from the .env file
load_dotenv()
token = os.getenv('TOKEN')

#initializing the bot to discord
client = discord.Client()

#if we've connected, it prints to the terminal, not to discord.
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)