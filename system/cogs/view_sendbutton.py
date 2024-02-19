import disnake
from system.cogs.Buttons.send import SendButton


class SendView(disnake.ui.View):
    def __init__(self, arg, bot):
        self.arg = arg
        self.bot = bot
        super().__init__(timeout=None)
        self.add_item(SendButton(self.arg, self.bot))