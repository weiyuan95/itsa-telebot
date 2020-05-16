from tasker.db.connector import create_connection
from tasker.bot.TeleBot import notify_user
import logging

def notify(messages):
    """
    Sends users notification messages via telegram.
    If the user is not found in the database, it is logged. No errors are raised.
    param - messages - list of strings representing usernames and messages to be sent
    """
    for raw_message in messages:
        # messages are in a username|notification format
        username, msg = raw_message.split('|')
        user_details = _get_user_details(username)

        # a user that was not in the database was sent
        if user_details is None:
            logging.info(f'Attemped to send a message to {username} but was not found in the database')
            continue

        username, chat_id = user_details
        notify_user(chat_id, msg)

def _get_user_details(username):
    """
    Retrieves user's username and chat id
    return - None, or a tuple of username, chat_id
    """
    conn = create_connection()
    cur = conn.cursor()
    SQL_STMT = 'SELECT * FROM users WHERE username=%s'
    cur.execute(SQL_STMT, [username])

    retrieved_data = cur.fetchone()
    # close connections
    cur.close()
    conn.close()

    return retrieved_data
