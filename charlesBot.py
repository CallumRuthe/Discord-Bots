# charlesBot.py

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='mute_user')
async def mute_user(ctx, user: discord.Member):
    await discord.Member.create_dm(user)
    await discord.DMChannel.send()
    print(user)
    # print(dm.send('hi'))


bot.run(TOKEN)
