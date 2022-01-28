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

    channel = client.get_channel(936463987258839050)
    await channel.send("i'm back <3")

#when a message has been sent...
@client.event
async def on_message(message):
    # initialising lists of users and responses to them
    foolsList = [680172801214382200, 516397002268082186]
    coolsList = [520252893396336642, 211903495362576384]

    foolResponse = ["stop talking", "fool", "poopoo head", "shut up"]
    coolResponse = ["hi!", "same", "you're so cool", "i love you"]
    
    # 15% of responses should get a response
    if (random.randrange(0, 5) < 1):
    # if a certain user is detected, respond accordingly
        if (foolsList.__contains__(message.author.id)):
            await message.reply(random.choice(foolResponse))
        if (coolsList.__contains__(message.author.id)):
            await message.reply(random.choice(coolResponse))

client.run(token)