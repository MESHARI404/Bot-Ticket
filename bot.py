import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Ticket counter
ticket_counter = 1

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="تذكرة", description="إنشاء تذكرة دعم جديدة")
async def create_ticket(interaction: discord.Interaction):
    global ticket_counter
    
    # Get the guild (server)
    guild = interaction.guild
    
    # Get the member who created the ticket
    member = interaction.user
    
    # Create ticket channel name
    channel_name = f"ticket-{ticket_counter}"
    
    # Get or create "Tickets" category
    category = discord.utils.get(guild.categories, name="Tickets")
    if category is None:
        category = await guild.create_category("Tickets")
    
    # Create permissions for the ticket channel
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    
    # Create the ticket channel
    ticket_channel = await guild.create_text_channel(
        name=channel_name,
        category=category,
        overwrites=overwrites
    )
    
    # Create embed message
    embed = discord.Embed(
        title="تم إنشاء التذكرة",
        description=f"لقد تم إنشاء تذكرتك في {ticket_channel.mention}",
        color=discord.Color.green()
    )
    
    # Send confirmation message
    await interaction.response.send_message(embed=embed, ephemeral=True)
    
    # Send welcome message in the ticket channel
    welcome_embed = discord.Embed(
        title="مرحباً بكم في تذكرتك",
        description=f"مرحباً {member.mention}! يرجى وصف مشكلتك وانتظر حتى يقوم أحد أعضاء الفريق بمساعدتك.",
        color=discord.Color.blue()
    )
    
    # Create close button
    class CloseButton(discord.ui.Button):
        def __init__(self):
            super().__init__(style=discord.ButtonStyle.danger, label="اغلاق التذكرة")
            
        async def callback(self, interaction: discord.Interaction):
            await ticket_channel.delete()
    
    # Create view with close button
    view = discord.ui.View()
    view.add_item(CloseButton())
    
    await ticket_channel.send(embed=welcome_embed, view=view)
    
    # Increment ticket counter
    ticket_counter += 1

# Run the bot
bot.run(os.getenv('TOKEN')) 