import tkinter as tk
import customtkinter
from Frames.Mini_App_Frames import *
from Frames.New_Analysis_Frames import *
from CustomObjects import *
#from TestDataExtractor2 import *

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
        
        #Audio-Gerät speichern
        Startupsettings.selected_audio_device = self.audio_device_list_selector.v.get()
        print("Selected Device: ", Startupsettings.selected_audio_device)
        
        #Session-Name speichern und an TestDataExtractor2 weitergeben
        Startupsettings.session_name = self.session_name_selector.entry_var.get()
        print(Startupsettings.session_name)
        #Main.Set_Session_Name(Startupsettings.session_name)


        Startupsettings.working_mode = self.working_mode_selector.v.get()
        print(Startupsettings.working_mode)

        self.mini_app_window = MiniAppWindow(self.master)

        
        self.destroy()

    def on_cancel(self):
        self.destroy()


class MiniAppWindow(customtkinter.CTkToplevel):
    def __init__(self, master = None):
        super().__init__(master)

        #Fenstergröße festlegen
        window_size_x = 150
        window_size_y = 200

        #Legt Fenster in untere Rechte Bildschirmecke und verhindert das manuelle Größe verändern
        self.geometry("{}x{}+{}+{}".format(window_size_x, window_size_y, self.winfo_screenwidth() - window_size_x, self.winfo_screenheight() - window_size_y))
        self.resizable(0,0)

        self.title("Live-Analyse")
      
        #Hintergrund transparent machen, falls gewünscht (aktuell nur volle Transparenz implementiert)
              
        #self.wm_attributes("-transparent", True)
        #self.config(bg='systemTransparent')


        #Grid-Konfiguration
        self.rowconfigure(0, weight=1)
        #self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        

        
        # Toolbar ausblenden, Konflikt mit Anweisung, das Fenster immer oben ist --> auskommentiert
        #self.overrideredirect(True)

        # Fenster bleibt immer oben
        self.attributes("-topmost", True)

        #Größe-Ändern-Button
        self.button_change_width = customtkinter.CTkButton(self, text = "<", command=self.change_width)
        self.button_change_width.grid(row = 0, rowspan = 3, column = 0)
        self.button_change_width.configure(width = 20, height = 200)

        self.var = tk.BooleanVar()
        self.var.set(True)

        #Additional Info Frame
        self.additional_info_frame = AdditionalInfoFrame(self)
        self.additional_info_frame.grid(row = 0, column = 1, rowspan = 3, padx = 10, sticky = "nsew")


        
        #Toolbar-Frame

        self.toolbar_frame = customtkinter.CTkFrame(self)
        self.toolbar_frame.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "sew")

        self.toolbar_frame.columnconfigure((0,1), weight=1)

        self.quit_button = customtkinter.CTkButton(self.toolbar_frame, text="X", width= 10, command=self.quit_analysis_button_event)
        self.quit_button.grid(row =0, column = 1, padx = 5, sticky = "ew")

        self.pause_button = customtkinter.CTkButton(self.toolbar_frame, text= "II", width=10, command=self.pause_button_event)
        self.pause_button.grid(row = 0, column = 0, padx = 5, sticky = "ew")

        self.pause_var = tk.BooleanVar()
        self.pause_var.set(False)

        #Score-Frame
        self.is_blinking = False
        self.score_frame = ScoreFrame(self, self.is_blinking)
        self.score_frame.grid(row = 0, column = 2,padx = 5, sticky = "n")
        
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
    def change_width(self):
        self.current_width = self.winfo_width()
        new_width = self.current_width + 200 if self.var.get() else self.current_width - 200
        current_x = self.winfo_x()
        for i in range(self.current_width, new_width, 10 if self.var.get() else -10):
            self.geometry("{}x{}+{}+{}".format(i, self.winfo_height(),current_x + self.current_width - i,self.winfo_y()))
            self.update()
            self.after(10)
        self.var.set(not self.var.get())
        self.button_change_width.configure(text="<" if self.var.get() else ">")

    def quit_analysis_button_event(self):
        self.destroy()
    
    def pause_button_event(self):
        if self.pause_var.get():
            self.pause_button.configure(text="II")
            self.pause_var.set(False)
            
            #ScoreFrame.set_pause_event(self, is_pause=self.pause_var)
        else:
            self.pause_analysis()
            self.pause_button.configure(text=">")
            self.pause_var.set(True)
            
            #ScoreFrame.set_pause_event(self, is_pause=self.pause_var)

    def pause_analysis(self):
        print("pause")