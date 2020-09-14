# bot.py
import os
import random
import discord
import datetime
from dotenv import load_dotenv

def calcTime(name, timeSaid):
    if name in dict:
        return str(timeSaid*dict[name])
    return str(timeSaid)

def update(name, timeNow):
    timeSince = time -timeNow
    minutessince = int(timeSince.total_seconds() / 60)

dict = {
  "": "",
  "model": "",
  "year":
}
time = 0
timeOrginal = 0
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    number = [int(s) for s in message.content.split() if s.isdigit()]
    if len(number) == 1:
        channel = client.get_channel(755118905801965628)
        await channel.send("The estimated wait time for " + str(message.author.display_name) + " is " + calcTime(message.author, number[0]) + " minutes")
        timeOrginal = number[0]
        time = datetime.datetime.now()

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel and after.channel != None and before.channel == None:
        update(member, datetime.datetime.now())

client.run(TOKEN)