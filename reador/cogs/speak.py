import discord
from discord.ext import commands

class Speak(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author == self.bot.user:
            return
                
        content = msg.content.lower()
        
        if content == "hello":
            await msg.channel.send("Hey")
            
        if content == "close":
            await msg.channel.send("Goodbye!")
            await self.bot.close()
          