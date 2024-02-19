from system.cogs.utilities import NaborStart
from system.cogs.callback import Command


cogs = (
    NaborStart,
    Command
)

def setup(bot):
    for cog in cogs:
        bot.add_cog(cog(bot)) 
        for command in cog.get_application_commands(self=cog):
            print(f"загружена команда /{command.name}")