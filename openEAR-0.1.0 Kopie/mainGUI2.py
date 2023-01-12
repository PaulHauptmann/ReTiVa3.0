import sys
import tkinter as tk
import customtkinter
from time import *
import TestDataExtractor2 as T3
import time
import threading


## GUI - Imports ##

# Path added, so kann direkt auf Ordner "CustomTkinter" referenziert werden
sys.path.append('openEAR-0.1.0 Kopie/GUI/CustomTkinter')

from Windows import *
from Frames.New_Analysis_Frames import *



#Standard-Modus festlegen
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"

#Color-Theme Einstellungen aus eigener Datei übernehmen (Custom CI, muss nur in der .json Datei verändert werden)
customtkinter.set_default_color_theme('.vscode/retiva_dark-blue.json')


#Die eigentliche App
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        
        # configure window
        self.title("ReTiVA – Real-Time Voice Analytics")
        self.geometry(f"{1100}x{580}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ReTiVA", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        #Neue-Analyse-Button
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Neue Analyse", command=self.new_analysis_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        #Start-Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Start", command=self.button_starter)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        
        #Stop-Button
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Stop", command=self.button_stop_command)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        #Mini-App-Button
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text = "Mini-App", command = self.mini_app_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        
        
        # set default values
        #self.sidebar_button_1.configure(state = "disabled")
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")
        
        
        

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def new_analysis_button_event(self):
        self.new_analysis_window = NewAnalysisWindow(self)
        self.new_analysis_window.grab_set()

    def mini_app_button_event(self):
        self.mini_app_window = MiniAppWindow(self)

    
    
    


    
   

    def button_stop_command(self):
        # If the STOP button is pressed then terminate the loop
        global stop
        stop = True

    def start_command(self):
        global stop
        stop = False
        while True and not stop:
            #Textbox vollständig löschen
            self.textbox.delete("0.0", tk.END)

            #Neuen Text aus T3 einfügen
            self.textbox.insert("0.0", T3.Main.update())
            #self.textbox.insert("0.0", "Test")
            self.textbox.insert("0.0", Startupsettings.selected_audio_device)
            time.sleep(0.5)

            



    def button_starter(self):

        t = threading.Thread(target=self.start_command)
        t.start()
        
        





if __name__ == "__main__":
    app = App()
    app.mainloop()