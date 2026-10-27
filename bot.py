import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("🦈 Shark Bot ONLINE! /shark dabao")

async def shark(update, context):
    await update.message.reply_text("🦈 Test Signal: BTC LONG 5x - Demo mode")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shark", shark))
    app.run_polling()

if __name__ == "__main__":
    main()
