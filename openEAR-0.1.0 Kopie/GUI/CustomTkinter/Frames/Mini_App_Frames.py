import tkinter
import customtkinter
from tkinter import ttk
import time
from MiniAppObjects import *
from PIL import Image, ImageTk


## Vertikale Ampel für Emotionsscore

class ScoreIndicatorFrame(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        self.configure(fg_color = "transparent")

        self.indicator = ScoreIndicator(self)
        self.indicator.grid(row = 0, column=2, padx = 5)
        #self.indicator.set_position(0.5)


## Zusätzliche Informationen

class AdditionalInfoFrame(customtkinter.CTkFrame):
    def __init__(self, *args, show_all_scales:bool, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #self.emotion_label = customtkinter.CTkLabel(self, text="Boredom", fg_color="gray50", corner_radius=10)
        #self.emotion_label.grid(row = 0, column = 0)

        if Startupsettings.show_dual_emotions:
            self.double_label = DualEmotions(self)
            self.double_label.grid(row = 0, column = 0,sticky = "new", padx = 30, pady = 10)
            self.double_label.set("Anger", "Tired")
        else:
            self.emotion_label = EmotionwithEmoji(self)
            self.emotion_label.grid(row = 0, column = 0, sticky = "new", padx = 60, pady = 10)
            self.emotion_label.set("Sadness")
        

            self.loi_indicator = HorizontalIndicator(self,left="Desinteresse",middle="Neutral",right="Interessiert")
            self.valence_indicator = HorizontalIndicator(self, left="Unangenehm", middle="", right="Angenehm")
            self.arousal_indicator = HorizontalIndicator(self, left= "Deaktivierend", middle="", right="Aktivierend")
        

        if show_all_scales:
            self.loi_indicator.grid(row = 2, column = 0)
            self.valence_indicator.grid(row = 3, column = 0)
            self.arousal_indicator.grid(row = 4, column = 0)
        else:
            if Startupsettings.loi_scale == 1:
                self.loi_indicator.grid(row = 2, column = 0)

            if Startupsettings.valence_scale == 1:
                self.valence_indicator.grid(row = 3, column = 0)
                print("Valence:", Startupsettings.valence_scale)

            if Startupsettings.arousal_scale == 1:
                self.arousal_indicator.grid(row = 4, column = 0)

        self.redeanteil = HorizontalIndicator(self, left="Redeanteil: ", middle="50%", right="100%")
        self.redeanteil.grid(row = 5, column = 0)
        
