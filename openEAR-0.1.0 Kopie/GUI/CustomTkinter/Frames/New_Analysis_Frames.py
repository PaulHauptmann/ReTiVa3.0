import tkinter as tk
import customtkinter
import listaudiodevices
from CustomObjects import *
from TestDataExtractor2 import *



## Frame, das die Audio-Geräteauswahl enthält. Ruft die Funktion get_input_device() auf und erzeugt dann
## für jedes Gerät einen RadioButton

class AudioDeviceListFrame (customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,  **kwargs)

        self.header_name = "Audio-Geräteauswahl"

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row = 0, column = 0, padx=10, pady = 20)

        self.devices = listaudiodevices.get_input_devices()
        #print(self.devices)


        self.v = customtkinter.StringVar()
        self.v.set(self.devices[0][1])
        self.device_radios = []
        for index, device in enumerate(self.devices, start= 1):
            device_radio = customtkinter.CTkRadioButton(self, text=device[1], variable=self.v, value=device[1])
            device_radio.grid(row = index, column = 0, padx=10, pady = 10)
            self.device_radios.append(device_radio)
        
        #self.device_radios[0].select()


## Frame, das einen Session-Name erfragt. Dieser wird erst in Windows.py in die Variable session_name 
## vom Typ Startupsettings geschrieben.

class SessionNameFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,  **kwargs)
        

        self.header = customtkinter.CTkLabel(self, text="Optionalen Session-Name vergeben: ")
        self.header.pack(padx=10, pady = 5, anchor = "n")


        self.entry_var= tk.StringVar()
        self.session_input = customtkinter.CTkEntry(self, textvariable=self.entry_var, width=400, height=30, placeholder_text="Name hier eingeben... ")
        self.session_input.pack(padx = 10, pady = 10, anchor = "s")


## Frame, in dem der gewünschte Modus der Analyse festgelegt werden kann

class WeightsFrame(customtkinter.CTkFrame):
    def __init__(self, master = None, parent = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.parent = parent

        self.header = customtkinter.CTkLabel(self, text="Konfiguration der Analyse")
        self.header.grid(row = 0, column = 1, padx=10, pady = 5)


        ## Voreinstellung für Gewichte auswählen 

        self.v = customtkinter.StringVar()
        
        self.workingmode_pitchsession = customtkinter.CTkRadioButton(self, text="Pitch - Session", variable=self.v, value= "Pitch - Session")
        self.workingmode_pitchsession.grid(row = 1, column = 0, padx=10, pady = 5)

        self.workingmode_conversation = customtkinter.CTkRadioButton(self, text="Gespräch", variable=self.v, value= "Gespräch")
        self.workingmode_conversation.grid(row = 1, column = 2, padx=10, pady = 5)

        self.v.trace("w", lambda *args: parent.on_ok())

        def on_radio_select():
            #Audio-Gerät speichern
            Startupsettings.selected_audio_device = self.parent.masteraudio_device_list_selector.v.get()
            print("Selected Device: ", Startupsettings.selected_audio_device)

            #Session-Name speichern und an TestDataExtractor2 weitergeben
            Startupsettings.session_name = self.session_name_selector.entry_var.get()
            Main.Set_Session_Name(Startupsettings.session_name)
            print(Startupsettings.session_name)

            Startupsettings.working_mode = self.working_mode_selector.v.get()
            Weights.set_working_mode(self.working_mode_selector.v.get())
            print(Startupsettings.working_mode)
            print(Weights.working_mode)


        ## Manuelle Gewichte-Anpassung, falls gewünscht

        self.spinbox_anger = CustomSpinBox(self, title="Anger")
        self.spinbox_anger.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.spinbox_boredom = CustomSpinBox(self, title="Boredom")
        self.spinbox_boredom.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.spinbox_disgust = CustomSpinBox(self, title="Disgust")
        self.spinbox_disgust.grid(row = 2, column = 2, padx = 5, pady = 5)

        
        
        self.spinbox_fear = CustomSpinBox(self, title="Fear")
        self.spinbox_fear.grid(row = 3, column = 0, padx = 5, pady = 5)

        self.spinbox_happiness = CustomSpinBox(self, title="Happiness")
        self.spinbox_happiness.grid(row = 3, column = 1, padx = 5, pady = 5)

        self.spinbox_neutral = CustomSpinBox(self, title="Neutral")
        self.spinbox_neutral.grid(row = 3, column = 2, padx = 5, pady = 5)


        self.spinbox_sadness = CustomSpinBox(self, title="Sadness")
        self.spinbox_sadness.grid(row = 4, column = 0, padx = 5, pady = 5)

