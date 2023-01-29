import tkinter as tk
from tkinter import filedialog
import os
from openpyxl import *

def open_excel_file(event):
    widget = event.widget
    idx = widget.nearest(event.y)
    widget.activate(idx)
    selected_file = widget.get(idx)
    workbook = load_workbook(os.path.join(filepath, selected_file))
    sheet = workbook.active
    # Clear the textbox
    textbox.delete("1.0", tk.END)
    for row in sheet.iter_rows():
        for cell in row:
            textbox.insert(tk.END, cell.value)
            textbox.insert(tk.END, " ")
        textbox.insert(tk.END, "\n")


root = tk.Tk()
root.title("Excel File Browser")

# define filepath
filepath = "openEAR-0.1.0 Kopie/SmileArchiv"

# create listbox
listbox = tk.Listbox(root)
listbox.pack(side=tk.LEFT)

# populate listbox with Excel file names
for file in os.listdir(filepath):
    if file.endswith(".xlsx"):
        listbox.insert(tk.END, file)

# create textbox
textbox = tk.Text(root, width=50, height=30)
textbox.pack(side=tk.RIGHT)

# bind listbox to open_excel_file function
listbox.bind("<Button-1>", open_excel_file)


root.mainloop()
