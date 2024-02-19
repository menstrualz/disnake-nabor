import disnake
from assets.enums import RolesIds
from system.cogs.Modals.zapros_modal import Forma


class SendButton(disnake.ui.Button):
    def __init__(self, arg, bot):
        self.arg = arg
        self.bot = bot
        super().__init__(label="Подать заявку", custom_id="send_button")

    async def callback(self, interaction: disnake.MessageInteraction) -> None:
        role = interaction.guild.get_role(RolesIds.AWAITING.value)
        if role in interaction.author.roles:
            await interaction.response.send_message("У вас уже **есть** поданная **заявка**, наберитесь терпения!", ephemeral=True)
        else:
            await interaction.response.send_modal(Forma(self.arg, self.bot))