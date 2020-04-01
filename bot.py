import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio


allowed_ranks_file = open('allowed-roles.txt', 'r')
allowed_ranks = allowed_ranks_file.readlines()
ranks = [x.strip() for x in allowed_ranks]


def isImmune(author):
    for user_role in author.roles:
        for rank in ranks:
            if rank == user_role.id:
                return True
    return False


Client = discord.Client()
bot = commands.Bot(command_prefix="%")


@bot.event
async def on_ready():
    print("deletelinks bot is ready")
    print("Client: " + bot.user.name)
    print("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="I will not hold back"))


@bot.event
async def on_message(message):
    if ("http" in message.content) or ("www." in message.content) and not isImmune(message.author):
        try:
            await bot.delete_message(message)
        except:
            return

token_file = open('token.txt', 'r')
token = token_file.readline()
token_file.close()

bot.run(token)