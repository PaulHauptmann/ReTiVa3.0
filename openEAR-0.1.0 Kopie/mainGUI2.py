import sys
import tkinter as tk
import customtkinter
from time import *
import TestDataExtractor2 as T
import time
import threading


## GUI - Imports ##

# Path added, so kann direkt auf Ordner "CustomTkinter" referenziert werden
sys.path.append('openEAR-0.1.0 Kopie/GUI/CustomTkinter')

from Windows import *
from Frames.New_Analysis_Frames import *
from Frames.Archive_Frames import *
from Frames.SettingsFrames import *
from Frames.MainWindowFrames import *



#Standard-Modus festlegen
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

#Color-Theme Einstellungen aus eigener Datei übernehmen (Custom CI, muss nur in der .json Datei verändert werden)
#customtkinter.set_default_color_theme('.vscode/retiva_dark-blue.json')
customtkinter.set_default_color_theme('.vscode/retiva_all-grey.json')



#Die eigentliche App
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        global stop

        # Fenster Bildschirmfüllend starten
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        #self.geometry(f"{1100}x{580}")
        
        # configure window
        self.title("ReTiVA – Real-Time Voice Analytics")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
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

        #Einstellungen-Button
        self.sidebar_button_settings = customtkinter.CTkButton(self.sidebar_frame, text="Einstellungen", command=self.show_settings_button_command)
        self.sidebar_button_settings.grid(row=4, column=0, padx=20, pady=10)

        #Archiv-Button
        self.sidebar_button_archive = customtkinter.CTkButton(self.sidebar_frame, text= "Archiv", command=self.show_archive_button_command)
        self.sidebar_button_archive.grid(row = 5, column = 0, padx = 20, pady = 10)
        
        #Mini-App-Button
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text = "Mini-App", command = self.mini_app_button_event)
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=10)



        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        
        # create textbox
        #self.textbox = ArchiveListFrame(self)
        #self.textbox.grid(row=0, column=1, padx=20, pady=20,rowspan = 3, sticky="nsew")
        #self.settings_frame = SettingsFrame(self)
        #self.settings_frame.grid(row = 0, column = 1, padx = 20, pady = 20, rowspan = 3, sticky = "nsew")
        #self.score_frame = SliderScoreFrame(self)
        #self.score_frame.grid(row = 0, column = 1, rowspan = 4, sticky = "nsew")




        ## Haupt - Frame für Anzeige diverser Funktionen
        
        self.main_frame = MainContainerFrame(self)
        self.main_frame.configure(fg_color = "transparent")
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.grid(row = 0, column = 1, rowspan = 4, padx = 20, pady = 20, sticky = "nsew")
    
        
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

    def show_settings_button_command(self):
        self.main_frame.show_settings()

    def show_archive_button_command(self):
        self.main_frame.show_archive()

    

    
    
    


    
   

    def button_stop_command(self):
        # If the STOP button is pressed then terminate the loop
        GlobalStartStop.analysis_loop = False

    '''
    def start_command(self):
        global stop
        stop = False
        #T3.Main.Set_Session_Name("test")
        while True and not stop:
            #Textbox vollständig löschen
            self.textbox.textbox.delete("0.0", tk.END)

            #Neuen Text aus T3 einfügen
            #self.textbox.textbox.insert("0.0", T3.Main.get_new_filename())
            #self.textbox.textbox.insert("0.0", "Test")
            T.Main.Updater()
            self.textbox.textbox.insert("0.0", T.Main.Loi_Score)
            #self.textbox.insert("0.0", Startupsettings.selected_audio_device)
            time.sleep(0.5)
    '''
            


    #Thread der Main While True Schleife ausführt
    def button_starter(self):

        '''t = threading.Thread(target=self.start_command)
        t.start()'''
        GlobalStartStop.analysis_loop = True

        t = threading.Thread(target=self.main_analysis_loop)
        t.start()
        print("started thread")
        print(GlobalStartStop.analysis_loop)

        
        

    '''def button_starter(self):

        window = AdvancedSettingsWindow(self)


    '''


    def main_analysis_loop(self):
        while True and GlobalStartStop.analysis_loop == True:

                    #T.Main.Updater()

                    print(Main.DataLength)
                    

                    time.sleep(0.5)


'''t = threading.Thread(target=main_analysis_loop)
t.start()
print("started thread")
'''








if __name__ == "__main__":
    app = App()
    app.mainloop()