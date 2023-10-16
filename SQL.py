import sqlite3

# Create a database and a users table
conn = sqlite3.connect('user_profiles.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL)
                  ''')

conn.commit()
conn.close()