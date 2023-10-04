import telegram
import os 
from flask import Flask, request

TOKEN="6631602228:AAGoRj0gPSHyGDXuLFeYTwZ7lfM-bwYclzI"
bot = telegram.Bot(TOKEN)

url = "https://backend2023i.pythonanywhere.com/webhook/"
print(bot.set_webhook(url))

# print(bot.delete_webhook())
# print(bot.get_webhook_info())
