import tkinter
import customtkinter
from Frames import *

class NewAnalysisWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("400x200")
        self.title = "Start"

        #Start-Button
        start_button = customtkinter.CTkButton(self, text="Start")
        start_button.grid(row = 2, column = 2, padx = 20, pady = 20)

        #Audio Device List Frame
        audio_device_list_selector = AudioDeviceListFrame(self)
        audio_device_list_selector.grid(row = 0, column = 0)




