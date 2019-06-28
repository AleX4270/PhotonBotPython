#Feel free to use, modify etc. 
#This bot runs on a
#General Public License 3.0

#You can use this code, but remember to always mention the author(me) and the name of the bot which uses this code originally.

#importing the discord.py library
import discord
from discord.ext import commands
import json
import random

#loading the info about the token and command prefix from a json file
try:
    with open("config.json") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("[ERROR] There is no file named config.json!")

token = data["token"]
prefix = data["prefix"]

if(token == ""): #if token is empty print error
    print("[ERROR] There is no token attached to your bot! Go to discordapp.com/developers/applications and copy it to your json file.")
    

#creating an instance of discord client

bot = commands.Bot(command_prefix="?")
bot.remove_command("help")

@bot.event #when the bot is ready it will execute this function
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("[VERSION] Official 2019.6.1 Release") #info about the bot version

    await bot.change_presence(activity=discord.Game("2019.6.1|?help"))

#list for ask command
answers = ("Yes", "No", "I don't think so...", "Definitely!", "Hard to say...", "I have scanned my database and the answer is YES!", "I prefer not to answer for your question... ", "Surely, the answer is no.")

rep = {}

#commands

@bot.command(pass_context=True)
async def say(ctx):                  #say command
    msg = str(ctx.message.content)
    nmsg = msg.replace("?say", "")
    await ctx.message.delete()
    await ctx.send(nmsg)

@bot.command()
async def ping(ctx):                #ping command
    await ctx.send("Pong!")

@bot.command()
async def info(ctx):                #info command
    await ctx.send("```PhotonBot, fully written in Discord.py. Original PhotonBot can be used only on ValHack Team server. For more info please visit github.com/AleX4270/PhotonBot```")

@bot.command()
async def users(ctx):   #users command
    server = bot.get_guild(397751793721016320)
    await ctx.send("```This server has got: {0} members```".format(len(server.members)))

@bot.command() 
async def ver(ctx): #ver command
    embed = discord.Embed(title = "Bot Version", description = "Shows info about bot version, last update etc.", color=0x2fd558)
    embed.add_field(name = "Version", value = "2019.6.1", inline = False)
    embed.add_field(name = "Last Update", value = "28.06.2019", inline = False)
    embed.add_field(name = "Testing", value = "filipton12", inline = False)
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx): #help command
    embed = discord.Embed(title = "Help", description = "Shows a list of available commands and info about them", color=0xeede17)
    embed.add_field(name = "?ping", value = "Bot will just respondw with Pong", inline = False)
    embed.add_field(name = "?info", value = "Shows info about the bot", inline = False)
    embed.add_field(name = "?users", value = "Shows the number of members on the server", inline = False)
    embed.add_field(name = "?ver", value = "Shows info about actual bot version, last update etc...", inline = False)
    embed.add_field(name = "?ask", value = "Description hidden", inline = False)
    embed.add_field(name = "?helpop", value = "Only for the bot administration", inline = False)
    await ctx.send(embed=embed)

@bot.command()
async def ask(ctx): #ask command
    msg = str(ctx.message.content)
    nmsg = msg.replace("?ask", "")

    if("?" not in nmsg):
        await ctx.send("Is that a question?")
        return

    if(nmsg == ""):
        await ctx.send("I can't see your question...")
        return

    ans = random.randint(1,7)
    await ctx.send(answers[ans])

@bot.command()
@commands.has_role("Photon Bot Admin")
async def status(ctx): #status command
    msg = str(ctx.message.content)
    nmsg = msg.replace("?status", "")
    await bot.change_presence(activity = discord.Game(nmsg))
    await ctx.message.delete()

@bot.command()
@commands.has_role("Photon Bot Admin")
async def helpop(ctx): #helpop command
    embed = discord.Embed(title = "Helpop", description = "Shows info about commands which are available only for the bot administration.", color=0x2fd558)
    embed.add_field(name = "?status", value = "Changes the status of the bot", inline = False)
    embed.add_field(name = "?report", value = "?report <reported player mention> (Reason). Keep in mind that report system is in Beta version.", inline = False)
    embed.add_field(name = "?replist", value = "Displays the list of reported users.", inline = False)
    embed.add_field(name = "?repclear", value = "Clears the list of reported users.", inline = False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role("Photon Bot Admin")
async def report(ctx, user: discord.Member): #report command
    idUser = user.id
    mUser = user.mention
    msg = ctx.message.content
    msg = msg.replace(str(mUser), "")
    msg = msg.replace("?report", "")

    if(msg == ""):
        await ctx.send("There is no reason!")
        return

    await ctx.send("User " + user.mention + " has been reported. Reason:" + "**" + msg + "**")

    rep[idUser] = msg
    with open("reports.json", "w") as json_file:
        try:
            json.dump(rep, json_file)
        except FileNotFoundError:
            print("[ERROR] There is no file called reports.json!")

@bot.command()
@commands.has_role("Photon Bot Admin")
async def replist(ctx): #replist command
    with open("reports.json", "r") as json_file:
        try:
            rep = json.load(json_file)
        except FileNotFoundError:
            print("[ERROR] There is no file called reports.json!")
    
    if(not rep):
        await ctx.send("**There aren't any reported users on the list.**")
        return

    await ctx.send("**Reported Users:**")
    for x in rep:
        await ctx.send("<@" + x + ">" + " Reason:" + "**" + rep[x] + "**") 

    

@bot.command()
@commands.has_role("Photon Bot Admin")
async def repclear(ctx): #repclear command
    rep = {}
    with open("reports.json", "w") as json_file:
        try:
            json.dump(rep, json_file)
        except FileNotFoundError:
            print("[ERROR] There is no file called reports.json!")

    await ctx.send("**Reports List has been cleared!**")


bot.run(token) #starting the bot









