import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

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
    if message.content.startswith("http"):
        try:
            await bot.delete_message(message)
        except:
            return

token_file = open('token.txt', 'r')
token = token_file.readline()
token_file.close()

bot.run(token)