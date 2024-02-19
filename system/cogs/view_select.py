import disnake
from system.cogs.Selects.roles_select import RecruitementSelect


class ViewSelect(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)
        self.add_item(RecruitementSelect(self.bot))