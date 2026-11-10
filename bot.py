import asyncio
import os
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# It reads the token securely from Render's Environment Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def handle_incoming_source(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
  raw_text = update.message.text or update.message.caption or ""
  codes = list(dict.fromkeys(re.findall(r"NG-[A-Za-z0-9]{6,10}", raw_text)))

  if not codes:
    await update.message.reply_text("No NG- codes found in that message.")
    return

  await update.message.reply_text(
      f"Found {len(codes)} codes! Open Nusuk 'Your keys' screen now. Starting"
      " in 5 seconds..."
  )
  await asyncio.sleep(5)

  for code in codes:
    await update.message.reply_text(code)
    await asyncio.sleep(5)


def run_bot():
  app = ApplicationBuilder().token(BOT_TOKEN).build()
  app.add_handler(
      MessageHandler(
          filters.TEXT & (~filters.COMMAND), handle_incoming_source
      )
  )
  app.run_polling()
