import os

from bot.client import create_bot
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

create_bot().run(discord_token)
