import os 
from flask import Flask, request
import telegram

TOKEN='6631602228:AAGoRj0gPSHyGDXuLFeYTwZ7lfM-bwYclzI'

app = Flask(__name__)

@app.route('/')
def main():
    return "DEPLOYMENT"

@app.route("/webhook/", methods=["POST", "GET"])
def webhook():

    if request.method == "POST":
        update = request.get_json()

        text = update['message']['text']
        chat_id = update['message']['chat']['id']

        bot = telegram.Bot(TOKEN)

        bot.sendMessage(chat_id, text)

        return 'Ok'
    else:
        return {"result": "Only post request"}

if __name__ == "__main__":
    app.run(debug=True)
