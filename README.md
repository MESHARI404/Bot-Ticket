
# The Code Was Created By HR Development

# Discord Ticket Bot

A simple Discord bot that creates and manages support tickets in a designated category.

## Features

- Create tickets using slash command `/ticket`
- Automatically creates a private channel for each ticket
- Close ticket button
- Organized ticket channels in a dedicated category

## Setup Instructions

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Create a Discord bot and get your token:

   - Go to https://discord.com/developers/applications
   - Create a New Application
   - Go to the "Bot" section
   - Create a bot and copy the token
   - Enable the following Privileged Gateway Intents:
     - Message Content Intent
     - Server Members Intent

3. Edit the `.env` file:

   - Replace `your_bot_token_here` with your actual bot token

4. Invite the bot to your server:

   - Go to OAuth2 > URL Generator
   - Select the following scopes:
     - `bot`
     - `applications.commands`
   - Select the following bot permissions:
     - Manage Channels
     - Read Messages/View Channels
     - Send Messages
     - Manage Messages
     - Embed Links
     - Read Message History
   - Use the generated URL to invite the bot

5. Run the bot:

```bash
python bot.py
```

## Usage

- Use `/ticket` to create a new support ticket
- A new private channel will be created under the "Tickets" category
- Use the "Close Ticket" button to delete the ticket channel when done
