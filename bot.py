
    import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦈 Leverage Shark Bot LIVE hai! /shark likho")

async def shark(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦈 Shark Signal: BTC LONG 5x (Demo - abhi API nahi laga)")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shark", shark))
    print("Bot polling started...")
    app.run_polling()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Shark Bot is Alive")

def run_web():
    port = int(os.getenv("PORT", 10000))
    print(f"Web server on port {port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    run_bot()
