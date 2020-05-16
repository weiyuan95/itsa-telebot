import os
import requests as r
import logging
from tasker.helpers.register_helper import register, all_lowercase

BASE_URL = f'https://api.telegram.org/bot{os.getenv("API_KEY")}'
SEND_MESSAGE_URL = BASE_URL + '/sendMessage'

def _auth_check():
    """
    Checks if the api key provided is valid or not
    """
    get_bot_url = f'{BASE_URL}/getMe'
    resp = r.post(get_bot_url)

    return resp.json()

def _reply(chat_id, msg):
    """
    Sends a reply to the user based on the specified message
    param chat_id - int
    param msg - str
    """

    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "markdown"
    }

    resp = r.post(SEND_MESSAGE_URL, json=payload)
    
    if resp.status_code != 200:
        logging.error(f'Not able to send message for chat id {chat_id}. {resp}')
        logging.error(f'{SEND_MESSAGE_URL}')

def register_user(username, chat_id):
    """
    Triggers a reply to the user when a user is trying to register
    param username - str
    param chat_id - int
    """
    REGISTER_REPLY = "Thank you for registering! You will now receive notifcations on this chat."
    INVALID_USERNAME_REPLY = "Please try registering again and ensure that your username is all lower case. Thank you!"

    # Usernames cannot have uppercase chars, since postgres makes a distinction between upper and lower case.
    # We could have the case where usernames like Claud and claud are unique.
    # We want to keep all lowercase usernames to keep things simple.
    if not all_lowercase(username):
        _reply(chat_id, INVALID_USERNAME_REPLY)
        return

    try:
        register(username, chat_id)
        _reply(chat_id, REGISTER_REPLY)
    except:
        error_reply(chat_id)

def error_reply(chat_id):
    """
    Triggers a reply to the user when the bot is sent something it doesnt understand
    param chat_id - int
    """
    ERROR_REPLY = "You have entered something invalid. Please only use `/register <username>`"

    _reply(chat_id, ERROR_REPLY)

def notify_user(chat_id, notification):
    _reply(chat_id, notification)
