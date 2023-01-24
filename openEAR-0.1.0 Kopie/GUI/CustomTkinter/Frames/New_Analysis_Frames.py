import tkinter as tk
import customtkinter
import listaudiodevices
from CustomObjects import *
from TestDataExtractor2 import *
from .SettingsFrames import *



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


class WeightsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        

        self.header = customtkinter.CTkLabel(self, text="Konfiguration der Analyse")
        self.header.grid(row = 0, column = 0, padx=10, pady = 5)

        self.emo_frame = emodbSettingsFrame(self, create_pie=False)
        self.emo_frame.grid(row = 2, column = 0, padx = 20, pady = 20)
        self.emo_frame.grid_remove()

        self.abc_frame = abcAffectSettingsFrame(self, create_pie=False)
        self.abc_frame.grid(row = 3, column = 0, padx = 20, pady = 20)
        self.abc_frame.grid_remove()

        


        ## Voreinstellung für Gewichte auswählen 

        self.radio_frame = customtkinter.CTkFrame(self)
        self.radio_frame.grid(row = 1, column = 0, padx = 20, pady = 30)

        self.v = customtkinter.StringVar()
        
        self.workingmode_pitchsession = customtkinter.CTkRadioButton(self.radio_frame, text="Pitch – Session", variable=self.v, value= "Pitch – Session")
        self.workingmode_pitchsession.grid(row = 0, column = 0, padx=10, pady = 5)

        self.workingmode_conversation = customtkinter.CTkRadioButton(self.radio_frame, text="Gespräch", variable=self.v, value= "Gespräch")
        self.workingmode_conversation.grid(row = 0, column = 1, padx=10, pady = 5)

        self.workingmode_custom = customtkinter.CTkRadioButton(self.radio_frame, text= "Benutzerdefiniert", variable=self.v, value="Benutzerdefiniert")
        self.workingmode_custom.grid(row = 0, column = 2, padx=10, pady = 5)


        self.v.trace("w", lambda *args: on_radio_select())



        
        ## Ändert die Werte der Variablen und der SpinBox felder bei Auswahl einer Voreinstellung
        
        ##TODO: Smootherer Übergang von Ein zu Ausblenden der zusätzlichen Einstellungen

        def on_radio_select():
            if self.v.get() == "Benutzerdefiniert":
                self.emo_frame.grid()
                self.abc_frame.grid()
            else :
                self.emo_frame.grid_remove()
                self.abc_frame.grid_remove()
                
            print(Weights.working_mode)
            Weights.Read_Weights_from_Excel(Weights, self.v.get())
            #self.spinbox_anger.set(Weights.w_emodb_anger)
            adjust_all_weights()
            #AdvancedSettingsFrame.adjust_weights()


        ## Wird aufgerufen bei ändern der Voreinstellung und ändert die Einträge der Spinboxen

        def adjust_all_weights():

            self.emo_frame.adjust_weights()
            self.emo_frame.update_chart()

            self.abc_frame.adjust_weights()
            self.abc_frame.update_chart()
            

            
class Observer:
    def update(self, subject):
        print(f'{type(subject).__name__} has been changed')
        


