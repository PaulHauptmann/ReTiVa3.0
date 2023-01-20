from typing import Union, Callable
import customtkinter


## Objekt, das die Start-Einstellungen speichert, die im New_Analysis_Window festgelegt werden ##

class Startupsettings(object):
    selected_audio_device = ""
    session_name = ""
    working_mode= ""



class Weights(object):
    
    #EmoDB Gewichte
    w_emodb_anger = 5
    w_emodb_boredom = int
    w_emodb_disgust = int
    w_emodb_fear = int
    w_emodb_happiness = int
    w_emodb_neutral = int
    w_emodb_sadness = int

    #abcAffect Gewichte
    w_abc_agressiv = int
    w_abc_cheerful = int
    w_abc_intoxicated = int
    w_abc_nervous = int
    w_abc_neutral = int
    w_abc_tired = int

    #avic Interest Gewichte
    w_avic_loi1 = int
    w_avic_loi2 = int
    w_avic_loi3 = int

    #Arousal Gewicht
    w_arousal = int

    #Valence Gewicht
    w_valence = int






class CustomSpinBox_old(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 command: Callable = None,
                 title = "",
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.weights = Weights()

        self.step_size = 1
        self.command = command

        self.title = customtkinter.CTkLabel(self, text = title, fg_color="transparent")
        self.title.grid(row = 0, column = 1)

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands
        
        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=1, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback(title=title))
        self.subtract_button.grid(row=1, column=0, padx=(10, 0), pady=3)


        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback(title=title))
        self.add_button.grid(row=1, column=2, padx=(0, 10), pady=3)

        # default value
        self.entry.insert(0, "0")


    def add_button_callback(self, title):
        self.title = title
        if self.command is not None:
            self.command() 
        print(self.entry.get())
        value = int(self.entry.get()) + self.step_size
        self.entry.delete(0, "end")
        self.entry.insert(0, value)
        self.add_command(title=self.title, new_value = value)
        #except ValueError:
        #    return print ("error")

    def subtract_button_callback(self, title):
        self.title = title
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
            self.substract_command(title=self.title, new_value=value)
            print(self.weights.w_emodb_anger)
        except ValueError:
            return print("error")

    def get(self) -> Union[float, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))
    
    def add_command(self, title, new_value):
        self.new_value = new_value
        self.title = title
        if self.title == "Anger": self.weights.w_emodb_anger = self.new_value
        

    def substract_command(self, title, new_value):
        self.new_value = new_value
        self.title = title
        if self.title == "Anger": self.weights.w_emodb_anger = self.new_value
        