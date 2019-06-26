#Feel free to use, modify etc. 
#This bot runs on a
#General Public License 3.0

#importing the discord.py library
import discord
from discord.ext import commands
import json

#loading the info about the token and command prefix from a json file
try:
    with open("config.json") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("[ERROR] There is no file named config.json!")

token = data["token"]
prefix = data["prefix"]

if(token == ""):
    print("[ERROR] There is no token attached to your bot! Go to discordapp.com/developers/applications and copy it to your json file.")

#creating an instance of discord client
client = discord.Client()

@client.event #when the bot is ready it will execute this function
async def on_ready():
    print("Logged in as {0.user}".format(client))
    print("[VERSION] Official 2019.6.1 Release (ALPHA)") #info about the bot version

@client.event #bot will execute this functions when someone will send a message
async def on_message(message):
    if(message.author == client.user): #if the message author is bot don't respond
        return
    if(message.content.startswith(prefix + "ping")): #ping command
        await message.channel.send("Pong!")
    if(message.content.startswith(prefix + "hello")): #hello command
        await message.channel.send("Hello! I'm Photon, a discord bot written using Discord.py library. For more info please visit github.com/AleX4270/PhotonBot")


client.run(token) #and at the end let's run the bot
