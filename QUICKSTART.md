# Quick Start Guide - Free Cloud Hosting

This guide will get your Discord bot running 24/7 in under 10 minutes using **Railway.app** (100% free).

## What You'll Need
- Discord account
- GitHub account (free)
- Railway account (free)
- 10 minutes

---

## Step 1: Create Your Discord Bot (2 minutes)

1. Go to https://discord.com/developers/applications
2. Click **"New Application"**
3. Name it (e.g., "Ready Bot")
4. Go to **"Bot"** tab on left
5. Click **"Add Bot"**
6. Enable these under "Privileged Gateway Intents":
   - ✅ Message Content Intent
   - ✅ Server Members Intent
7. Click **"Reset Token"** and **COPY IT** (you'll need this!)

## Step 2: Invite Bot to Your Server (1 minute)

1. Go to **"OAuth2"** → **"URL Generator"**
2. Check these boxes:
   - Scopes: `bot`
   - Bot Permissions: `Send Messages`, `Embed Links`, `Read Messages/View Channels`
3. Copy the generated URL at the bottom
4. Paste it in your browser and invite bot to your server

## Step 3: Upload Files to GitHub (3 minutes)

1. Go to https://github.com and sign in
2. Click the **"+"** in top right → **"New repository"**
3. Name it `discord-ready-bot`
4. Make it Public
5. Click **"creating a new file"**
6. Name it `discord_ready_bot.py` and paste the code from the bot file
7. Click **"Commit new file"**
8. Repeat for `requirements.txt` and `Procfile`

**OR** download all files and upload them:
- Click "Add file" → "Upload files"
- Drag and drop: `discord_ready_bot.py`, `requirements.txt`, `Procfile`
- Click "Commit changes"

## Step 4: Deploy on Railway (3 minutes)

1. Go to https://railway.app
2. Click **"Login"** → Sign in with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your `discord-ready-bot` repository
6. Railway will automatically start building

## Step 5: Add Your Bot Token (1 minute)

1. Click on your project in Railway
2. Click the **"Variables"** tab
3. Click **"New Variable"**
4. Enter:
   - **Variable Name:** `DISCORD_BOT_TOKEN`
   - **Value:** Paste the token you copied in Step 1
5. Click **"Add"**

## Step 6: Check if It's Working!

1. Go to **"Deployments"** tab in Railway
2. Click on the latest deployment
3. Look at the logs - you should see: `[YourBotName] has connected to Discord!`
4. Check Discord - your bot should be **online** (green dot)!

---

## Test Your Bot

In your Discord server, type:
```
!help_ready
```

You should see a list of all commands!

Then try:
```
!ready_colin
!ready_brady
!status
```

Anyone can ready up any of the 9 players using the `!ready_name` commands!

---

## Troubleshooting

**Bot not responding?**
- Check Railway logs for errors
- Make sure Message Content Intent is enabled
- Verify bot has permissions in your Discord server

**Bot offline?**
- Check Railway deployment status
- Make sure you added the token correctly (no spaces)
- Look at Railway logs for error messages

**"Token is invalid" error?**
- Go back to Discord Developer Portal
- Reset your token
- Update it in Railway Variables

---

## Cost

✅ **100% FREE** - Railway gives you $5/month credit, and this bot uses about $0.50-$1/month

Your bot will run 24/7 without your computer being on!

---

## Next Steps

- Customize the bot code
- Add more commands
- Invite friends to register
- Start using the ready tracking system!

## Getting Help

Check the full README.md for:
- Complete command list
- Advanced features
- Alternative hosting options
- Customization guide
