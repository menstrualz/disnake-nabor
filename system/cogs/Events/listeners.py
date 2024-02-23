from disnake.ext import commands


class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        pass

    @commands.Cog.listener()
    async def on_disconnect(self):
        pass

    @commands.Cog.listener()
    async def on_resumed(self):
        pass
    
def setup(bot):
    bot.add_cog(Listeners(bot))
