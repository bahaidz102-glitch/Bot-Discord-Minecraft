import discord
from discord.ext import commands
from mcstatus import JavaServer
from datetime import datetime
import config

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="status", aliases=["st"])
    async def status(self, ctx):
        """Kiểm tra trạng thái server Minecraft"""
        try:
            server = JavaServer.lookup(f"{config.SERVER_IP}:{config.SERVER_PORT}")
            s = server.status()
            
            embed = discord.Embed(title="🟢 Server Online", color=discord.Color.green())
            embed.add_field(name="🌐 IP", value=f"`{config.SERVER_IP}:{config.SERVER_PORT}`", inline=False)
            embed.add_field(name="👥 Người chơi", value=f"{s.players.online}/{s.players.max}", inline=True)
            embed.add_field(name="⏱️ Ping", value=f"{round(s.latency)}ms", inline=True)
            embed.add_field(name="📋 Version", value=s.version.name, inline=True)
            
            if s.players.online > 0 and s.players.sample:
                players = "\n".join([f"• {p.name}" for p in s.players.sample[:10]])
                if len(s.players.sample) > 10:
                    players += f"\n...và {len(s.players.sample) - 10} người khác"
                embed.add_field(name="🎮 Đang chơi", value=players, inline=False)
            
            embed.timestamp = datetime.now()
            embed.set_footer(text=config.BOT_NAME)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title="🔴 Server Offline",
                description=f"Không thể kết nối tới `{config.SERVER_IP}:{config.SERVER_PORT}`",
                color=discord.Color.red(),
                timestamp=datetime.now()
            )
            embed.set_footer(text=config.BOT_NAME)
            await ctx.send(embed=embed)

    @commands.command(name="players", aliases=["pl", "online"])
    async def players(self, ctx):
        """Danh sách người chơi đang online"""
        try:
            server = JavaServer.lookup(f"{config.SERVER_IP}:{config.SERVER_PORT}")
            s = server.status()
            
            if s.players.online > 0 and s.players.sample:
                p_list = "\n".join([f"• {p.name}" for p in s.players.sample])
                embed = discord.Embed(
                    title=f"👥 Người chơi ({s.players.online}/{s.players.max})",
                    description=p_list,
                    color=discord.Color.blue()
                )
            else:
                embed = discord.Embed(
                    title="👥 Không có ai online",
                    description="Server đang trống!",
                    color=discord.Color.orange()
                )
            embed.set_footer(text=f"{config.SERVER_IP}:{config.SERVER_PORT}")
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title="🔴 Server Offline", color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command(name="help", aliases=["h", "cmd"])
    async def help_cmd(self, ctx):
        """Menu trợ giúp"""
        embed = discord.Embed(title="📋 Lệnh Bot Minecraft", color=discord.Color.blue())
        embed.add_field(name="!status / !st", value="Kiểm tra trạng thái server", inline=False)
        embed.add_field(name="!players / !pl", value="Xem danh sách người chơi", inline=False)
        embed.add_field(name="!setup_role", value="(Admin) Tạo nút pick role", inline=False)
        embed.add_field(name="!help", value="Hiển thị menu này", inline=False)
        embed.set_footer(text=f"{config.BOT_NAME} | {config.SERVER_IP}:{config.SERVER_PORT}")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Minecraft(bot))