import discord
import logging
import random
import codes
from Dice import dice
from codes import pre


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

@client.event
async def on_ready():
    print(f'{client.user} is now Online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(codes.prefix + 'hello'):
        await message.channel.send('Hello '+str(message.author)+'!')
    
    #Changes the prefix that is needed to run commands to the specific character and outputs the change
    if message.content.startswith(codes.prefix + 'prefix'):
        await message.channel.send('The Prefiix has been changed to: ' + pre(message.content))

    #Rolls the specificed amount and values of dice and outputs it to the same channel the command was sent in
    if message.content.startswith(codes.prefix +'r') or message.content.startswith(codes.prefix +'roll'):
        input = message.content
        if input.startswith(codes.prefix +'roll'):
            input = input.replace('oll','')
        await message.channel.send('('+str(message.author.mention)+') '+dice(input))
        await message.delete()

client.run(codes.token, log_handler=handler)