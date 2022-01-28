# importing libraries
import os
import random
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
    print(f'{client.user} online.')

#when a message has been sent
async def on_message(message):
    foolsList = [680172801214382200, 516397002268082186]
    responseList = ["stop talking", "fool", "poopoo head", "shut up"] # common responses to fools on the internet
    if (foolsList.contains(message.author.id)): # if it's someone in foolsList...
        await message.channel.send(random.choice(responseList)) #...give one of those common responses.

client.run(token)