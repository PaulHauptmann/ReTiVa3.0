from typing import Union, Callable
import customtkinter
from openpyxl import *


## Objekt, das die Start-Einstellungen speichert, die im New_Analysis_Window festgelegt werden ##

class Startupsettings(object):
    selected_audio_device = ""
    session_name = ""
    working_mode= ""


## Globale Gewichte, müssen nicht instanziert werden. Alle Klassen sollten sich hier die Gewichte rausziehen können
## TODO: Schnittstelle zu TestDataExtractor2

class Weights(object):
    
    #EmoDB Gewichte
    w_emodb_anger = 0
    w_emodb_boredom = 0
    w_emodb_disgust = 0
    w_emodb_fear = 0
    w_emodb_happiness = 0
    w_emodb_neutral = 0
    w_emodb_sadness = 0

    #abcAffect Gewichte
    w_abc_agressiv = 0
    w_abc_cheerful = 0
    w_abc_intoxicated = 0
    w_abc_nervous = 0
    w_abc_neutral = 0
    w_abc_tired = 0

    #avic Interest Gewichte
    w_avic_loi1 = 0
    w_avic_loi2 = 0
    w_avic_loi3 = 0

    #Arousal Gewicht
    w_arousal = 0

    #Valence Gewicht
    w_valence = 0

    #Working Mode
    working_mode = ""

    def Read_Weights_from_Excel():
        wb = load_workbook('openEAR-0.1.0 Kopie/GUI/Default Weights/default_weights.xlsx')

        # Select the sheet
        ws = wb['Gewichte']

        #Select the right Column based on the selected working mode

        # Create an empty list to store the numbers
        numbers = []

        #Create a list storing the variable names of Class "Weights" in Order
        weights_variables = []
        weights_variables = [i for i in dir(Weights) if not callable(getattr(Weights, i)) and not i.startswith("__")]

        

        # Iterate through the rows of the column
        for row in ws.iter_rows(3, 20, values_only=True):
            # Append the number in the first column to the list
            numbers.append(row[1])

        # Assign the first number to a variable
        for i in range(len(numbers)):
            weights_variables[i] = numbers[i]
       
        print(weights_variables)

    def set_working_mode(working_mode = str):
        Weights.working_mode = working_mode
        return working_mode

#Weights.Read_Weights_from_Excel()





class CustomSpinBox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 title = "",
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        #self.weights = Weights()

        self.step_size = 1
        self.command = command

        self.title = customtkinter.CTkLabel(self, text = title, fg_color="transparent")
        self.title.grid(row = 0, column = 1)

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=0)  # entry expands

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=1, column=1, columnspan=1, padx=3, pady=3, sticky = "ew")

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=lambda:self.subtract_button_callback(title=title))
        self.subtract_button.grid(row=1, column=0, padx=(10, 0), pady=3)


        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=lambda:self.add_button_callback(title=title))
        self.add_button.grid(row=1, column=2, padx=(0, 10), pady=3)

        # default value
        self.entry.insert(0, "0")


    def add_button_callback(self, title):
        self.title = title
        
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
            self.change_weight_command(title=self.title, new_value = value)
            print("Anger: " + str(Weights.w_emodb_anger))
        except ValueError:
            return print ("error")

    def subtract_button_callback(self, title):
        self.title = title
        if self.entry.get() != 0:
            if self.command is not None:
                self.command()
            try:
                current_value = int(self.entry.get())
                if current_value > 0:
                    value = current_value - self.step_size
                    self.entry.delete(0, "end")
                    self.entry.insert(0, value)
                    self.change_weight_command(title=self.title, new_value=value)
                    print("Boredom" + str(Weights.w_emodb_boredom))
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
    
    def change_weight_command(self, title, new_value):
        self.new_value = new_value
        self.title = title
        if self.title == "Anger": Weights.w_emodb_anger= self.new_value
        if self.title == "Boredom": Weights.w_emodb_boredom= self.new_value

    