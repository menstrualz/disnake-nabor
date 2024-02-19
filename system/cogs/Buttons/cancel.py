import disnake
from assets.enums import Color, RolesIds


class CancelButton(disnake.ui.Button):
    def __init__(self, user, bot, embed):
        self.user = user
        self.bot = bot
        self.embed = embed
        super().__init__(label="Отказать", custom_id="cancel_button")

    async def callback(self, interaction: disnake.MessageInteraction) -> None:
        user = await interaction.guild.fetch_member(self.user)
        embed = disnake.Embed(color=Color.GRAY)
        embed.title = "Вам отказано в заявке!"
        embed.description = f"{user.mention}, Вам **отказали** в заявке!\n" \
                             "попробуйте в **следующий** раз!"
        embed.set_thumbnail(url=user.display_avatar)
        await user.send(embed=embed)
        edited_embed = self.embed.copy()
        edited_embed.set_footer(text=f"Рассматривает: {interaction.author.name}", icon_url=interaction.author.avatar_url)
        await interaction.response.edit_message(embed=edited_embed, view=None)
        role = interaction.guild.get_role(RolesIds.AWAITING.value)
        if role in user.roles:
            await user.remove_roles(role)
            await interaction.followup.send("Пользователь был оповещен об отказе в заявке.", ephemeral=True)
        else:
            return interaction.followup.send