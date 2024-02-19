import disnake
from system.cogs.Buttons.accept import AcceptButton
from system.cogs.Buttons.cancel import CancelButton
from system.cogs.Buttons.sobes import SobesButton



class ViewForAdmin(disnake.ui.View):
    def __init__(self, user, bot, embed):
        self.member = user
        self.bot = bot
        self.embed = embed
        super().__init__(timeout=None)
        self.add_item(AcceptButton(self.member, self.bot, self.embed))
        self.add_item(SobesButton(self.member, self.bot, self.embed))
        self.add_item(CancelButton(self.member, self.bot, self.embed))