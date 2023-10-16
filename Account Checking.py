import sqlite3

# Connect to the database
conn = sqlite3.connect('user_profiles.db')

# Create a cursor
cursor = conn.cursor()

# Execute an SQL query to retrieve user profiles
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

# Display the retrieved data
for user in users:
    print(f'User ID: {user[0]}, Username: {user[1]}, Password: {user[2]}')

# Close the connection
conn.close()