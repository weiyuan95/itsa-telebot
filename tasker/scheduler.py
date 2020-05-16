# we need to append the cwd to the sys path since we are running the Procfile
# from outside of the app module
import sys
import os
sys.path.append(os.getcwd())

from apscheduler.schedulers.blocking import BlockingScheduler
from tasker.tasks import notify_users
import logging
from worker import conn
from rq import Queue

logging.basicConfig()
# display all INFO logs so we can tell what's going on
logging.getLogger('pika').setLevel(logging.ERROR)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

sched = BlockingScheduler()
q = Queue(connection=conn)

def run_notify_users():
    q.enqueue(notify_users)

sched.add_job(func=run_notify_users)
sched.add_job(func=run_notify_users, trigger='interval', minutes=1)

sched.start()