import discord
from discord.ext import commands
import logging
import requests
import json

with open('path_to_file/config.json', 'r') as f:
    data = json.load(f)
    token = data[0]

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.presences = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'⭐ Bot has logged in as {bot.user}')

@bot.event
async def on_member_update(before, after):
    if before.activity != after.activity:
        channel = bot.get_channel(1008072678210539670)
        await channel.send("Damnnnn")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.slash_command()
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")

bot.run(token)