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

# The 9 players
PLAYERS = {
    'colin': 'Colin',
    'cortland': 'Cortland',
    'brady': 'Brady',
    'jack': 'Jack',
    'shoes': 'Shoes',
    'david': 'David',
    'mote': 'Mote',
    'austin': 'Austin',
    'nick': 'Nick'
}

class GameTracker:
    def __init__(self):
        self.data = self.load_data()
        self.initialize_players()
        
    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {
            'week': 1,
            'ready_users': [],
            'timer_end': None,
            'channel_id': None
        }
    
    def initialize_players(self):
        """Ensure all 9 players exist in the data"""
        # This doesn't add them to ready_users, just ensures we track them
        pass
    
    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def ready_up(self, player_name):
        """Mark a player as ready by their name"""
        player_name = player_name.lower()
        
        if player_name not in PLAYERS:
            return False, f"Unknown player: {player_name}"
        
        if player_name in self.data['ready_users']:
            return False, f"{PLAYERS[player_name]} is already readied up!"
        
        self.data['ready_users'].append(player_name)
        self.save_data()
        return True, f"{PLAYERS[player_name]} has readied up!"
    
    def unready(self, player_name):
        """Mark a player as not ready"""
        player_name = player_name.lower()
        
        if player_name not in PLAYERS:
            return False, f"Unknown player: {player_name}"
        
        if player_name in self.data['ready_users']:
            self.data['ready_users'].remove(player_name)
            self.save_data()
            return True, f"{PLAYERS[player_name]} is no longer ready."
        return False, f"{PLAYERS[player_name]} wasn't readied up."
    
    def all_ready(self):
        """Check if all 9 players are ready"""
        return len(self.data['ready_users']) == len(PLAYERS)
    
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

# Create individual ready commands for each player
@bot.command(name='ready_colin', help='Mark Colin as ready')
async def ready_colin(ctx):
    success, message = tracker.ready_up('colin')
    await ctx.send(message)
    await check_all_ready(ctx)

@bot.command(name='ready_cortland', help='Mark Cortland as ready')
async def ready_cortland(ctx):
    success, message = tracker.ready_up('cortland')
    await ctx.send(message)
    await check_all_ready(ctx)

@bot.command(name='ready_brady', help='Mark Brady as ready')
async def ready_brady(ctx):
    success, message = tracker.ready_up('brady')
    await ctx.send(message)
    await check_all_ready(ctx)

@bot.command(name='ready_jack', help='Mark Jack as ready')
async def ready_jack(ctx):
    success, message = tracker.ready_up('jack')
    await ctx.send(message)
    await check_all_ready(ctx)

@bot.command(name='ready_shoes', help='Mark Shoes as ready')
async def ready_shoes(ctx):
    success, message = tracker.ready_up('shoes')
    await ctx.send(message)
    await check_all_ready(ctx)

@bot.command(name='ready_david', help='Mark David as ready')
async def ready_david(ctx):
    success, message = tracker.ready_up('david')
    await ctx.send(message)
    await check_all_ready(ctx)

@bot.command(name='ready_mote', help='Mark Mote as ready')
async def ready_mote(ctx):
    success, message = tracker.ready_up('mote')
    await ctx.send(message)
    await check_all_ready(ctx)

@bot.command(name='ready_austin', help='Mark Austin as ready')
async def ready_austin(ctx):
    success, message = tracker.ready_up('austin')
    await ctx.send(message)
    await check_all_ready(ctx)

@bot.command(name='ready_nick', help='Mark Nick as ready')
async def ready_nick(ctx):
    success, message = tracker.ready_up('nick')
    await ctx.send(message)
    await check_all_ready(ctx)

# Unready commands
@bot.command(name='unready_colin', help='Mark Colin as not ready')
async def unready_colin(ctx):
    success, message = tracker.unready('colin')
    await ctx.send(message)

@bot.command(name='unready_cortland', help='Mark Cortland as not ready')
async def unready_cortland(ctx):
    success, message = tracker.unready('cortland')
    await ctx.send(message)

@bot.command(name='unready_brady', help='Mark Brady as not ready')
async def unready_brady(ctx):
    success, message = tracker.unready('brady')
    await ctx.send(message)

@bot.command(name='unready_jack', help='Mark Jack as not ready')
async def unready_jack(ctx):
    success, message = tracker.unready('jack')
    await ctx.send(message)

@bot.command(name='unready_shoes', help='Mark Shoes as not ready')
async def unready_shoes(ctx):
    success, message = tracker.unready('shoes')
    await ctx.send(message)

@bot.command(name='unready_david', help='Mark David as not ready')
async def unready_david(ctx):
    success, message = tracker.unready('david')
    await ctx.send(message)

@bot.command(name='unready_mote', help='Mark Mote as not ready')
async def unready_mote(ctx):
    success, message = tracker.unready('mote')
    await ctx.send(message)

@bot.command(name='unready_austin', help='Mark Austin as not ready')
async def unready_austin(ctx):
    success, message = tracker.unready('austin')
    await ctx.send(message)

@bot.command(name='unready_nick', help='Mark Nick as not ready')
async def unready_nick(ctx):
    success, message = tracker.unready('nick')
    await ctx.send(message)

async def check_all_ready(ctx):
    """Check if everyone is ready and advance week if so"""
    if tracker.all_ready():
        tracker.advance_week()
        tracker.cancel_timer()
        await ctx.send(f'🎉 Everyone is ready! Advancing to **Week {tracker.data["week"]}**!')
        await ctx.send('Ready status has been reset. Use !ready_name commands to ready up for the next week.')

@bot.command(name='status', help='Check current game status')
async def status(ctx):
    embed = discord.Embed(title="Game Status", color=discord.Color.blue())
    embed.add_field(name="Week", value=tracker.data['week'], inline=False)
    
    ready_count = len(tracker.data['ready_users'])
    total_count = len(PLAYERS)
    embed.add_field(name="Ready Players", value=f"{ready_count}/{total_count}", inline=False)
    
    ready_list = []
    for player_key, player_name in PLAYERS.items():
        status_emoji = "✅" if player_key in tracker.data['ready_users'] else "❌"
        ready_list.append(f"{status_emoji} {player_name}")
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

@bot.command(name='help_ready', help='Show all available commands')
async def help_ready(ctx):
    embed = discord.Embed(title="Ready Bot Commands", color=discord.Color.green())
    embed.add_field(name="Ready Commands", value="Mark someone as ready:", inline=False)
    ready_cmds = "\n".join([f"`!ready_{name.lower()}`" for name in PLAYERS.values()])
    embed.add_field(name="", value=ready_cmds, inline=False)
    
    embed.add_field(name="Unready Commands", value="Mark someone as not ready:", inline=False)
    unready_cmds = "\n".join([f"`!unready_{name.lower()}`" for name in PLAYERS.values()])
    embed.add_field(name="", value=unready_cmds, inline=False)
    
    embed.add_field(name="Other Commands", value="`!status` - Check game status", inline=False)
    embed.add_field(name="**Admin Commands**", value="─────────────────", inline=False)
    embed.add_field(name="!starttimer", value="Start 48-hour timer", inline=False)
    embed.add_field(name="!canceltimer", value="Cancel active timer", inline=False)
    embed.add_field(name="!setweek <number>", value="Set week number", inline=False)
    embed.add_field(name="!resetready", value="Reset all ready statuses", inline=False)
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
                for player_key, player_name in PLAYERS.items():
                    if player_key not in tracker.data['ready_users']:
                        not_ready.append(player_name)
                
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
