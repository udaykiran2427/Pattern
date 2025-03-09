# Pattern Bot - Auto Role Manager

## Overview
This Discord bot automatically assigns roles to new members and grants full access once they change their nickname.

## Features
- Assigns a **New Member** role when a user joins the server.
- Monitors nickname changes and upgrades the user to a **Member** role upon change.
- Sends a welcome message prompting users to change their nickname.
- Uses `.env` file for secure token and configuration management.

## Requirements
- Python 3.8+
- `discord.py` library
- `python-dotenv` for environment variable management

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/udaykiran2427/Pattern.git
   cd Pattern
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add:
   ```env
   DISCORD_BOT_TOKEN=your_bot_token_here
   DISCORD_GUILD_ID=your_guild_id_here
   NEW_MEMBER_ROLE_ID=your_new_member_role_id_here
   MEMBER_ROLE_ID=your_member_role_id_here
   ```

## Running the Bot
Execute the following command to run the bot:
```bash
python bot.py
```
## License
This project is licensed under the MIT License.

## Fun Fact
I named my bot **Pattern** as a reference to *Pattern* from *The Stormlight Archive*.
