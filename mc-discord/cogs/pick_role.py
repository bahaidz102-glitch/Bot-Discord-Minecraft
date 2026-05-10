import discord
from discord.ext import commands
import config

class RoleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label=config.ROLE_LABEL,
        emoji=config.ROLE_EMOJI,
        style=discord.ButtonStyle.green,
        custom_id="pick_role_minecraft"
    )
    async def pick_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = interaction.guild.get_role(config.ROLE_ID)
        if not role:
            await interaction.response.send_message("❌ Không tìm thấy role!", ephemeral=True)
            return

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"✅ Đã **gỡ** role {role.mention}", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"✅ Đã **thêm** role {role.mention}", ephemeral=True)

class PickRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Đăng ký view khi bot khởi động"""
        self.bot.add_view(RoleView())

    @commands.command(name="setup_role")
    @commands.has_permissions(administrator=True)
    async def setup_role(self, ctx):
        """Tạo nút pick role"""
        embed = discord.Embed(
            title="🎭 Pick Role Minecraft",
            description=f"Nhấn nút **{config.ROLE_EMOJI} {config.ROLE_LABEL}** để nhận/gỡ role!\n\n"
                        f"🟢 Bấm lần 1: Thêm role\n"
                        f"🔴 Bấm lần 2: Gỡ role",
            color=discord.Color.green()
        )
        embed.set_footer(text=config.BOT_NAME)
        await ctx.send(embed=embed, view=RoleView())

async def setup(bot):
    await bot.add_cog(PickRole(bot))