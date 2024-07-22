import discord
from discord import app_commands
from discord.ext import commands
import json

from config import *
from core.read_data import read_data
from core.send_to_cache import send_to_cache

class PseudoRead(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author == self.bot.user:
            return
                
        content = msg.content.lower()
        
        if content == "reading cog":
            await msg.channel.send("Works")
    
    @app_commands.command(name="pseudo_read", description="Changes the data for statuses")
    async def pseudo_read(self, msg: discord.Interaction):
        if msg.user.id != OWNER_ID: return
              
        await msg.response.send_message("Reading data")
        
        send_data = await read_data(self.bot, msg)      
        await send_to_cache(msg, send_data)