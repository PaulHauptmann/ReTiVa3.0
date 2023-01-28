import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import customtkinter
from CustomObjects import *
from .PieChartFrames import *
from .Observer import *



class emodbSettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, create_pie:bool, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = customtkinter.CTkLabel(self, text= "EmoDB - Auswertung")
        self.title.grid(row = 0, column = 1)


        if create_pie : 
            ## Tortendiagramm erzeugen
            self.pie = PieChartFrame(self)

            #Farbe der Bereiche nach Reihenfolge unten anpassen
            self.pie.colors = ["white", "green", "white", "yellow", "red", "green", "blue", "yellow"]

            self.pie.grid(row = 1, column = 3, padx = 30)


        '''observer = Observer()
        Weights.w_emodb_anger.attach(observer)
        Weights.w_emodb_boredom.attach(observer)
        Weights.w_emodb_disgust.attach(observer)
        Weights.w_emodb_fear.attach(observer)
        Weights.w_emodb_happiness.attach(observer)
        Weights.w_emodb_neutral.attach(observer)
        Weights.w_emodb_sadness.attach(observer)
        '''




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
        '''self.pie.data = [Weights.w_emodb_anger,
                         Weights.w_emodb_boredom,
                         Weights.w_emodb_disgust,
                         Weights.w_emodb_fear,
                         Weights.w_emodb_happiness,
                         Weights.w_emodb_neutral,
                         Weights.w_emodb_sadness]

        self.pie.update_chart()
'''
class abcAffectSettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, create_pie:bool, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = customtkinter.CTkLabel(self, text= "abcAffect - Auswertung")
        self.title.grid(row = 0, column = 1)

        if create_pie:
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

        
    def update_chart(self):
        # Daten an Tortendiagramm übergeben und aktualisieren
        '''self.pie.data = [Weights.w_abc_agressiv,
                        Weights.w_abc_cheerful,
                        Weights.w_abc_intoxicated,
                        Weights.w_abc_nervous,
                        Weights.w_abc_neutral,
                        Weights.w_abc_tired,
                        ]

        self.pie.update_chart()'''
    

class ScalesSettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = customtkinter.CTkLabel(self, text="Select the Scales that should be displayed: (Max: 2)")
        self.title.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.var1 = customtkinter.IntVar()
        self.var2 = customtkinter.IntVar()
        self.var3 = customtkinter.IntVar()
        

        self.switch_loi = customtkinter.CTkSwitch(self, text= "Level of Interest", variable=self.var1, command=self.check_state)
        self.switch_loi.grid(row = 1, column = 0, pady = 10, padx = 10, sticky = "w")

        self.switch_arousal = customtkinter.CTkSwitch(self, text= "Arousal", variable=self.var2, command=self.check_state)
        self.switch_arousal.grid(row = 2, column = 0, pady = 10,padx = 10, sticky = "w")

        self.switch_valence = customtkinter.CTkSwitch(self, text= "Valence", variable=self.var3, command=self.check_state)
        self.switch_valence.grid(row = 3, column = 0, pady = 10,padx = 10, sticky = "w")

        self.switch_loi.select()
        self.switch_valence.select()

        self.var1.trace("w", lambda *args: self.loi_select())
        self.var2.trace("w", lambda *args: self.arousal_select())
        self.var3.trace("w", lambda *args: self.valence_select())

    def check_state(self):
        if self.var1.get() + self.var2.get() + self.var3.get() > 2:
            self.var1.set(0)


    def loi_select(self):
        Startupsettings.loi_scale = self.var1.get()
        print(Startupsettings.loi_scale)

    def arousal_select(self):
        Startupsettings.arousal_scale = self.var2.get()
        print(Startupsettings.arousal_scale)

    def valence_select(self):
        Startupsettings.valence_scale = self.var3.get()
        print(Startupsettings.valence_scale)


class EmotionSettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = customtkinter.CTkLabel(self, text="Change Output of the strongest Emotion(s)")
        self.title.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nw")

        self.v = customtkinter.BooleanVar()

        self.emotion_with_emoji = customtkinter.CTkRadioButton(self, text="Emotion with Emoji", variable=self.v, value=False)
        self.emotion_with_emoji.grid(row = 1, column = 0, padx=10, pady = 10, sticky = "w")

        self.dual_emotions = customtkinter.CTkRadioButton(self, text="Emotion and Affect", variable=self.v, value=True)
        self.dual_emotions.grid(row = 2, column = 0, padx=10, pady = 10, sticky = "w")

        self.v.trace("w", lambda *args: on_radio_select())

    
        def on_radio_select():
            Startupsettings.show_dual_emotions = self.v.get()
            print(Startupsettings.show_dual_emotions)


class BigAnalysisChooseModel(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = customtkinter.CTkLabel(self, text="Choose the displayed Analysis Model in the Detailed View")
        self.title.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nw")

        self.v = customtkinter.StringVar()

        self.emodb = customtkinter.CTkRadioButton(self, text="EmoDB", variable=self.v, value="EmoDB")
        self.emodb.grid(row = 1, column = 0, padx=10, pady = 10, sticky = "w")

        self.abc = customtkinter.CTkRadioButton(self, text="AbcAffect", variable=self.v, value="AbcAffect")
        self.abc.grid(row = 2, column = 0, padx=10, pady = 10, sticky = "w")

        self.v.trace("w", lambda *args: on_radio_select())

        def on_radio_select():
                Startupsettings.show_abc_graphs = self.v.get()
                print(Startupsettings.show_abc_graphs)