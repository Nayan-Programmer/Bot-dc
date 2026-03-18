import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ===== YOUR DATA =====
GAME_LINK = "https://linkurl.pk/3uU0qH-n"
SERVER_INVITE = "https://discord.com/invite/bloxfruits"

# ===== TRACKING =====
dm_users = set()
total_dms = 0


@bot.event
async def on_ready():
    print("✅ Successfully logged in!")
    print(f"🤖 Bot Name: {bot.user}")
    print("🚀 Bot is ready...\n")


# ===== SEND MESSAGE IN SERVER =====
@bot.command()
async def start(ctx):
    await ctx.send("Hosting levi fully bribed 8/12 with bh")
    print("📢 Server message sent!")


# ===== DM HANDLER =====
@bot.event
async def on_message(message):
    global total_dms

    if message.author.bot:
        return

    # Check if DM
    if isinstance(message.channel, discord.DMChannel):

        # If user already got link → ignore
        if message.author.id in dm_users:
            return

        # Add user to set
        dm_users.add(message.author.id)
        total_dms += 1

        # Send message
        await message.channel.send(
            "Yo join my ps we are 8 ppls and levi to tiki 🔥\n"
            f"{GAME_LINK}\n\n"
            f"Join our Discord too:\n{SERVER_INVITE}"
        )

        # LOGS
        print(f"📩 New DM from: {message.author}")
        print(f"📊 Total DMs: {total_dms}\n")

    await bot.process_commands(message)


bot.run("MTQ4MzgzNDI2NDEzODI4OTIzNA.GN-SRS.d5NB0MHfv9c05N5rv8oX0s4mGcuL67KBpczvco")