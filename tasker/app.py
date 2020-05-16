from flask import Flask, request
import os
from os.path import join, dirname
from dotenv import load_dotenv
from tasker.bot.TeleBot import register_user, error_reply

app = Flask(__name__)
env_path = join(dirname(__file__), '..', '.env')
load_dotenv(env_path)

# receive updates from telegram on this endpoint
# since the telegram does not care about the response from this
# endpoint, anything is fine
@app.route(f'/{os.environ.get("HOOK_SECRET")}', methods=["POST"])
def parse_registrants():
    # assume that a valid update always hits the server
    data = request.json['message']
    chat_id = data['chat']['id']

    if 'text' not in data:
        error_reply(chat_id)
        return " "

    text = data['text']

    if '/register ' in text.lower():
        # the user should be entering his username after the space
        username = text.split(' ')[1]
        register_user(username, chat_id)
    else:
        error_reply(chat_id)

    return " "

if __name__ == '__main__':
    app.run()