import os 
from flask import Flask, request
import telegram

TOKEN='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

app = Flask(__name__)

@app.route('/')
def main():
    return "DEPLOYMENT"

@app.route("/webhook/", methods=["POST", "GET"])
def webhook():
    chat_id = 5575549228

    bot = telegram.Bot(TOKEN)

    bot.sendMessage(chat_id, "Hi")

    return 'Ok'

if __name__ == "__main__":
    app.run(debug=True)
