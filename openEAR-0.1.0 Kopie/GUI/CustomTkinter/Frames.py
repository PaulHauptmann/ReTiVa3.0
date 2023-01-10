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
            device_radio.grid(row = index, column = 0, padx=5, pady = 5)
            self.device_radios.append(device_radio)
        
        self.device_radios[0].select()



        

        
        
