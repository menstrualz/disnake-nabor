import disnake
from assets.enums import Color
from system.cogs.view_sendbutton import SendView


class RecruitementSelect(disnake.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        options = [
            disnake.SelectOption(label="Заявка на Support", value="Support"),
            disnake.SelectOption(label="Заявка на Helper", value="Helper"),
            disnake.SelectOption(label="Заявка на Moderator", value="Moderator"),
            disnake.SelectOption(label="Заявка на Control", value="Control"),
            disnake.SelectOption(label="Заявка на Creative", value="Creative"),
            disnake.SelectOption(label="Заявка на EventMaker", value="EventMaker"),
            disnake.SelectOption(label="Заявка на TribuneMod", value="TribuneMod"),
            disnake.SelectOption(label="Заявка на Close Maker", value="CloseMaker"),
            disnake.SelectOption(label="Заявка на MediaScope", value="MediaScope"),
        ]

        super().__init__(placeholder="Выберите должность", options=options, min_values=0, max_values=1, custom_id="recruitement_select")

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            arg = interaction.values[0]
            embed = disnake.Embed(color=Color.GRAY)
            embed.title = f"Набор на должность {arg}"
            embed.description = "**Что вы получите от нас:**\n" \
                                "- 50 монеток за дополнительную смену\n" \
                                "- Розыгрыши нитро в нашем чате\n" \
                                "- Доступ в Стафф-чаты и ценный опыт в данной сфере\n" \
                                "- Интересные и весёлые обучения от наших кураторов\n" \
                                "- Семейный обстановка, ламповая атмосфера\n" \
                                "- Активный и дружественный коллектив\n" \
                                "**Что требуется от вас:**\n" \
                                "- Полных 16 лет\n" \
                                "- Умение общаться с аудиторией\n" \
                                "- Адекватность и знание правил сервера\n" \
                                "- Желание помогать развитию проекта\n" \
                                "*Так же, если у вас не было опыта в данной сфере, мы с радостью будем готовы дать вам шанс на то, чтобы вы испытали себя в чём-то новом*\n" \

            await interaction.response.send_message(embed=embed, view=SendView(arg, self.bot), ephemeral=True)