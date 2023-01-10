import tkinter
import customtkinter
from Frames.New_Analysis_Frames import *
from CustomObjects import *

class NewAnalysisWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Neue Analyse")

        #Start-Button
        start_button = customtkinter.CTkButton(self, text="Start", command=self.on_ok)
        start_button.grid(row = 2, column = 2, padx = 20, pady = 20)

        #Abbrechen-Button
        cancel_button = customtkinter.CTkButton(self, text="Abbrechen", command=self.on_cancel)
        cancel_button.grid(row = 2, column = 1, padx = 20, pady = 20)

        #Audio Device List Frame
        self.audio_device_list_selector = AudioDeviceListFrame(self)
        self.audio_device_list_selector.grid(row = 1, column = 0, padx = 20, pady = 20)

        #Session Name Frame
        self.session_name_selector = SessionNameFrame(self)
        self.session_name_selector.grid(row = 0, column = 1, padx = 20, pady = 20)

        #Working-Mode Frame
        self.working_mode_selector = WorkingModeFrame(self)
        self.working_mode_selector.grid(row = 1, column = 1, padx = 20, pady = 20)

    def on_ok(self):
        selected_device = self.audio_device_list_selector.v.get()
        Startupsettings.selected_audio_device = selected_device
        print("Selected Device: ", Startupsettings.selected_audio_device)
        
        Startupsettings.session_name = self.session_name_selector.entry_var.get()
        print(Startupsettings.session_name)
        
        self.destroy()

    def on_cancel(self):
        self.destroy()

