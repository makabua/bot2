# Discord Ready Bot

A Discord bot that tracks player ready status, manages game weeks, and includes a 48-hour timer for advancing weeks automatically.

## Features

- **Player Registration**: Users can register/unregister to participate
- **Ready Tracking**: Track which players are ready and which aren't
- **Week Management**: Automatically advances weeks when all players are ready
- **48-Hour Timer**: Optional timer that auto-advances the week if not everyone is ready
- **Persistent Data**: Saves all data to JSON file (survives bot restarts)
- **Status Display**: Beautiful embed showing current status

## Commands

### Ready Commands (Anyone can use these)
- `!ready_colin` - Mark Colin as ready
- `!ready_cortland` - Mark Cortland as ready
- `!ready_brady` - Mark Brady as ready
- `!ready_jack` - Mark Jack as ready
- `!ready_shoes` - Mark Shoes as ready
- `!ready_david` - Mark David as ready
- `!ready_mote` - Mark Mote as ready
- `!ready_austin` - Mark Austin as ready
- `!ready_nick` - Mark Nick as ready

### Unready Commands (Anyone can use these)
- `!unready_colin` - Mark Colin as not ready
- `!unready_cortland` - Mark Cortland as not ready
- `!unready_brady` - Mark Brady as not ready
- `!unready_jack` - Mark Jack as not ready
- `!unready_shoes` - Mark Shoes as not ready
- `!unready_david` - Mark David as not ready
- `!unready_mote` - Mark Mote as not ready
- `!unready_austin` - Mark Austin as not ready
- `!unready_nick` - Mark Nick as not ready

### Other Commands
- `!status` - View current game status (week, ready players, timer)
- `!help_ready` - Show all available commands

### Admin Commands (require Administrator permission)
- `!starttimer` - Start the 48-hour countdown timer
- `!canceltimer` - Cancel the active timer
- `!setweek <number>` - Manually set the week number
- `!resetready` - Reset all ready statuses

## How It Works

**Anyone can ready up any of the 9 players** using the `!ready_name` commands. This means:
- Colin can ready himself with `!ready_colin`
- Brady can ready Colin with `!ready_colin`
- Anyone in the server can mark anyone ready

This is useful when:
- Someone doesn't have Discord access at the moment
- Someone forgets to ready up
- One person is collecting everyone's status

## Setup Instructions

### Step 1: Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section in the left sidebar
4. Click "Add Bot"
5. Under "Privileged Gateway Intents", enable:
   - **Message Content Intent**
   - **Server Members Intent**
6. Click "Reset Token" and copy your bot token (keep this secret!)

### Step 2: Invite Bot to Your Server

1. In the Developer Portal, go to "OAuth2" → "URL Generator"
2. Select scopes:
   - `bot`
   - `applications.commands`
3. Select bot permissions:
   - Send Messages
   - Embed Links
   - Read Message History
   - Read Messages/View Channels
4. Copy the generated URL and open it in your browser
5. Select your server and authorize the bot

### Step 3: Host the Bot 24/7 (Free Cloud Hosting)

You'll need to use a **free cloud hosting service** to run the bot 24/7 without keeping your computer on. Here are the best free options:

---

#### **OPTION 1: Railway.app (EASIEST - Recommended)** ⭐

Railway offers free hosting with $5 monthly credit (enough for a Discord bot).

**Step-by-step:**

1. **Create account** at [Railway.app](https://railway.app/)
   - Sign up with GitHub

2. **Upload your bot to GitHub:**
   - Create a new repository on [GitHub.com](https://github.com/new)
   - Upload all the bot files (`discord_ready_bot.py`, `requirements.txt`, `Procfile`)

3. **Deploy on Railway:**
   - Click "New Project" in Railway
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway automatically detects it's a Python project

4. **Add your bot token:**
   - In Railway, click on your project
   - Go to "Variables" tab
   - Click "New Variable"
   - Name: `DISCORD_BOT_TOKEN`
   - Value: Paste your bot token from Step 1
   - Click "Add"

5. **Deploy:**
   - Railway will automatically build and start your bot
   - Check the "Deployments" tab to see logs
   - Your bot should appear online in Discord within 1-2 minutes!

**That's it! Your bot is now running 24/7 for free.**

---

#### **OPTION 2: Render.com (Also Free)**

Render offers free hosting for web services and background workers.

**Step-by-step:**

1. **Create account** at [Render.com](https://render.com/)

2. **Upload bot to GitHub** (same as Railway)

3. **Create new Web Service:**
   - Click "New +" → "Background Worker"
   - Connect your GitHub repository
   - Name: `discord-ready-bot`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python discord_ready_bot.py`

4. **Add environment variable:**
   - Scroll to "Environment Variables"
   - Add: `DISCORD_BOT_TOKEN` = your token
   - Click "Create Background Worker"

5. Bot will deploy automatically and run 24/7!

---

#### **OPTION 3: Replit (Browser-Based - No GitHub Needed)**

Easiest if you don't want to use GitHub, but requires a keep-alive trick.

**Step-by-step:**

1. **Create account** at [Replit.com](https://replit.com)

2. **Create new Repl:**
   - Click "+ Create Repl"
   - Choose "Python"
   - Name it whatever you want

3. **Upload files:**
   - Delete the default `main.py`
   - Click "Upload file" icon (📁)
   - Upload `discord_ready_bot.py` and `requirements.txt`

4. **Set bot token:**
   - Click the 🔒 Lock icon in left sidebar (Secrets)
   - Key: `DISCORD_BOT_TOKEN`
   - Value: Your bot token
   - Click "Add new secret"

5. **Configure to run the bot:**
   - Click the three dots ⋮ next to "Files"
   - Show hidden files
   - Edit `.replit` file:
   ```
   run = "python discord_ready_bot.py"
   ```

6. **Click the green "Run" button**
   - Bot will start!

7. **Keep it running 24/7 (Important!):**
   - Replit free tier stops after inactivity
   - Use [UptimeRobot](https://uptimerobot.com/) (free):
     - Create account
     - Add new monitor
     - Type: HTTP(s)
     - URL: Your replit URL (looks like `https://your-repl-name.username.repl.co`)
     - Monitoring interval: 5 minutes
   - UptimeRobot will ping your repl every 5 minutes keeping it alive

---

#### **Comparison:**

| Service | Difficulty | Setup Time | 100% Free? |
|---------|-----------|------------|------------|
| Railway | Easy | 5 minutes | Yes ($5/month credit) |
| Render | Easy | 5 minutes | Yes (750 hours/month) |
| Replit | Very Easy | 3 minutes | Yes (with UptimeRobot trick) |

**Recommendation:** Start with Railway - it's the simplest and most reliable for Discord bots.

### Step 4: Local Testing (Optional)

If you want to test locally first:

1. Install Python 3.8 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your bot token as environment variable:
   - **Windows**: `set DISCORD_BOT_TOKEN=your_token_here`
   - **Mac/Linux**: `export DISCORD_BOT_TOKEN=your_token_here`
4. Run the bot:
   ```bash
   python discord_ready_bot.py
   ```

## How The Bot Works

### Normal Flow
1. Anyone can ready up any of the 9 players using `!ready_name` commands
2. When ALL 9 players are ready, the bot automatically:
   - Advances to the next week
   - Resets everyone's ready status
   - Cancels any active timer

### Timer Flow
1. Admin starts timer with `!starttimer`
2. Bot monitors for 48 hours
3. If not everyone is ready when timer expires:
   - Bot announces who wasn't ready
   - Advances to next week anyway
   - Resets ready statuses

### The 9 Players
The bot tracks these 9 players:
- Colin, Cortland, Brady, Jack, Shoes, David, Mote, Austin, Nick

Anyone in your Discord server can mark any of these players as ready/not ready.

### Data Persistence
All data is saved to `bot_data.json`:
- Current week number
- List of registered users
- List of ready users
- Timer end time
- Channel ID for notifications

## Troubleshooting

**Bot doesn't respond:**
- Make sure the bot has permission to read and send messages in the channel
- Verify Message Content Intent is enabled in Developer Portal

**Timer doesn't work:**
- Make sure an admin started the timer with `!starttimer`
- The timer checks every 5 minutes (not instant)

**Bot goes offline:**
- Check your hosting service is still running
- Verify your bot token is correct
- Check hosting service logs for errors

## Customization

You can modify these values in the code:

- **Timer duration**: Change `timedelta(hours=48)` in `start_timer()` function
- **Check interval**: Change `@tasks.loop(minutes=5)` to check timer more/less frequently
- **Command prefix**: Change `command_prefix='!'` to use a different prefix

## Security Notes

- Never share your bot token publicly
- Use environment variables, not hardcoded tokens
- The bot data file contains Discord user IDs (not sensitive, but be aware)

## Support

If you encounter issues:
1. Check the bot has proper permissions
2. Verify intents are enabled in Developer Portal
3. Check hosting service logs
4. Ensure all dependencies are installed

## License

Free to use and modify for your Discord server!
