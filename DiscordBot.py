import discord, datetime, random
from discord.ext.commands import Bot
from datetime import datetime as dt

bot = Bot(command_prefix="!")
current_time = dt.now().strftime('%H:%M:%S')
current_date = dt.now().strftime('%Y-%m-%d')

user_token = "YOUR TOKEN HERE"


#   Events
@bot.event
async def on_ready():
    print("[x] Online")

# Message edit notice to be finished
# @bot.event
# async def on_message_edit(before, after):
#     return await bot.say("Old: {}\nNew: {}".format(before, after))
        #'**{}** in channel `#{}` edited their message:\nFrom: {}\nTo: {}'.format(after.author.name, after.channel.name, before.content, after.content))


# Commands

    # Hello world
@bot.command()
async def hello(*args):
    if str(args) == "()":
        return await bot.say("Hello, world!")
    else:
        return await bot.say("Hello, {}!".format(*args))

    # Time and date
@bot.command()
async def time():
    return await bot.say("The time is: {}\nThe date is: {}"\
    .format(current_time,current_date))

    # Echo
@bot.command()
async def echo(*args):
    say_this = ""
    for i in args:
        say_this += i + " "
    return await bot.say(say_this)

    # Roll the dice
@bot.command()
async def roll(*args):
    rand_numbers = []
    if str(args) == "()":
        rand_numbers.append(random.randint(1,6))
    elif not int(*args) >= 6:
        for i in range(int(*args)):
            rand_numbers.append(random.randint(1,6))
    else:
        for i in range(6):.append(random.randint(1,6))
    numbers = "".join(str(rand_numbers))
    return await bot.say("You rolled: {}".format(numbers[1:-1]))

print("[ ] Starting")
bot.run(user_token)

# For inviting the bot to the channel use:
# https://discordapp.com/oauth2/authorize?client_id=YOUR_ID_HERE&scope=bot&permissions=0
# The Client ID can be found on the same page as token
