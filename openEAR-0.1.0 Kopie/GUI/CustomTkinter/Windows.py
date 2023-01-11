import tkinter
import customtkinter
from Frames.Mini_App_Frames import *
from Frames.New_Analysis_Frames import *
from CustomObjects import *

class NewAnalysisWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Neue Analyse")

        #Start-Button
        self.start_button = customtkinter.CTkButton(self, text="Start", command=self.on_ok)
        self.start_button.grid(row = 2, column = 2, padx = 20, pady = 20)

        #Abbrechen-Button
        self.cancel_button = customtkinter.CTkButton(self, text="Abbrechen", command=self.on_cancel)
        self.cancel_button.grid(row = 2, column = 1, padx = 20, pady = 20)

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
        
        Startupsettings.selected_audio_device = self.audio_device_list_selector.v.get()
        print("Selected Device: ", Startupsettings.selected_audio_device)
        
        Startupsettings.session_name = self.session_name_selector.entry_var.get()
        print(Startupsettings.session_name)

        Startupsettings.working_mode = self.working_mode_selector.v.get()
        print(Startupsettings.working_mode)
        
        self.destroy()

    def on_cancel(self):
        self.destroy()


class MiniAppWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Fenster Einstellungen
        self.geometry("200x150")
        self.resizable(0,0)

        
        # Toolbar ausblenden, Konflikt mit Anweisung, das Fenster immer oben ist --> auskommentiert
        #self.overrideredirect(True)

        # Fenster bleibt immer oben
        self.attributes("-topmost", True)

        #Expand-Button
        self.button_expand = customtkinter.CTkButton(self,)

        #Toolbar-Frame
        self.toolbar_frame = BottomToolbarFrame(self)
        self.toolbar_frame.grid(row = 2, column = 0, columnspan = 3, sticky = "s")
        
        '''
        #Drag-Handle zum verschieben des Fensters
        self.grip = customtkinter.CTkLabel(self, fg_color="gray25")
        self.grip.grid(row = 0, column = 0, columnspan = True)
    
        self.grip.bind("<ButtonPress-1>", self.start_move)
        self.grip.bind("<ButtonRelease-1>", self.stop_move)
        self.grip.bind("<B1-Motion>", self.do_move)
        
        '''

    
    '''
    
    ## Drag-Bedienung zum verschieben des Fensters via Drag-Bar ##
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")
    
    '''


    ## Buttons ##
    def close_window(self):
        self.destroy()
