from tasker.db.connector import create_connection

def register(username, chat_id):
    """
    A function that registers all the users into the database
    """
    conn = create_connection()
    cur = conn.cursor()

    SQL_STMT = 'INSERT INTO users (username, chat_id) VALUES (%s, %s)'

    cur.execute(SQL_STMT, (username, str(chat_id)))

    conn.commit()

    # close connections
    cur.close()
    conn.close()

def all_lowercase(username):
    for ch in username:
        if ch.isupper():
            return False
    return True
