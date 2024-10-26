import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from Bot.handlers import register_all_handlers

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Check if the token is loaded
if API_TOKEN is None:
    raise ValueError("Token is not set. Please check your .env file.")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Initialize dispatcher without the bot instance

# Register all handlers
register_all_handlers(dp)


async def main():
    """Main function to start polling."""
    try:
        await dp.start_polling(bot)  # Pass the bot instance to start_polling
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")


if __name__ == '__main__':
    asyncio.run(main())
