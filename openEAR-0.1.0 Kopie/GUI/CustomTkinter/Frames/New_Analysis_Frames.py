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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        

        self.header = customtkinter.CTkLabel(self, text="Konfiguration der Analyse")
        self.header.grid(row = 0, column = 1, padx=10, pady = 5)


        ## Voreinstellung für Gewichte auswählen 

        self.v = customtkinter.StringVar()
        
        self.workingmode_pitchsession = customtkinter.CTkRadioButton(self, text="Pitch – Session", variable=self.v, value= "Pitch – Session")
        self.workingmode_pitchsession.grid(row = 1, column = 0, padx=10, pady = 5)

        self.workingmode_conversation = customtkinter.CTkRadioButton(self, text="Gespräch", variable=self.v, value= "Gespräch")
        self.workingmode_conversation.grid(row = 1, column = 1, padx=10, pady = 5)

        self.workingmode_custom = customtkinter.CTkRadioButton(self, text= "Benutzerdefiniert", variable=self.v, value="Benutzerdefiniert")
        self.workingmode_custom.grid(row = 1, column = 2, padx=10, pady = 5)


        self.v.trace("w", lambda *args: on_radio_select())

        def on_radio_select():
            Weights.Read_Weights_from_Excel(Weights, self.v.get())
            #self.spinbox_anger.set(Weights.w_emodb_anger)
            adjust_weights()
            print(Weights.working_mode)
        ## Manuelle Gewichte-Anpassung, falls gewünscht

        def adjust_weights():

            #emodb
            self.spinbox_anger.set(Weights.w_emodb_anger)
            self.spinbox_boredom.set(Weights.w_emodb_boredom)
            self.spinbox_disgust.set(Weights.w_emodb_disgust)
            self.spinbox_fear.set(Weights.w_emodb_fear)
            self.spinbox_happiness.set(Weights.w_emodb_happiness)
            self.spinbox_neutral.set(Weights.w_emodb_neutral)
            self.spinbox_sadness.set(Weights.w_emodb_sadness)

            #loi
            self.spinbox_loi1.set(Weights.w_avic_loi1)
            self.spinbox_loi2.set(Weights.w_avic_loi2)
            self.spinbox_loi3.set(Weights.w_avic_loi3)

            


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

        self.spinbox_loi1 = CustomSpinBox(self, title = "Level of Interest 1")
        self.spinbox_loi1.grid(row = 4, column = 1, padx = 5, pady = 5)

        self.spinbox_loi2 = CustomSpinBox(self, title = "Level of Interest 2")
        self.spinbox_loi2.grid(row = 4, column = 2, padx = 5, pady = 5)



        self.spinbox_loi3 = CustomSpinBox(self, title = "Level of Interest 3")
        self.spinbox_loi3.grid(row = 5, column = 0, padx = 5, pady = 5)