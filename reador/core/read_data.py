import discord
from discord import app_commands
from discord.ext import commands
import json

from config import *
# from core.send_to_cache import send_to_cache

def rm_fir_last_lines(rd):
    fline = rd.find('\n')
    lline = rd.rfind('\n')
    return rd[fline+1:lline]

# This reads the latest data version

async def read_data(bot, msg):
    # await msg.response.send_message("Looking for latest data.")
    
    channel = bot.get_channel(DATA_TC)

    async for message in channel.history(limit=1):
        rdata = message.content
        break
    
    
    codel_rdata = rm_fir_last_lines(rdata)
    
    send_data = json.loads(codel_rdata)

    # formatted_data = json.dumps(send_data, indent=4)
    # await msg.channel.send(f"```json\n{formatted_data}\n```")
    
    return send_data