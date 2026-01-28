import discord
from discord.ext import commands, tasks
import json
import os
from datetime import datetime, timedelta
import asyncio

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Data storage
DATA_FILE = 'bot_data.json'

class GameTracker:
    def __init__(self):
        self.data = self.load_data()
        
    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {
            'week': 1,
            'ready_users': [],
            'registered_users': {},  # Maps user_id to display name
            'timer_end': None,
            'channel_id': None
        }
    
    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def register_user(self, user_id, display_name):
        """Register a user with their display name"""
        user_id = str(user_id)
        self.data['registered_users'][user_id] = display_name
        self.save_data()
    
    def is_registered(self, user_id):
        """Check if a user is registered"""
        return str(user_id) in self.data['registered_users']
    
    def ready_up(self, user_id):
        user_id = str(user_id)
        if not self.is_registered(user_id):
            return False, "You're not authorized to use this bot. Contact an admin."
        
        if user_id in self.data['ready_users']:
            return False, "You're already readied up!"
        
        self.data['ready_users'].append(user_id)
        self.save_data()
        return True, "You've readied up!"
    
    def unready(self, user_id):
        user_id = str(user_id)
        if user_id in self.data['ready_users']:
            self.data['ready_users'].remove(user_id)
            self.save_data()
            return True
        return False
    
    def all_ready(self):
        if not self.data['registered_users']:
            return False
        return set(self.data['ready_users']) == set(self.data['registered_users'].keys())
    
    def reset_ready(self):
        self.data['ready_users'] = []
        self.save_data()
    
    def advance_week(self):
        self.data['week'] += 1
        self.reset_ready()
        self.save_data()
    
    def start_timer(self):
        end_time = datetime.now() + timedelta(hours=48)
        self.data['timer_end'] = end_time.isoformat()
        self.save_data()
    
    def cancel_timer(self):
        self.data['timer_end'] = None
        self.save_data()
    
    def get_time_remaining(self):
        if not self.data['timer_end']:
            return None
        
        end_time = datetime.fromisoformat(self.data['timer_end'])
        remaining = end_time - datetime.now()
        
        if remaining.total_seconds() <= 0:
            return timedelta(0)
        
        return remaining
    
    def set_channel(self, channel_id):
        self.data['channel_id'] = channel_id
        self.save_data()

tracker = GameTracker()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    check_timer.start()

@bot.event
async def on_message(message):
    # Auto-register users on first interaction
    if message.author.bot:
        return
    
    # Check if user needs to be registered
    if not tracker.is_registered(message.author.id):
        # Check if they're one of the authorized users
        authorized_names = ['colin', 'cortland', 'brady', 'jack', 'shoes', 'david', 'mote', 'austin', 'nick']
        display_name = message.author.display_name.lower()
        username = message.author.name.lower()
        
        # Check if their name matches any authorized name
        for auth_name in authorized_names:
            if auth_name in display_name or auth_name in username:
                tracker.register_user(message.author.id, message.author.display_name)
                await message.channel.send(f'✅ {message.author.mention} has been auto-registered!')
                break
    
    await bot.process_commands(message)

@bot.command(name='ready', help='Mark yourself as ready')
async def ready(ctx):
    success, message = tracker.ready_up(ctx.author.id)
    await ctx.send(f'{ctx.author.mention}: {message}')
    
    if success and tracker.all_ready():
        tracker.advance_week()
        tracker.cancel_timer()
        await ctx.send(f'🎉 Everyone is ready! Advancing to **Week {tracker.data["week"]}**!')
        await ctx.send('Ready status has been reset. Use !ready when you\'re ready for the next week.')

@bot.command(name='unready', help='Mark yourself as not ready')
async def unready(ctx):
    if tracker.unready(ctx.author.id):
        await ctx.send(f'{ctx.author.mention} is no longer ready.')
    else:
        await ctx.send(f'{ctx.author.mention}, you weren\'t readied up.')

@bot.command(name='status', help='Check current game status')
async def status(ctx):
    embed = discord.Embed(title="Game Status", color=discord.Color.blue())
    embed.add_field(name="Week", value=tracker.data['week'], inline=False)
    
    ready_count = len(tracker.data['ready_users'])
    total_count = len(tracker.data['registered_users'])
    embed.add_field(name="Ready Players", value=f"{ready_count}/{total_count}", inline=False)
    
    if tracker.data['registered_users']:
        ready_list = []
        for user_id, display_name in tracker.data['registered_users'].items():
            status_emoji = "✅" if user_id in tracker.data['ready_users'] else "❌"
            ready_list.append(f"{status_emoji} {display_name}")
        embed.add_field(name="Players", value="\n".join(ready_list), inline=False)
    
    time_remaining = tracker.get_time_remaining()
    if time_remaining is not None:
        if time_remaining.total_seconds() > 0:
            hours = int(time_remaining.total_seconds() // 3600)
            minutes = int((time_remaining.total_seconds() % 3600) // 60)
            embed.add_field(name="Time Remaining", value=f"{hours}h {minutes}m", inline=False)
        else:
            embed.add_field(name="Time Remaining", value="⏰ Timer expired!", inline=False)
    else:
        embed.add_field(name="Timer", value="Not active", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='starttimer', help='Start the 48-hour timer (admin only)')
@commands.has_permissions(administrator=True)
async def start_timer(ctx):
    tracker.start_timer()
    tracker.set_channel(ctx.channel.id)
    await ctx.send('⏰ 48-hour timer started! If not everyone is ready when time expires, the week will advance automatically.')

@bot.command(name='canceltimer', help='Cancel the active timer (admin only)')
@commands.has_permissions(administrator=True)
async def cancel_timer(ctx):
    tracker.cancel_timer()
    await ctx.send('Timer cancelled.')

@bot.command(name='setweek', help='Set the current week number (admin only)')
@commands.has_permissions(administrator=True)
async def set_week(ctx, week: int):
    if week < 1:
        await ctx.send('Week must be 1 or greater.')
        return
    
    tracker.data['week'] = week
    tracker.save_data()
    await ctx.send(f'Week set to {week}.')

@bot.command(name='resetready', help='Reset all ready statuses (admin only)')
@commands.has_permissions(administrator=True)
async def reset_ready(ctx):
    tracker.reset_ready()
    await ctx.send('All ready statuses have been reset.')

@bot.command(name='adduser', help='Manually add a user (admin only)')
@commands.has_permissions(administrator=True)
async def add_user(ctx, member: discord.Member):
    tracker.register_user(member.id, member.display_name)
    await ctx.send(f'✅ {member.mention} has been manually registered!')

@bot.command(name='removeuser', help='Remove a user (admin only)')
@commands.has_permissions(administrator=True)
async def remove_user(ctx, member: discord.Member):
    user_id = str(member.id)
    if user_id in tracker.data['registered_users']:
        del tracker.data['registered_users'][user_id]
        if user_id in tracker.data['ready_users']:
            tracker.data['ready_users'].remove(user_id)
        tracker.save_data()
        await ctx.send(f'❌ {member.mention} has been removed.')
    else:
        await ctx.send(f'{member.mention} was not registered.')

@bot.command(name='listusers', help='List all registered users (admin only)')
@commands.has_permissions(administrator=True)
async def list_users(ctx):
    if not tracker.data['registered_users']:
        await ctx.send('No users registered yet.')
        return
    
    user_list = '\n'.join([f'• {name}' for name in tracker.data['registered_users'].values()])
    await ctx.send(f'**Registered Users:**\n{user_list}')

@bot.command(name='help_ready', help='Show all available commands')
async def help_ready(ctx):
    embed = discord.Embed(title="Ready Bot Commands", color=discord.Color.green())
    embed.add_field(name="!ready", value="Mark yourself as ready", inline=False)
    embed.add_field(name="!unready", value="Mark yourself as not ready", inline=False)
    embed.add_field(name="!status", value="Check game status", inline=False)
    embed.add_field(name="**Admin Commands**", value="─────────────────", inline=False)
    embed.add_field(name="!starttimer", value="Start 48-hour timer", inline=False)
    embed.add_field(name="!canceltimer", value="Cancel active timer", inline=False)
    embed.add_field(name="!setweek <number>", value="Set week number", inline=False)
    embed.add_field(name="!resetready", value="Reset all ready statuses", inline=False)
    embed.add_field(name="!adduser @user", value="Manually add a user", inline=False)
    embed.add_field(name="!removeuser @user", value="Remove a user", inline=False)
    embed.add_field(name="!listusers", value="List all registered users", inline=False)
    await ctx.send(embed=embed)

@tasks.loop(minutes=5)
async def check_timer():
    time_remaining = tracker.get_time_remaining()
    
    if time_remaining is not None and time_remaining.total_seconds() <= 0:
        # Timer expired
        if tracker.data['channel_id']:
            channel = bot.get_channel(tracker.data['channel_id'])
            if channel:
                not_ready = []
                for user_id, display_name in tracker.data['registered_users'].items():
                    if user_id not in tracker.data['ready_users']:
                        try:
                            user = await bot.fetch_user(int(user_id))
                            not_ready.append(user.mention)
                        except:
                            not_ready.append(display_name)
                
                if not_ready:
                    await channel.send(f'⏰ 48-hour timer expired! The following players were not ready: {", ".join(not_ready)}')
                
                tracker.advance_week()
                tracker.cancel_timer()
                await channel.send(f'Advancing to **Week {tracker.data["week"]}**. Ready status has been reset.')

# Run the bot
if __name__ == '__main__':
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if not TOKEN:
        print("Error: DISCORD_BOT_TOKEN environment variable not set!")
        print("Please set your Discord bot token as an environment variable.")
    else:
        bot.run(TOKEN)
