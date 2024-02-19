import asyncio
import disnake
from disnake.ext import commands
from assets.databases import Database
from assets.pool import db_pool


class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.Cog.listener()
    async def on_connect(self):
        await db_pool.create_pool()
        await asyncio.sleep(1)

    @commands.Cog.listener()
    async def on_disconnect(self):
        await db_pool.close_pool()
        await asyncio.sleep(1)

    @commands.Cog.listener()
    async def on_resumed(self):
        await db_pool.create_pool()
        await asyncio.sleep(1)
    
def setup(bot):
    bot.add_cog(Listeners(bot))