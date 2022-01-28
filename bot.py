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

#when a message has been sent...
async def on_message(message):
    # initialising lists of users and responses to them
    foolsList = [680172801214382200, 516397002268082186]
    coolsList = [520252893396336642, 211903495362576384]

    foolResponse = ["stop talking", "fool", "poopoo head", "shut up"]
    coolResponse = ["hi!", "same", "you're so cool", "i love you"]
    
    # if a certain user is detected, respond accordingly
    if (message.author.id in foolsList):
        print (random.choice(foolResponse))
        await message.general.send(random.choice(foolResponse))
    if (message.author.id in coolsList):
        print (random.choice(coolResponse))
        await message.channel.send(random.choice(coolResponse))

client.run(token)