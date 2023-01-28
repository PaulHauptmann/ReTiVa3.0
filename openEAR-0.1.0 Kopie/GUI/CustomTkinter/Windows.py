import tkinter as tk
import customtkinter
from Frames.Mini_App_Frames import *
from Frames.New_Analysis_Frames import *
from Frames.MainWindowFrames import *
from CustomObjects import *
from TestDataExtractor2 import *
from Frames.SettingsFrames import *
from Frames.MainWindowFrames import *
from MiniAppObjects import *
import threading
import random
import subprocess


class NewAnalysisWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Neue Analyse")
        #self.parent = parent

        

        

        '''
        #Erweiterte Einstellungen-Button
        self.advanced_setting_button = customtkinter.CTkButton(self, text= "Erweiterte Einstellungen...", command=self.open_advanced_button_command)
        self.advanced_setting_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "se")
        '''

        #Start-Button
        self.start_button = customtkinter.CTkButton(self, text="Start", command=self.on_ok)
        self.start_button.grid(row = 3, column = 3, padx = 20, pady = 20)

        #Abbrechen-Button
        self.cancel_button = customtkinter.CTkButton(self, text="Abbrechen", command=self.on_cancel)
        self.cancel_button.grid(row = 3, column = 2, padx = 20, pady = 20)


        #Audio Device List Frame
        self.audio_device_list_selector = AudioDeviceListFrame(self)
        self.audio_device_list_selector.grid(row = 1, column = 0, padx = 20, pady = 20)

        #Session Name Frame
        self.session_name_selector = SessionNameFrame(self)
        self.session_name_selector.grid(row = 0, column = 1, padx = 20, pady = 10)

        #Working-Mode Frame
        self.working_mode_selector = WeightsFrame(self, expand_all=False)
        self.working_mode_selector.grid(row = 1, column = 1, padx = 20, pady = 10)
        
        self.working_mode_selector.v.trace("w", lambda *args: self.on_radio_select)

        


    
    def on_radio_select(self):
        return 0
    
    
    
    
    def on_ok(self):
        
        


        #Audio-Gerät speichern
        Startupsettings.selected_audio_device = self.audio_device_list_selector.v.get()
        print("Selected Device: ", Startupsettings.selected_audio_device)
        
        #Session-Name speichern und an TestDataExtractor2 weitergeben
        Startupsettings.session_name = self.session_name_selector.entry_var.get()
        if Startupsettings.session_name != "":
            Main.Set_Session_Name(Startupsettings.session_name)
        else :
            Main.Set_Session_Name(None)

        print(Startupsettings.session_name)
        print("ABC Graphen?    " , Startupsettings.show_abc_graphs)


        # Gewichte an Backend übergeben, erst dort werden sie normiert
        Main.Get_Soll_Werte( Weights.w_emodb_anger, 
                             Weights.w_emodb_boredom, 
                             Weights.w_emodb_disgust,
                             Weights.w_emodb_fear, 
                             Weights.w_emodb_happiness, 
                             Weights.w_emodb_neutral, 
                             Weights.w_emodb_sadness,
                             Weights.w_abc_agressiv,
                             Weights.w_abc_cheerful,
                             Weights.w_abc_intoxicated,
                             Weights.w_abc_nervous,
                             Weights.w_abc_neutral,
                             Weights.w_abc_tired)




        Startupsettings.working_mode = self.working_mode_selector.v.get()
        #Weights.set_working_mode(self.working_mode_selector.v.get())
        print(Startupsettings.working_mode)
        print(Weights.working_mode)

        #print(Weights.)

        #Big Analysis Frame starten
        MainContainerFrame.show_big_analysis()

        #Starte Uhr in BigAnalysis Window
        MainContainerFrame.start_clock()
        MainContainerFrame.set_window_session_name()
        

        

        """t2 = threading.Thread(target=self.ai_loop)
        t2.start()
        print("AI_Thread")"""

        # Mini App Window starten und Main Analysis Loop fahren
        
        self.mini_app_window = MiniAppWindow(self.master)
        
        GlobalStartStop.analysis_loop = True

        #time.sleep(5)
        print("GUI Thread")

        t = threading.Thread(target=self.main_analysis_loop)
        t.start()
        print("started thread")
        print(GlobalStartStop.analysis_loop)
        
        




        #Main.Updater()
        
        self.destroy()
    


    def on_cancel(self):
        self.destroy()
        #process.kill()
        


    ##################################################
    ##################################################

    ## Where the Magic Happens! Main Schleife       ##

    ##################################################
    ##################################################

    '''def run_smilextract():
        global process
        process = subprocess.Popen(["SMILExtract", "-C", "config/emobase_live4.conf"], cwd="/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/")

    def stop_smilextract():
        process.kill()
'''


    def ai_loop(self):
        
        try:
            subprocess.run(["SMILExtract", "-C", "config/emobase_live4.conf"], cwd="/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/")
        except FileNotFoundError:
            pass







    def main_analysis_loop(self):
        while True and GlobalStartStop.analysis_loop == True:




            #Startet die Datenextraktion und alle zugehörigen Funktionen
            Main.Updater()

            print("Läuft")

            ## Mini App Window ##

            
            #Haupt-Score Update Funktion
            self.mini_app_window.linear_score_frame.indicator.update_widget(rel_y=Main.Score_Retiva)
            
            #Emotionslabel Update Funktion
            '''try:
                self.mini_app_window.additional_info_frame.emotion_label.set(Main.get_highest_EmoDb())
                self.mini_app_window.additional_info_frame.double_label.set(Main.get_highest_EmoDb(), Main.get_highest_AbcAffect())
            except AttributeError:
                pass'''
            
            try:
                self.mini_app_window.additional_info_frame.emotion_label.set("Happiness")
                self.mini_app_window.additional_info_frame.double_label.set("Happiness", "Neutral")
            except AttributeError:
                pass
            
            
            #Loi-Score Update Funktion
            self.mini_app_window.additional_info_frame.loi_indicator.update_widget(Main.Loi_Score)

            #Arousal-Score Update Funktion
            self.mini_app_window.additional_info_frame.arousal_indicator.update_widget(Main.DataArousal[-1])

            #Valence-Score Update Funktion
            self.mini_app_window.additional_info_frame.valence_indicator.update_widget(Main.DataValence[-1])

            #Redeanteil-Update Funktion
            self.mini_app_window.additional_info_frame.redeanteil.update_widget(Main.DataSpeakRatio[-1])

            #Update die Widgets im Big Analysis Window
            MainContainerFrame.update_analysis_window()

            

            time.sleep(1)







class MiniAppWindow(customtkinter.CTkToplevel):
    def __init__(self, master = None):
        super().__init__(master)

        #Fenstergröße festlegen
        window_size_x = 140
        window_size_y = 260


        #Legt Fenster in untere Rechte Bildschirmecke und verhindert das manuelle Größe verändern
        self.geometry("{}x{}+{}+{}".format(window_size_x, window_size_y, self.winfo_screenwidth() - window_size_x, self.winfo_screenheight() - window_size_y))
        #self.resizable(0,0)

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
        self.button_change_width.configure(width = 20, height = 220)

        self.var = tk.BooleanVar()
        self.var.set(True)

        #Additional Info Frame
        self.additional_info_frame = AdditionalInfoFrame(self, show_all_scales=False)
        self.additional_info_frame.grid(row = 0, column = 1, rowspan = 3, padx = 10, sticky = "nsew")


        
        #Toolbar-Frame

        self.toolbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.toolbar_frame.grid(row = 2, column = 2, padx = 5, pady = (0,5), sticky = "sew")

        self.toolbar_frame.columnconfigure((0,1), weight=1)

        self.quit_button = customtkinter.CTkButton(self.toolbar_frame, text="STOP  ▢", width= 10, command=self.quit_analysis_button_event, font=customtkinter.CTkFont(size=18, weight="bold"), hover_color="red")
        self.quit_button.grid(row =0, column = 1, padx = 5)

        
        #Score-Frame
        
        #self.score_frame = ScoreFrame(self)
        #self.score_frame.grid(row = 0, column = 2,padx = 5, sticky = "n")

        self.linear_score_frame = ScoreIndicatorFrame(self)
        self.linear_score_frame.grid(row = 0, column = 2, padx = 10, pady = (10,0), sticky = "ns")
        
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
        new_width = self.current_width + 350 if self.var.get() else self.current_width - 350
        current_x = self.winfo_x()
        for i in range(self.current_width, new_width, 10 if self.var.get() else -10):
            self.geometry("{}x{}+{}+{}".format(i, self.winfo_height(),current_x + self.current_width - i,self.winfo_y()))
            self.update()
            self.after(2)
        self.var.set(not self.var.get())
        self.button_change_width.configure(text="<" if self.var.get() else ">")

    def quit_analysis_button_event(self):
        GlobalStartStop.analysis_loop = False
        MainContainerFrame.show_archive()
        MainContainerFrame.stop_clock()
        
        print("Analyse beendet")
        self.destroy()
    
