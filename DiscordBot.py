import discord, datetime
from discord.ext.commands import Bot
from datetime import datetime as dt

bot = Bot(command_prefix="!")
current_time = dt.now().strftime('%H:%M:%S')
current_date = dt.now().strftime('%Y-%m-%d')

user_token = "YOUR TOKEN HERE"


#   Events
@bot.event
async def on_read():
    print("Client logged in")

@bot.event
async def on_message_edit(before, after):
    if after.content:
        bot.say("{} just edited his message.".format(author))


#   Commands
@bot.command()
async def hello(*args):
    return await bot.say("Hello, world!")

@bot.command()
async def time():
    return await bot.say("The time is: {}\nThe date is: {}"\
    .format(current_time,current_date))

@bot.command()
async def echo(message):
    return await bot.say(message)



print("[x] Running")
bot.run(user_token)

# For inviting the bot to the channel use:
# https://discordapp.com/oauth2/authorize?client_id=YOUR_ID_HERE&scope=bot&permissions=0
# The Client ID can be found on the same page as token
