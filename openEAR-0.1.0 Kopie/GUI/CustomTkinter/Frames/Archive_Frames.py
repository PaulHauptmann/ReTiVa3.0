import customtkinter
import tkinter as tk
import os
from openpyxl import *

class ArchiveListFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        # define filepath
        self.filepath = "openEAR-0.1.0 Kopie/SmileArchiv"

        #Label
        self.title_label = customtkinter.CTkLabel(self, text = "Archiv: ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row = 0, column = 0, pady = 20)
        
        #Grid
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        # create listbox
        self.listbox = tk.Listbox(self, borderwidth=0)
        self.listbox.grid(row = 1, column = 0, rowspan=2, padx=10, pady=10, sticky="nsew")

        # populate listbox with Excel file names
        for file in os.listdir(self.filepath):
            if file.endswith(".xlsx"):
                self.listbox.insert(tk.END, file)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row = 0, column= 1, rowspan = 3, padx = 10, pady = 10, sticky="nsew")


        # bind listbox to open_excel_file function
        self.listbox.bind("<Button-1>", self.open_excel_file)

    def open_excel_file(self, event):
        widget = event.widget
        idx = widget.nearest(event.y)
        widget.activate(idx)
        selected_file = widget.get(idx)
        workbook = load_workbook(os.path.join(self.filepath, selected_file))
        sheet = workbook.active
        # Clear the textbox
        self.textbox.delete("1.0", tk.END)
        for row in sheet.iter_rows():
            for cell in row:
                self.textbox.insert(tk.END, cell.value)
                self.textbox.insert(tk.END, " ")
            self.textbox.insert(tk.END, "\n")