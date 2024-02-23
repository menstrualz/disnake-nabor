import disnake
from assets.enums import RolesIds, Color


class AcceptButton(disnake.ui.Button):
    def __init__(self, user, bot, embed):
        self.user = user
        self.bot = bot
        self.embed = embed
        super().__init__(label="Одобрить", custom_id="accept_button")

    async def callback(self, interaction: disnake.MessageInteraction) -> None:
        user = await interaction.guild.fetch_member(self.user)
        embed = disnake.Embed(
            color=Color.GRAY, title="Ваша заявка принята!",
            description=f"{user.mention}, Ваша заявка была **принята** {interaction.author.mention}!\n"
                        "Удачи в **работе**, пупс!"
        ).set_thumbnail(url=user.display_avatar)

        try:
            await user.send(embed=embed)
        except disnake.Forbidden:
            pass

        edited_embed = self.embed.copy()
        edited_embed.set_footer(
            text=f"Рассматривает: {interaction.author.display_name}",
            icon_url=interaction.author.display_avatar
        )
        await interaction.response.edit_message(embed=edited_embed, view=None)
        role = interaction.guild.get_role(RolesIds.AWAITING.value)
        if role in user.roles:
            await user.remove_roles(role)
        await interaction.followup.send("Пользователь оповещен, не забудьте выдать роль!", ephemeral=True)
