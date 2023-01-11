import tkinter
import customtkinter

class BottomToolbarFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)
        
        self.button_close = customtkinter.CTkButton(self,text="close",  command=self.master.destroy)
        self.button_close.grid(row = 0, column = 1)

        self.button_expand = customtkinter.CTkButton(self, text="text2")
        self.button_expand.grid(row = 0, column = 0)