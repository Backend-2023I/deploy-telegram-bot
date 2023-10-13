import os 
from flask import Flask, request
import telegram
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

TOKEN='6631602228:AAGoRj0gPSHyGDXuLFeYTwZ7lfM-bwYclzI'

app = Flask(__name__)

@app.route('/')
def main():
    return "DEPLOYMENT"

def echo(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    text = update.message.text

    bot.sendMessage(chat_id, text)

@app.route("/webhook/", methods=["POST", "GET"])
def webhook():

    if request.method == "POST":
        bot = telegram.Bot(TOKEN)
        dp = Dispatcher(bot,update_queue=None)
        update = request.get_json()

        update = Update.de_json(update, bot)
        dp.add_handler(MessageHandler(Filters.text, echo))

        dp.process_update(update)
    else:
        return {"result": "Only post request"}

if __name__ == "__main__":
    app.run(debug=True)
