import threading
from flask import Flask
from bot import run_bot

app = Flask(__name__)


@app.route("/")
def home():
  return "Nusuk Telegram Bot is active and running 24/7!"


def start_flask():
  # Render assigns a dynamic port, default to 10000 if local
  port = int(os.environ.get("PORT", 10000))
  app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
  import os

  # Start the Telegram bot in a background thread
  bot_thread = threading.Thread(target=run_bot)
  bot_thread.start()

  # Start the Flask web server on the main thread
  start_flask()