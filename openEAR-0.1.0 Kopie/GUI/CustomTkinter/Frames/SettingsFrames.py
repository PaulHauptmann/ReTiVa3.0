import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import customtkinter
from CustomObjects import *
from .PieChartFrames import *
from .Observer import *



class emodbSettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = customtkinter.CTkLabel(self, text= "EmoDB - Auswertung")
        self.title.grid(row = 0, column = 1)



        ## Tortendiagramm erzeugen
        self.pie = PieChartFrame(self)

        #Farbe der Bereiche nach Reihenfolge unten anpassen
        self.pie.colors = ["white", "green", "white", "yellow", "red", "green", "blue", "yellow"]

        self.pie.grid(row = 1, column = 3, padx = 30)


        observer = Observer()

        Weights.w_emodb_anger.attach(observer)
        Weights.w_emodb_boredom.attach(observer)
        Weights.w_emodb_disgust.attach(observer)
        Weights.w_emodb_fear.attach(observer)
        Weights.w_emodb_happiness.attach(observer)
        Weights.w_emodb_neutral.attach(observer)
        Weights.w_emodb_sadness.attach(observer)
        




        self.spinbox_emo_anger = CustomSpinBox(self, title="Anger")
        self.spinbox_emo_anger.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.spinbox_emo_boredom = CustomSpinBox(self, title="Boredom")
        self.spinbox_emo_boredom.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.spinbox_emo_disgust = CustomSpinBox(self, title="Disgust")
        self.spinbox_emo_disgust.grid(row = 1, column = 2, padx = 5, pady = 5)
        
        self.spinbox_emo_fear = CustomSpinBox(self, title="Fear")
        self.spinbox_emo_fear.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.spinbox_emo_happiness = CustomSpinBox(self, title="Happiness")
        self.spinbox_emo_happiness.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.spinbox_emo_neutral = CustomSpinBox(self, title="Neutral")
        self.spinbox_emo_neutral.grid(row = 2, column = 2, padx = 5, pady = 5)

        self.spinbox_emo_sadness = CustomSpinBox(self, title="Sadness")
        self.spinbox_emo_sadness.grid(row = 3, column = 0, padx = 5, pady = 5)

    def adjust_weights(self):

        # Wert in Spinboxen anpassen auf Wert aus Weights - Class
        print(Weights.w_emodb_anger)
        self.spinbox_emo_anger.set(Weights.w_emodb_anger)
        self.spinbox_emo_boredom.set(Weights.w_emodb_boredom)
        self.spinbox_emo_disgust.set(Weights.w_emodb_disgust)
        self.spinbox_emo_fear.set(Weights.w_emodb_fear)
        self.spinbox_emo_happiness.set(Weights.w_emodb_happiness)
        self.spinbox_emo_neutral.set(Weights.w_emodb_neutral)
        self.spinbox_emo_sadness.set(Weights.w_emodb_sadness)

    def update_chart(self):
        # Daten an Tortendiagramm übergeben und aktualisieren
        self.pie.data = [Weights.w_emodb_anger,
                        Weights.w_emodb_boredom,
                        Weights.w_emodb_disgust,
                        Weights.w_emodb_fear,
                        Weights.w_emodb_happiness,
                        Weights.w_emodb_neutral,
                        Weights.w_emodb_sadness]

        self.pie.update_chart()

class abcAffectSettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = customtkinter.CTkLabel(self, text= "abcAffect - Auswertung")
        self.title.grid(row = 0, column = 1)


        ## Tortendiagramm erzeugen
        self.pie = PieChartFrame(self)

        #Farbe der Bereiche nach Reihenfolge unten anpassen
        self.pie.colors = ["white", "green", "white", "yellow", "red", "green", "blue", "yellow"]

        self.pie.grid(row = 1, column = 3, padx = 30)



        self.spinbox_abc_agressiv = CustomSpinBox(self, title="Agressiv")
        self.spinbox_abc_agressiv.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.spinbox_abc_cheerful = CustomSpinBox(self, title="Cheerful")
        self.spinbox_abc_cheerful.grid(row = 1, column = 1)

        self.spinbox_abc_intoxicated = CustomSpinBox(self, title="Intoxicated")
        self.spinbox_abc_intoxicated.grid(row = 1, column = 2)

        self.spinbox_abc_nervous = CustomSpinBox(self, title="Nervous")
        self.spinbox_abc_nervous.grid(row = 2, column = 0)

        self.spinbox_abc_neutral = CustomSpinBox(self, title="Neutral_abc_Affect")
        self.spinbox_abc_neutral.grid(row = 2, column = 1)

        self.spinbox_abc_tired = CustomSpinBox(self, title="Tired")
        self.spinbox_abc_tired.grid(row = 2, column = 2)
    
    def adjust_weights(self):

            self.spinbox_abc_agressiv.set(Weights.w_abc_agressiv)
            self.spinbox_abc_cheerful.set(Weights.w_abc_cheerful)
            self.spinbox_abc_intoxicated.set(Weights.w_abc_intoxicated)
            self.spinbox_abc_nervous.set(Weights.w_abc_nervous)
            self.spinbox_abc_neutral.set(Weights.w_abc_neutral)
            self.spinbox_abc_tired.set(Weights.w_abc_tired)

            # Daten an Tortendiagramm übergeben und aktualisieren
            self.pie.data = [Weights.w_abc_agressiv,
                            Weights.w_abc_cheerful,
                            Weights.w_abc_intoxicated,
                            Weights.w_abc_nervous,
                            Weights.w_abc_neutral,
                            Weights.w_abc_tired,
                            ]

            self.pie.update_chart()



