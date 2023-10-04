import os 
from flask import Flask, request

# TOKEN=os.environ["TOKEN"]

app = Flask(__name__)

@app.route('/')
def main():
    return "DEPLOYMENT"

@app.route("/webhook/")
def webhook():
    return 'webhook'

if __name__ == "__main__":
    app.run(debug=True)
