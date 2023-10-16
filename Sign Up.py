import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to add a new user to the database
def create_user():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username already exists
    conn = sqlite3.connect('user_profiles.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Error", "Username already exists.")
    else:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User created successfully.")

# Create the main tkinter window
root = tk.Tk()
root.title("User Profile Creation")

# Create username and password entry fields
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button to create a new user profile
create_button = tk.Button(root, text="Create User Profile", command=create_user)
create_button.pack()

root.mainloop()