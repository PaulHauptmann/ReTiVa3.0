import tkinter
import customtkinter
from tkinter import ttk
import time
from MiniAppObjects import *

class ScoreFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        
        self.score_title=tkinter.Label(self, text="Live-Score:")
        #self.score_title=customtkinter.CTkLabel(self, text="Live-Score:")
        self.score_title.grid(row = 0, column = 0)

        self.score_label = customtkinter.CTkLabel(self, width=100, height=100,corner_radius=20, fg_color="green", text="")
        self.score_label.grid(row = 1, column = 0)
        

class ScoreIndicatorFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        self.indicator = ScoreIndicator(self)
        self.indicator.grid(row = 0, column=2, padx = 5)
        #self.indicator.set_position(0.5)



class AdditionalInfoFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        self.columnconfigure(0, weight=1)

        self.emotion_label = customtkinter.CTkLabel(self, text="Boredom", fg_color="gray50", corner_radius=10)
        self.emotion_label.grid(row = 0, column = 0)

        self.speak_ratio_label = customtkinter.CTkLabel(self, text="Redeanteil: {}".format(""))
        self.speak_ratio_label.grid(row = 1, column = 0)

        self.loi_indicator = HorizontalIndicator(self,left="Desinteresse",middle="Neutral",right="Interessiert")
        self.loi_indicator.grid(row = 2, column = 0)

        self.valence_indicator = HorizontalIndicator(self, left="Unangenehm", middle="", right="Angenehm")
        self.valence_indicator.grid(row = 3, column = 0)
        
