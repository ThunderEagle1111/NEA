import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import random

# Sample function to generate random stock data
def generate_random_stock_data():
    data = [500 + random.uniform(-20, 20) for _ in range(100)]
    return data

# Sample function to display a stock graph
def display_stock_graph(stock_name):
    data = generate_random_stock_data()
    plt.plot(data)
    plt.title(f'{stock_name} Stock')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()

# Sample function to handle the main menu
def main_menu():
    # Create a tkinter window
    window = tk.Tk()
    window.title("Forex Trading Simulator")

    # Create buttons for each stock
    stocks = ["Stock 1", "Stock 2", "Stock 3", "Stock 4", "Stock 5"]
    for stock in stocks:
        stock_button = tk.Button(window, text=stock, command=lambda s=stock: display_stock_graph(s))
        stock_button.pack()

    # Create a leaderboard button, buy/sell buttons, etc.

    window.mainloop()

# Sample function for the login menu
class login_menu:
    def __init__(self):
        # Create a tkinter window for login
        login_window = tk.Tk()
        login_window.title("Login")

        username_label = tk.Label(login_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(login_window)
        username_entry.pack()

        password_label = tk.Label(login_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(login_window, show="*")
        password_entry.pack()

        login_button = tk.Button(login_window, text="Login", command=self.login)
        login_button.pack()

        login_window.mainloop()

    # Create username and password entry fields
    def login(self):
        username = username_entry.get()
        password = password_entry.get()

    # Check for a specific username and password
        if username == "123" and password == "123":
            login_window.destroy()
            blank_page()
        else:
            messagebox.showerror("Error", "Invalid username or password")



# Run the login menu
login_menu()

def blank_page():
    blank_window = tk.Tk()
    blank_window.title("Blank Page")

    # Create content for the blank page
    label = tk.Label(blank_window, text="Welcome to the Blank Page!")
    label.pack()

    # Add more widgets or content as needed

    blank_window.mainloop()


login_window = tk.Tk()
login_window.title("Login")

# Create and place username label and entry
username_label = tk.Label(login_window, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1)

# Create and place password label and entry
password_label = tk.Label(login_window, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_window, show="*")
password_entry.grid(row=1, column=1)

# Create and place login button
login_button = tk.Button(login_window, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

login_window.mainloop()
