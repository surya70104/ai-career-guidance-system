import os
import sqlite3

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(
    "database/users.db",
    check_same_thread=False
)


cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,

    phone TEXT,
    linkedin TEXT,
    github TEXT,
    location TEXT,
    college TEXT,
    degree TEXT,
    skills TEXT,
    objective TEXT,
    projects TEXT,
    certifications TEXT,

    avatar TEXT
)
""")

conn.commit()