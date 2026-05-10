import discord
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents, help_command=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    # Load các module
    await bot.load_extension("cogs.minecraft")
    await bot.load_extension("cogs.auto_check")
    await bot.load_extension("cogs.pick_role")
    
    print(f"✅ Bot: {bot.user}")
    print(f"📡 Server: {config.SERVER_IP}:{config.SERVER_PORT}")
    print(f"⏱️  Check: {config.CHECK_INTERVAL}s")
    print(f"📢 Kênh auto: {config.CHANNEL_ID}")
    print("------")

bot.run(config.TOKEN)