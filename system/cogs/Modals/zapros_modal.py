import disnake
from assets.enums import ChannelId, Color, RolesIds
from system.cogs.view_admin import ViewForAdmin


class Forma(disnake.ui.Modal):
    def __init__(self, arg, bot):
        self.arg = arg
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label="ваше имя и возраст?",
                placeholder="Ваш ответ",
                custom_id="name_age"
            ),
            disnake.ui.TextInput(
                label="ваш часовой пояс?",
                placeholder="Ваш ответ",
                custom_id="hours"
            ),
            disnake.ui.TextInput(
                label="был ли опыт в подобной сфере, если да - где?",
                placeholder="Ваш ответ",
                custom_id="exp"
            ),
            disnake.ui.TextInput(
                label="ваши знания запрещенной символики от 1 до 10.",
                placeholder="Ваш ответ",
                custom_id="zapretki",
                style=disnake.TextInputStyle.paragraph
            ),
            disnake.ui.TextInput(
                label="сколько времени готовы уделять серверу?",
                placeholder="Ваш ответ",
                custom_id="time_serv",
                style=disnake.TextInputStyle.paragraph
            )
        ]
        super().__init__(title=f"Заявка на {self.arg}", components=components, custom_id="zapros_modal", timeout=600)

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        name_age, hours, exp, zapretki, time_serv = (
            interaction.text_values["name_age"],
            interaction.text_values["hours"],
            interaction.text_values["exp"],
            interaction.text_values["zapretki"],
            interaction.text_values["time_serv"]
        )
        channel = await self.bot.fetch_channel(ChannelId.TARGET.value)
        embed = disnake.Embed(color=Color.GRAY)
        embed.title = f"Новая заявка на {self.arg}"
        embed.description = f"**Новая заявка от:** {interaction.author.mention}\n" \
                            f"**Id:** {interaction.author.id}\n" \
                            f"**Name:** {interaction.author.name}"
        embed.add_field(name="> Имя Возраст", value=f"```{name_age}```")
        embed.add_field(name="> Часовой Пояс", value=f"```{hours}```")
        embed.add_field(name="> Опыт был?", value=f"```{exp}```")
        embed.add_field(name="> Запретки", value=f"```{zapretki}```")
        embed.add_field(name="> Сколько уделять", value=f"```{time_serv}```")
        embed2 = disnake.Embed(color=Color.GRAY)
        embed2.title = "Ваша заявка подана!"
        embed2.description = f"{interaction.author.mention}, Ваша заявка на роль\n" \
                             f"**{self.arg}** была подана **успшено!**"
        embed2.set_footer(text="При рассмотрении вашей заявке вы будете оповещены")
        embed2.set_thumbnail(url=interaction.author.display_avatar)
        await interaction.response.defer(with_message=True, ephemeral=True)
        await interaction.followup.send(embed=embed2, ephemeral=True)
        await channel.send(embed=embed, view=ViewForAdmin(interaction.author.id, self.bot, embed))
        role = interaction.guild.get_role(RolesIds.AWAITING.value)
        await interaction.author.add_roles(role)
