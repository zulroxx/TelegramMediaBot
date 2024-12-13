from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://t.me/+2-1JeRuUBDtlMmZl")

# Main application setup
app = ApplicationBuilder().token("7601384842:AAGpEogD6U5RkDIJsyYveQSFiXn6JC1R1vo").build()  # Replace YOUR_BOT_TOKEN with your bot's token

# Add the command handler
app.add_handler(CommandHandler("start", start))

# Run the bot using polling
app.run_polling()
