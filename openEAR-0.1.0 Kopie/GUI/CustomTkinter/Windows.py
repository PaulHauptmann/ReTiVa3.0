import tkinter
import customtkinter
from Frames import *

class NewAnalysisWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.geometry("400x200")
        self.title = "Start"

        #Start-Button
        start_button = customtkinter.CTkButton(self, text="Start", command=self.on_ok)
        start_button.grid(row = 2, column = 3, padx = 20, pady = 20)

        #Abbrechen-Button
        cancel_button = customtkinter.CTkButton(self, text="Abbrechen", command=self.on_cancel)
        cancel_button.grid(row = 2, column = 2, padx = 20, pady = 20)

        #Audio Device List Frame
        self.audio_device_list_selector = AudioDeviceListFrame(self)
        self.audio_device_list_selector.grid(row = 0, column = 0, padx = 20, pady = 20)

    def on_ok(self):
        selected_device = self.audio_device_list_selector.v.get()
        print("Selected device:", selected_device)
        self.destroy()

    def on_cancel(self):
        self.destroy()

