import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        fullname TEXT,
        username TEXT,
        phone_number INTEGER,
        group_id INTEGER
    )
""")
con.commit()


async def user_data_insert(user_id, fullname, username, phone_number, group_id):
    cur.execute("INSERT INTO users (user_id, fullname, username, phone_number, group_id) VALUES (?, ?, ?, ?, ?)",
                (user_id, fullname, username, phone_number, group_id))
    con.commit()


async def check_user(user_id):
    a = cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    return a
