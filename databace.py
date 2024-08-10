import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        fullname TEXT,
        username TEXT,
        phone_number INTEGER
    )
""")
con.commit()


async def user_data(user_id, fullname, username, phone_number):
    cur.execute("INSERT INTO users (user_id,fullname,username,phone_number) VALUES (?,?,?,?)",
                (user_id, fullname, username, phone_number))
    con.commit()


async def check_user(user_id):
    cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    if cur:
        return True
    else:
        return False
