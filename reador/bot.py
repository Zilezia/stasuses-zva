import asyncio
import discord
from discord.ext import commands

from config import *
from cogs import *

def app():
    intents = discord.Intents.all()
    intents.members = True
    
    myID = OWNER_ID
    bot = commands.Bot(intents=intents, command_prefix='&')
    
    def is_me(interaction: discord.Interaction):
        return interaction.user.id == myID

    @bot.event
    async def on_ready():        
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands") # these i tbh pointless when ran, when locally only i think i never tried with a server or anything
        print(f'{bot.user.name} is online') # cuz well these are not outputted in the terminal
        channel = bot.get_channel(TEXT_CHANNEL)
        await channel.send(f"I'm online! <@{myID}>") # but this ofc happens bc its on discord then :>
    async def load_cogs():
        for cog in [
            # ReadData,
            PseudoRead,
            ChangeData,
            # unimportant
            Speak
        ]: 
            await bot.add_cog(cog(bot))
    
    asyncio.run(load_cogs())
    
        
    bot.run(BOT_TOKEN)

app()
