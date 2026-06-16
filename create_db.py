import sqlite3
import os

DB_NAME = "truthlens.db"

if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

conn = sqlite3.connect(DB_NAME)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article TEXT,
    prediction TEXT,
    confidence REAL,
    category TEXT,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database created successfully!")