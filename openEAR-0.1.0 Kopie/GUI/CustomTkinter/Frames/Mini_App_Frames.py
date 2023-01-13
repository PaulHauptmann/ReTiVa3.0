import tkinter
import customtkinter
from tkinter import ttk
import time

class ScoreFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        
        self.score_title=tkinter.Label(self, text="Live-Score:")
        #self.score_title=customtkinter.CTkLabel(self, text="Live-Score:")
        self.score_title.grid(row = 0, column = 0)

        self.score_label = customtkinter.CTkLabel(self, width=100, height=100,corner_radius=20, fg_color="green", text="")
        self.score_label.grid(row = 1, column = 0)
        

    def set_pause_event(self, is_pause):
        self.pause = is_pause

        



class AdditionalInfoFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        self.columnconfigure(0, weight=1)

        self.emotion_label = customtkinter.CTkLabel(self, text="Boredom", fg_color="gray50", corner_radius=10)
        self.emotion_label.grid(row = 0, column = 0)

        self.speak_ratio_label = customtkinter.CTkLabel(self, text="Redeanteil: {}".format(""))
        self.speak_ratio_label.grid(row = 1, column = 0)
        
