import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Store your bot token in an .env file

# Replace with your actual Discord server and role IDs
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))
NEW_MEMBER_ROLE_ID = int(os.getenv("NEW_MEMBER_ROLE_ID"))
MEMBER_ROLE_ID = int(os.getenv("MEMBER_ROLE_ID"))

# Enable necessary intents
intents = discord.Intents.default()
intents.members = True  # Required for member role management
intents.guilds = True   # Required for guild-related events
intents.message_content = True  # Fixes the warning about message content

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """Runs when the bot is ready."""
    print(f"Logged in as {bot.user} and connected to Discord!")

@bot.event
async def on_member_join(member):
    """Assigns the 'New Member' role when someone joins."""
    guild = member.guild
    role = discord.utils.get(guild.roles, id=NEW_MEMBER_ROLE_ID)

    if role:
        await member.add_roles(role)
        try:
            await member.send("Welcome! Please change your nickname to access the server.")
        except discord.Forbidden:
            print(f"Could not send a DM to {member.name}.")
    else:
        print("New Member role not found!")

@bot.event
async def on_member_update(before, after):
    """Checks if the user has changed their nickname and assigns full access."""
    if before.nick != after.nick and after.nick is not None:
        guild = after.guild
        new_member_role = discord.utils.get(guild.roles, id=NEW_MEMBER_ROLE_ID)
        member_role = discord.utils.get(guild.roles, id=MEMBER_ROLE_ID)

        if new_member_role and member_role and new_member_role in after.roles:
            await after.remove_roles(new_member_role)
            await after.add_roles(member_role)
            try:
                await after.send("Thanks for changing your nickname! You now have full access.")
            except discord.Forbidden:
                print(f"Could not send a DM to {after.name}.")
        else:
            print("Roles not found or user does not have the new member role.")

# Run the bot
bot.run(TOKEN)
