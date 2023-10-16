import tkinter as tk
from tkinter import messagebox
import subprocess


# Sample function for the login menu
def login_menu():
    # Create a tkinter window for login
    login_window = tk.Tk()
    login_window.title("Forex 100 Login")

    # Create username and password entry fields
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Check for a specific username and password
        if username == "123" and password == "123":
            login_window.destroy()
            run_test2()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def run_test2():
        try:
            subprocess.run(["python", "test2.py"])  # Replace "python" with the appropriate command to run test2.py
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack()

    login_window.mainloop()

login_menu()