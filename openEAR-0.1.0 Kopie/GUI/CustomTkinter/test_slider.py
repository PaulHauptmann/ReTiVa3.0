import tkinter as tk
from tkinter import ttk

def update_indicator(value):
    y = int((100-value)/100*200)
    indicator.place(x=25, y=y)

root = tk.Tk()

# Create a gradient label
gradient = tk.Canvas(root, width=50, height=200)
gradient.pack()

# Create an indicator
indicator = tk.Label(gradient, width=50, height=5)
indicator.pack()

# Create a disabled slider
slider = ttk.Scale(root, from_=0, to=100, command=update_indicator, orient='horizontal',state='disable')
slider.pack()

# Set the gradient color
for i in range(0, 200, 5):
    color = "#%02x%02x%02x" % (int((200-i)/200*255), int(i/200*255), 0)
    print(color)
    gradient.create_rectangle(0, i, 50, i+5, fill=color)

root.mainloop()
