import tkinter
import customtkinter

class BottomToolbarFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        #self.rowconfigure(0, weight=1)
        
        self.button_close = customtkinter.CTkButton(self,text="close",  command=self.master.destroy)
        self.button_close.grid(row = 0, column = 1, padx = 10)
        self.button_close.configure(width = 50)

       

class ScoreFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        self.score_label = customtkinter.CTkLabel(self, width=100, height=100, fg_color="green")
        self.score_label.grid(row = 0, column = 0)

