import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

name = "your bot name"
reactionBot = commands.Bot(command_prefix='xD')
 
@reactionBot.event
async def on_ready():
    print (f"========================\n{name} Bot Is Ready\n========================")
 
 
@reactionBot.event
async def on_message(message):
    if(message.channel.id == "  "): # channel id
        await reactionBot.add_reaction(message, "   ") # custom emoji id
        await reactionBot.add_reaction(message, "   ") # custom emoji id
 
reactionBot.run("   ") # bot token
