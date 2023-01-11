import tkinter
import customtkinter
import listaudiodevices



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
        

        self.header = customtkinter.CTkLabel(self, text="Session-Name vergeben: ")
        self.header.pack(padx=10, pady = 5, anchor = "n")


        self.entry_var= tkinter.StringVar()
        self.session_input = customtkinter.CTkEntry(self, textvariable=self.entry_var, width=400, height=30, placeholder_text="Name hier eingeben... ")
        self.session_input.pack(padx = 10, pady = 10, anchor = "s")


## Frame, in dem der gewünschte Modus der Analyse festgelegt werden kann

class WorkingModeFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,  **kwargs)

        self.header = customtkinter.CTkLabel(self, text="Konfiguration der Analyse")
        self.header.grid(row = 0, column = 1, padx=10, pady = 5)


        ## Working-Mode auswählen 

        self.v = customtkinter.StringVar()
        
        self.workingmode_pitchsession = customtkinter.CTkRadioButton(self, text="Pitch - Session", variable=self.v, value= "Pitch - Session")
        self.workingmode_pitchsession.grid(row = 1, column = 0, padx=10, pady = 5)

        self.workingmode_conversation = customtkinter.CTkRadioButton(self, text="Gespräch", variable=self.v, value= "Gespräch")
        self.workingmode_conversation.grid(row = 1, column = 2, padx=10, pady = 5)