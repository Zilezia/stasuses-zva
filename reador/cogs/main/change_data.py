import discord
from discord import app_commands
from discord.ext import commands
import json

from config import *
from core.read_data import read_data
from core.send_to_cache import send_to_cache

class ChangeData(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author == self.bot.user:
            return
                
        content = msg.content.lower()
        
        if content == "reading cog":
            await msg.channel.send("Works")
    
    # project_list = [name]

    project_list = [ "other", "ZJountries-api", "ZJountries", "playful-pandas", "kot_ml", "statuses-zva" ]
    
    status_list = [ 
        "Working", "Paused", "Finished", "Updating", "Fixing", "Nothing", "Not begun" 
    ]
    
    @app_commands.command(name="change_data", description="Changes the data for statuses")
    @app_commands.choices(
        name=[app_commands.Choice(name=project_i, value=project_i) for project_i in project_list],
        status=[app_commands.Choice(name=status_i, value=status_i) for status_i in status_list],
    )
    async def change_data(
        self, msg: discord.Interaction, 
        name: app_commands.Choice[str] = None,
        status: app_commands.Choice[str] = None, 
        url: str = None
    ):
        if msg.user.id != OWNER_ID: return
        
        await msg.response.send_message("One moment")
        
        taken_data = await read_data(self.bot, msg)
        
        if name != None and status != None:
            for item in taken_data[TABLE]:
                if item["name"] == name.value:
                    item["status"] = status.value
                    break
        elif name != None and status == None:
            pass
        elif name == None and status != None:
            pass
        else:
            pass
        
        formatted_data = json.dumps(taken_data, indent=4)
        data_channel = self.bot.get_channel(DATA_TC)
        await data_channel.send(f"\n```json\n{formatted_data}\n```")
        
        await send_to_cache(msg, taken_data)
        
        # nice