import tkinter as tk
from tkinter import PhotoImage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from itertools import count
from matplotlib.animation import FuncAnimation

# Sample function to generate random stock data
def generate_random_stock_data():
    data = [100 + random.uniform(-20, 20) for _ in range(100)]
    return data

# Sample function to update and display a live stock graph
def update_live_stock_graph(i):
    data = generate_random_stock_data()
    ax.clear()
    ax.plot(data)
    ax.set_title(f"Stock Price")
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    canvas.draw()

# Create the main tkinter window
root = tk.Tk()
root.title("Live Stock Graph")

# Create a matplotlib figure and axis for the live graph
fig, ax = plt.subplots()
ax.set_title("Stock Price")
ax.set_xlabel('Time')
ax.set_ylabel('Price')

# Create a canvas for the live graph
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Use Matplotlib's FuncAnimation to create a live updating graph
ani = FuncAnimation(fig, update_live_stock_graph, blit=False, interval=2500)

root.mainloop()