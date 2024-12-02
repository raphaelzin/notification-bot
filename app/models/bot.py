#!/usr/bin/env python
import logging
import os
from dotenv import load_dotenv

from telegram import ForceReply, Update, Message, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
botToken = os.getenv('TELEGRAM_BOT_TOKEN')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

bot = Bot(botToken)

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    chatIdTail = ""
    if update.message and update.message.chat and update.message.chat.id:
        chatIdTail = f"\nOut conversation id is: {update.message.chat.id}"

    await update.message.reply_html(
        rf"Hi {user.mention_html()}!" + chatIdTail,
        reply_markup=ForceReply(selective=True),
    )

async def send_message(message, chat_id) -> Message | None:
    async with bot:
        return await bot.send_message(chat_id, message)

# async def register_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     if update.message and update.message.chat and update.message.chat.id:
#         save_recipient(update.effective_user.full_name, update.message.chat.id)

def run_bot() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(botToken).concurrent_updates(True).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CommandHandler("register_me", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)