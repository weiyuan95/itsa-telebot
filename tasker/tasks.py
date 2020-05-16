from tasker.consume_queue import consume_from_queue
from tasker.helpers.notify_helper import notify
import logging

def notify_users():
    all_messages = consume_from_queue('notify')
    notify(all_messages)
    logging.info(f'{len(all_messages)} Users notified')
