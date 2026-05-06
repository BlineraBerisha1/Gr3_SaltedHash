import sqlite3

DB_NAME = "users.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password_hash TEXT,
        salt TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_user(username, password_hash, salt):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                       (username, password_hash, salt))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def get_user(username):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    conn.close()
    return user

def get_all_users():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()

    conn.close()
    return users