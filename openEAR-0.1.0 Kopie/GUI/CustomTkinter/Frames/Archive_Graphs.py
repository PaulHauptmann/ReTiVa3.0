import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.figure import Figure
from TestDataExtractor2 import *
import customtkinter
import numpy as np
import ctypes


## Farben global für alle Graphen ändern ##
c_background = '#212121'
c_white = '#F2F2F2'

c_1 = '#3A65A4'
c_2 = '#82A3D4'
c_3 = '#C2D1E8'
c_4 = '#FFDBBD'
c_5 = '#FFAD69'
c_6 = '#DE6400'
c_7 = '#964400'


c_colors = []
c_colors.append(c_1)
c_colors.append(c_2)
c_colors.append(c_3)
c_colors.append(c_4)
c_colors.append(c_5)
c_colors.append(c_6)
c_colors.append(c_7)


c_dark_gray = '#717171'
c_light_gray = '#909090'

print(c_colors)



class Variablen():

    Archive_Data_Time               = [0.0]
    Archive_Data_Aroual               = [0.0]
    Archive_Data_Valence               = [0.0]
    Archive_Data_EmodbEmotionAnger               = [0.0]
    Archive_Data_EmodbEmotionBoredm               = [0.0]
    Archive_Data_EmodbEmotionDisgust               = [0.0]
    Archive_Data_EmodbEmotionFear               = [0.0]
    Archive_Data_EmodbEmotionHappness               = [0.0]
    Archive_Data_EmodbEmotionNeutral               = [0.0]
    Archive_Data_EmodbEmotionSadness               = [0.0]
    Archive_Data_AbcAffectAgressiv               = [0.0]
    Archive_Data_AbcAffectCheerful               = [0.0]
    Archive_Data_AbcAffectIntoxicatd               = [0.0]
    Archive_Data_AbcAffectNervous               = [0.0]
    Archive_Data_AbcAffectNeutral               = [0.0]
    Archive_Data_AbcAffectTired               = [0.0]
    Archive_Data_Loi1               = [0.0]
    Archive_Data_Loi2               = [0.0]
    Archive_Data_Loi3               = [0.0]
    Archive_Soll_DataEmodbEmotionAnger               = [0.0]
    Archive_Soll_DataEmodbEmotionBoredom               = [0.0]
    Archive_Soll_DataEmodbEmotionDisgust               = [0.0]
    Archive_Soll_DataEmodbEmotionFear               = [0.0]
    Archive_Soll_DataEmodbEmotionHappiness               = [0.0]
    Archive_Soll_DataEmodbEmotionNeutral               = [0.0]
    Archive_Soll_DataEmodbEmotionSadness               = [0.0]
    Archive_Soll_DataAbcAffectAgressiv               = [0.0]
    Archive_Soll_DataAbcAffectCheerfull               = [0.0]
    Archive_Soll_DataAbcAffectIntoxicated               = [0.0]
    Archive_Soll_DataAbcAffectNervous               = [0.0]
    Archive_Soll_DataAbcAffectNeutral               = [0.0]
    Archive_Soll_DataAbcAffectTired               = [0.0]
    Archive_Abs_MW_Data_Arousal               = [0.0]
    Archive_Abs_MW_Data_Valence               = [0.0]
    Archive_Abs_MW_Data_EmodbEmotionAnger               = [0.0]
    Archive_Abs_MW_Data_EmodbEmotionBoredom               = [0.0]
    Archive_Abs_MW_Data_EmodbEmotionDisgust               = [0.0]
    Archive_Abs_MW_Data_EmodbEmotionFear               = [0.0]
    Archive_Abs_MW_Data_EmodbEmotionHappiness               = [0.0]
    Archive_Abs_MW_Data_EmodbEmotionNeutral               = [0.0]
    Archive_Abs_MW_Data_EmodbEmotionSadness               = [0.0]
    Archive_Abs_MW_Data_AbcAffectAgressiv               = [0.0]
    Archive_Abs_MW_Data_AbcAffectCheerfull               = [0.0]
    Archive_Abs_MW_Data_AbcAffectIntoxicated               = [0.0]
    Archive_Abs_MW_Data_AbcAffectNervous               = [0.0]
    Archive_Abs_MW_Data_AbcAffectNeutral               = [0.0]
    Archive_Abs_MW_Data_AbcAffectTired               = [0.0]
    Archive_Abs_MW_Data_Loi1               = [0.0]
    Archive_Abs_MW_Data_Loi2               = [0.0]
    Archive_Abs_MW_Data_Loi3               = [0.0]
    Archive_Score_EmodbEmotions               = [0.0]
    Archive_Score_AbcAffect               = [0.0]
    Archive_Score_Retiva               = [0.0]
    Archive_Abs_MW_Loi_Score               = [0.0]
    Archive_MW_SpeakRatio                   = [0.0]
    


#########################################################################
#### Graph mit zeitlichem Verlauf der einzelnen Emotionen von EmoDb #####
#########################################################################


class GraphEmoOverTime_Archive(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        test_list1 = [0.2, 0.3, 0.1, 0.5, 0.3]
        test_list2 = [0.5, 0.6, 0.7, 0.4, 0.2]

        #Daten auf 100er Skala normieren
        #DataEmodbEmotionAnger_normed = [i * 100 for i in test_list1 ]
        #DataEmodbEmotionBoredom_normed = [i * 100 for i in test_list2 ]
        
        

        DataEmodbEmotionAnger_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionAnger ]
        DataEmodbEmotionBoredom_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionBoredm ]
        DataEmodbEmotionDisgust_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionDisgust ]
        DataEmodbEmotionFear_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionFear ]
        DataEmodbEmotionHappiness_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionHappness ]
        DataEmodbEmotionNeutral_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionNeutral ]
        DataEmodbEmotionSadness_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionSadness ]

        #self.lists = [Main.DataEmodbEmotionAnger, Main.DataEmodbEmotionBoredom, Main.DataEmodbEmotionDisgust, Main.DataEmodbEmotionFear, Main.DataEmodbEmotionHappiness, Main.DataEmodbEmotionNeutral, Main.DataEmodbEmotionSadness]

        #Neue Listen-Liste mit normierten Daten
        self.lists_normed = [DataEmodbEmotionAnger_normed,
                            DataEmodbEmotionBoredom_normed,
                            DataEmodbEmotionDisgust_normed,
                            DataEmodbEmotionFear_normed,
                            DataEmodbEmotionHappiness_normed,
                            DataEmodbEmotionNeutral_normed,
                            DataEmodbEmotionSadness_normed]
            

        self.figure, self.ax = plt.subplots(facecolor=c_background, figsize=(6, 2))
        self.figure.set_layout_engine("constrained")

        self.ax.set_title('Mix of Emotions over Time', color = c_white)

        self.ax.spines['bottom'].set_color(c_white)
        self.ax.spines['left'].set_color(c_white)
        self.ax.spines['top'].set_color(c_background)
        self.ax.spines['right'].set_color(c_background)
        

    def create_graph(self):
        #for i in range(7):
        self.ax.tick_params(color = c_white, which = "both", labelcolor = c_white)
        self.ax.set_facecolor(color = c_background)
        
        

        self.ax.plot(self.lists_normed[0], label=f'Anger', color = c_1)
        self.ax.plot(self.lists_normed[1], label=f'Boredom', color = c_2)
        self.ax.plot(self.lists_normed[2], label=f'Disgust', color = c_3)
        self.ax.plot(self.lists_normed[3], label=f'Fear', color = c_4)
        self.ax.plot(self.lists_normed[4], label=f'Happiness', color = c_5)
        self.ax.plot(self.lists_normed[5], label=f'Neutral', color = c_6)
        self.ax.plot(self.lists_normed[6], label=f'Sadness', color = c_7)
        self.ax.set_ylabel('Prozent', color = c_white)
        self.ax.set_ylim(0,100)
        self.ax.set_xlabel('Time (s)', color = c_white)
        #self.ax.set_xticklabels(["start"])
        self.ax.legend()
        self.ax.xaxis.set_visible(True)
        self.ax.legend().set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_chart(self):
        
        test_list2 = [0.2, 0.3, 0.1, 0.5, 0.3]
        test_list1 = [0.5, 0.6, 0.7, 0.4, 0.2]

        #Daten auf 100er Skala normieren
        #DataEmodbEmotionAnger_normed = [i * 100 for i in test_list1 ]
        #DataEmodbEmotionBoredom_normed = [i * 100 for i in test_list2 ]
        
        
        DataEmodbEmotionAnger_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionAnger ]
        DataEmodbEmotionBoredom_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionBoredm ]
        DataEmodbEmotionDisgust_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionDisgust ]
        DataEmodbEmotionFear_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionFear ]
        DataEmodbEmotionHappiness_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionHappness ]
        DataEmodbEmotionNeutral_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionNeutral ]
        DataEmodbEmotionSadness_normed = [i * 100 for i in Variablen.Archive_Data_EmodbEmotionSadness ]
        
        #self.lists = [Main.DataEmodbEmotionAnger, Main.DataEmodbEmotionBoredom, Main.DataEmodbEmotionDisgust, Main.DataEmodbEmotionFear, Main.DataEmodbEmotionHappiness, Main.DataEmodbEmotionNeutral, Main.DataEmodbEmotionSadness]

        #Neue Listen-Liste mit normierten Daten
        self.lists_normed = [DataEmodbEmotionAnger_normed,
                            DataEmodbEmotionBoredom_normed,
                            DataEmodbEmotionDisgust_normed,
                            DataEmodbEmotionFear_normed,
                            DataEmodbEmotionHappiness_normed,
                            DataEmodbEmotionNeutral_normed,
                            DataEmodbEmotionSadness_normed]
        
        lines = self.ax.get_lines()
        for i in range(len(lines)):
            lines[i].set_data(range(len(self.lists_normed[i])), self.lists_normed[i])
        self.ax.relim()
        self.ax.autoscale_view()
        self.figure.canvas.draw()
    

#############################################################################
#### Graph mit zeitlichem Verlauf der einzelnen Emotionen von AbcAffect #####
#############################################################################


class GraphAbcOverTime_Archive(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        test_list1 = [0.2, 0.3, 0.1, 0.5, 0.3]
        test_list2 = [0.5, 0.6, 0.7, 0.4, 0.2]


        '''Variablen.archive_Data_AbcAffectIntoxicatd
        Variablen.archive_Data_AbcAffectNervous
        Variablen.archive_Data_AbcAffectNeutral
        Variablen.archive_Data_AbcAffectTired'''

        
        
        #Daten auf 100er Skala normieren
        DataAbcAffectAgressiv_normed = [i * 100 for i in test_list1]
        DataAbcAffectCheerfull_normed = [i * 100 for i in test_list2]


        #DataAbcAffectAgressiv_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectAgressiv]
        #DataAbcAffectCheerfull_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectCheerful]
        DataAbcAffectIntoxicated_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectIntoxicatd]
        DataAbcAffectNervous_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectNervous]
        DataAbcAffectNeutral_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectNeutral]
        DataAbcAffectTired_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectTired]


        #Neue Listen-Liste mit normierten Daten
        self.lists_normed = [
                                DataAbcAffectAgressiv_normed,
                                DataAbcAffectCheerfull_normed,
                                DataAbcAffectIntoxicated_normed,
                                DataAbcAffectNervous_normed,
                                DataAbcAffectNeutral_normed,
                                DataAbcAffectTired_normed
                            ]





        self.figure, self.ax = plt.subplots(facecolor=c_background, figsize=(6,2))
        self.figure.set_layout_engine("constrained")
        
        self.ax.set_title('Mix of Emotions over Time', color = c_white)
        

        self.ax.spines['bottom'].set_color(c_white)
        self.ax.spines['left'].set_color(c_white)
        self.ax.spines['top'].set_color(c_background)
        self.ax.spines['right'].set_color(c_background)
        

    def create_graph(self):
        #for i in range(7):
        self.ax.tick_params(color = c_white, which = "both", labelcolor = c_white)
        self.ax.set_facecolor(color = c_background)
        

        self.ax.plot(self.lists_normed[0], label=f'Agressive', color = c_1)
        self.ax.plot(self.lists_normed[1], label=f'Cheerfull', color = c_2)
        self.ax.plot(self.lists_normed[2], label=f'Intoxicated', color = c_3)
        self.ax.plot(self.lists_normed[3], label=f'Nervous', color = c_4)
        self.ax.plot(self.lists_normed[4], label=f'Neutral', color = c_5)
        self.ax.plot(self.lists_normed[5], label=f'Tired', color = c_6)
        self.ax.set_ylabel('Prozent', color = c_white)
        self.ax.set_ylim(0,100)
        self.ax.set_xlabel('Time (s)', color = c_white)
        #self.ax.set_xticklabels(["start"])
        self.ax.legend()
        self.ax.xaxis.set_visible(True)
        self.ax.legend().set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_chart(self):
        
        test_list2 = [0.2, 0.3, 0.1, 0.5, 0.3]
        test_list1 = [0.5, 0.6, 0.7, 0.4, 0.2]

        '''Variablen.archive_Data_AbcAffectIntoxicatd
        Variablen.archive_Data_AbcAffectNervous
        Variablen.archive_Data_AbcAffectNeutral
        Variablen.archive_Data_AbcAffectTired
        '''
        
        #Daten auf 100er Skala normieren
        DataAbcAffectAgressiv_normed = [i * 100 for i in test_list1]
        DataAbcAffectCheerfull_normed = [i * 100 for i in test_list2]

        #DataAbcAffectAgressiv_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectAgressiv]
        #DataAbcAffectCheerfull_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectCheerful]
        DataAbcAffectIntoxicated_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectIntoxicatd]
        DataAbcAffectNervous_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectNervous]
        DataAbcAffectNeutral_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectNeutral]
        DataAbcAffectTired_normed = [i * 100 for i in Variablen.Archive_Data_AbcAffectTired]

        #Neue Listen-Liste mit normierten Daten
        self.lists_normed = [
                                DataAbcAffectAgressiv_normed,
                                DataAbcAffectCheerfull_normed,
                                DataAbcAffectIntoxicated_normed,
                                DataAbcAffectNervous_normed,
                                DataAbcAffectNeutral_normed,
                                DataAbcAffectTired_normed
                            ]
        
        lines = self.ax.get_lines()
        for i in range(len(lines)):
            lines[i].set_data(range(len(self.lists_normed[i])), self.lists_normed[i])
        self.ax.relim()
        self.ax.autoscale_view()
        self.figure.canvas.draw()


##################################################################
#### Balkendiagramm zum vergleich von soll und ist bei EmoDb #####
###################################################################


class BarChartEmo_Archive(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

                

        if Variablen.Archive_Abs_MW_Data_EmodbEmotionAnger != None and Variablen.Archive_Soll_DataEmodbEmotionAnger != None:
            self.list1 = [Variablen.Archive_Abs_MW_Data_EmodbEmotionAnger[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionBoredom[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionDisgust[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionFear[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionHappiness[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionNeutral[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionSadness[-1]]
            self.list2 = [Variablen.Archive_Soll_DataEmodbEmotionAnger[-1],Variablen.Archive_Soll_DataEmodbEmotionBoredom[-1],Variablen.Archive_Soll_DataEmodbEmotionDisgust[-1],Variablen.Archive_Soll_DataEmodbEmotionFear[-1],Variablen.Archive_Soll_DataEmodbEmotionHappiness[-1],Variablen.Archive_Soll_DataEmodbEmotionNeutral[-1],Variablen.Archive_Soll_DataEmodbEmotionSadness[-1]]
        else:
            self.list1 = [0.14,0.28,0.42,0.56,0.70,0.85,1]
            self.list2 = [0.14,0.28,0.42,0.56,0.70,0.85,1]

        self.list1_normed = [i * 100 for i in self.list1]
        self.list2_normed = [i * 100 for i in self.list2]
        

    

    def create_chart(self):
        x = [i for i in range(1,8)]
        
        # Create a new figure
        fig = Figure(figsize=(6,2))
        fig.set_layout_engine("constrained")
        fig.set_facecolor(c_background)
        ax = fig.add_subplot(111)
        ax.set_facecolor(c_background)
        ax.tick_params(colors = c_white, which = "both")

        ax.set_title('Mix of Emotions in total', color = c_white, pad=10)
        ax.set_ylabel('Prozent', color = c_white)

        labels = ["Anger", "Boredom" , "Disgust", "Fear", "Happiness", "Neutral", "Sadness"]
        



        ax.spines['bottom'].set_color(c_white)
        ax.spines['left'].set_color(c_white)
        ax.spines['top'].set_color(c_background)
        ax.spines['right'].set_color(c_background)
        
        # Add the bar chart to the figure
        ax.bar(x, self.list1_normed, width=0.4, color = c_colors)
        ax.bar([i+0.4 for i in x], self.list2_normed, width=0.4, color = c_dark_gray)
        
        # Set the y-axis range and hide the x-axis
        #ax.set_ylim(0, max(max(self.list1), max(self.list2)))
        ax.set_ylim(0,100)
        ax.set_xlim(0,8)
        ax.set_xticks(x, labels)
        
        # Create a canvas to display the chart
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.canvas = canvas

    def update_chart(self):

        if Variablen.Archive_Abs_MW_Data_EmodbEmotionAnger != None and Variablen.Archive_Soll_DataEmodbEmotionAnger != None:
            self.list1 = [Variablen.Archive_Abs_MW_Data_EmodbEmotionAnger[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionBoredom[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionDisgust[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionFear[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionHappiness[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionNeutral[-1],Variablen.Archive_Abs_MW_Data_EmodbEmotionSadness[-1]]
            self.list2 = [Variablen.Archive_Soll_DataEmodbEmotionAnger[-1],Variablen.Archive_Soll_DataEmodbEmotionBoredom[-1],Variablen.Archive_Soll_DataEmodbEmotionDisgust[-1],Variablen.Archive_Soll_DataEmodbEmotionFear[-1],Variablen.Archive_Soll_DataEmodbEmotionHappiness[-1],Variablen.Archive_Soll_DataEmodbEmotionNeutral[-1],Variablen.Archive_Soll_DataEmodbEmotionSadness[-1]]
        else:
            self.list1 = [0.1, 0.5, 0.2, 0.4, 0.7, 0.1, 0.3]
            self.list2 = [0.14,0.28,0.42,0.56,0.70,0.85,1]

        self.list1_normed = [i * 100 for i in self.list1]
        self.list2_normed = [i * 100 for i in self.list2]
        
        
        fig = self.canvas.figure
        ax = fig.axes[0]
        
        ax.clear()
        
        ax.set_title('Mix of Emotions in total', color = c_white, pad=10)
        ax.set_ylabel('Prozent', color = c_white)

        labels = ["Anger", "Boredom" , "Disgust", "Fear", "Happiness", "Neutral", "Sadness"]
        
        ax.spines['bottom'].set_color(c_white)
        ax.spines['left'].set_color(c_white)
        ax.spines['top'].set_color(c_background)
        ax.spines['right'].set_color(c_background)
        
        x = [i for i in range(1,8)]
        
        ax.bar(x, self.list1_normed, width=0.4, color = c_colors)
        ax.bar([i+0.4 for i in x], self.list2_normed, width=0.4, color = c_dark_gray)
        
        ax.set_ylim(0,100)
        ax.set_xlim(0,8)
        ax.set_xticks(x, labels)
        
        self.canvas.draw()



######################################################################
#### Balkendiagramm zum vergleich von soll und ist bei AbcAffect #####
######################################################################


class BarChartAbc_Archive(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                        
        


        if Variablen.Archive_Abs_MW_Data_AbcAffectAgressiv != None and Variablen.Archive_Soll_DataAbcAffectAgressiv != None:
            self.list1 = [Variablen.Archive_Abs_MW_Data_AbcAffectAgressiv[-1],Variablen.Archive_Abs_MW_Data_AbcAffectCheerfull[-1],Variablen.Archive_Abs_MW_Data_AbcAffectIntoxicated[-1],Variablen.Archive_Abs_MW_Data_AbcAffectNervous[-1],Variablen.Archive_Abs_MW_Data_AbcAffectNeutral[-1],Variablen.Archive_Abs_MW_Data_AbcAffectTired[-1]]
            self.list2 = [Variablen.Archive_Soll_DataAbcAffectAgressiv[-1],Variablen.Archive_Soll_DataAbcAffectCheerfull[-1],Variablen.Archive_Soll_DataAbcAffectIntoxicated[-1],Variablen.Archive_Soll_DataAbcAffectNervous[-1],Variablen.Archive_Soll_DataAbcAffectNeutral[-1],Variablen.Archive_Soll_DataAbcAffectTired[-1]]
        else:
            self.list1 = [0.17,0.34,0.51,0.68,0.85,1]
            self.list2 = [0.17,0.34,0.51,0.68,0.85,1]

        self.list1_normed = [i * 100 for i in self.list1]
        self.list2_normed = [i * 100 for i in self.list2]

    def create_chart(self):
        x = [i for i in range(1,7)]
        
        # Create a new figure
        fig = Figure(figsize=(6,2))
        fig.set_facecolor(c_background)
        ax = fig.add_subplot(111)
        ax.set_facecolor(c_background)
        ax.tick_params(colors = c_white, which = "both")


        ax.set_title('Mix of Emotions in total', color = c_white)
        ax.set_ylabel('Prozent', color = c_white)

        labels = ['Agressiv', 'Cheerful', 'Intoxicated', 'Nervous', 'Neutral', 'Tired']
        
        ax.spines['bottom'].set_color(c_white)
        ax.spines['left'].set_color(c_white)
        ax.spines['top'].set_color(c_background)
        ax.spines['right'].set_color(c_background)

        # Add the bar chart to the figure
        ax.bar(x, self.list1_normed, width=0.4, color = c_colors)
        ax.bar([i+0.4 for i in x], self.list2_normed, width=0.4, color = c_dark_gray)
        
        # Set the y-axis range and hide the x-axis
        ax.set_ylim(0, 100)
        ax.set_xlim(0,7)
        ax.set_xticks(x, labels)
        
        # Create a canvas to display the chart
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand=1)

        self.canvas = canvas

    def update_chart(self):

        if Variablen.Archive_Abs_MW_Data_AbcAffectAgressiv != None and Variablen.Archive_Soll_DataAbcAffectAgressiv != None:
            self.list1 = [Variablen.Archive_Abs_MW_Data_AbcAffectAgressiv[-1],Variablen.Archive_Abs_MW_Data_AbcAffectCheerfull[-1],Variablen.Archive_Abs_MW_Data_AbcAffectIntoxicated[-1],Variablen.Archive_Abs_MW_Data_AbcAffectNervous[-1],Variablen.Archive_Abs_MW_Data_AbcAffectNeutral[-1],Variablen.Archive_Abs_MW_Data_AbcAffectTired[-1]]
            self.list2 = [Variablen.Archive_Soll_DataAbcAffectAgressiv[-1],Variablen.Archive_Soll_DataAbcAffectCheerfull[-1],Variablen.Archive_Soll_DataAbcAffectIntoxicated[-1],Variablen.Archive_Soll_DataAbcAffectNervous[-1],Variablen.Archive_Soll_DataAbcAffectNeutral[-1],Variablen.Archive_Soll_DataAbcAffectTired[-1]]
        else:
            self.list1 = [0.1, 0.5, 0.2, 0.4, 0.7, 0.1, 0.3]
            self.list2 = [0.14,0.28,0.42,0.56,0.70,0.85,1]

        self.list1_normed = [i * 100 for i in self.list1]
        self.list2_normed = [i * 100 for i in self.list2]
        
        
        fig = self.canvas.figure
        ax = fig.axes[0]
        
        ax.clear()
        
        ax.set_title('Mix of Emotions in total', color = c_white, pad=10)
        ax.set_ylabel('Prozent', color = c_white)

        labels = ["Anger", "Boredom" , "Disgust", "Fear", "Happiness", "Neutral", "Sadness"]
        
        ax.spines['bottom'].set_color(c_white)
        ax.spines['left'].set_color(c_white)
        ax.spines['top'].set_color(c_background)
        ax.spines['right'].set_color(c_background)
        
        x = [i for i in range(1,8)]
        
        ax.bar(x, self.list1_normed, width=0.4, color = c_colors)
        ax.bar([i+0.4 for i in x], self.list2_normed, width=0.4, color = c_dark_gray)
        
        ax.set_ylim(0,100)
        ax.set_xlim(0,8)
        ax.set_xticks(x, labels)
        
        self.canvas.draw()
        
        
        
######################################################################
####               DonutDiagramm mit EmoDbEmotion                #####
######################################################################
        
        
class DonutEmo_Archive(customtkinter.CTkFrame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.labels = ["Anger", "Boredom" , "Disgust", "Fear", "Happiness", "Neutral", "Sadness"]
        self.list1 = [1,1,1,1,1,1,1]

    

    def create_chart(self):
        # Create a new figure
        fig = Figure(figsize=(4,4))
        fig.set_layout_engine("constrained")
        fig.set_facecolor(c_background)
        self.ax = fig.add_subplot(111)

        self.ax.set_title('Mix of Emotions over the whole Session', color = c_white, pad=20)

        # Add the donut chart to the figure
        self.wedges, self.texts = self.ax.pie(self.list1, radius=0.8, wedgeprops=dict(width=0.4, edgecolor=c_background), colors=c_colors)
        self.ax.pie([1], radius=0.4, wedgeprops=dict(width=0.4, edgecolor=c_background, facecolor=c_background))
        

        # Add labels and lines to the segments
        bbox_props = dict(boxstyle="square,pad=0.3", fc=c_background, ec=c_background, lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-", ec= c_white), bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(self.wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            self.horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            self.ax.annotate(self.labels[i], xy=(x, y), xytext=(1.2*np.sign(x), 1.3*y),
                        horizontalalignment=self.horizontalalignment, color =c_white, **kw)

        # Create a canvas to display the chart
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def update_chart(self, emodb_list:list):

        if len(emodb_list) == 7:
            self.list1 = emodb_list
        else:
            self.list1 = [1,3,2,2,1,1,2]

        total = sum(self.list1)
        self.list_normed = [i/total for i in self.list1]

        
        # Update the data of the wedges and explode list
        for i, wedge in enumerate(self.wedges):
            wedge.set_radius(self.list_normed[i])
            #wedge.set_explode(self.explode_list[i])
        
        # Remove old labels 
        for text in self.ax.texts:
            text.remove()

        # Update the data and redraw the chart
        self.wedges, self.texts = self.ax.pie(self.list_normed, radius=0.8, wedgeprops=dict(width=0.4, edgecolor=c_background), colors=c_colors)
        self.ax.pie([1], radius=0.4, wedgeprops=dict(width=0.4, edgecolor=c_background, facecolor=c_background))
        
        bbox_props = dict(boxstyle="square,pad=0.3", fc=c_background, ec=c_background, lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-", ec= c_white), bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(self.wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            self.horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            self.ax.annotate(self.labels[i], xy=(x, y), xytext=(1.2*np.sign(x), 1.3*y),
                        horizontalalignment=self.horizontalalignment, color =c_white, **kw)

        self.canvas.draw()



######################################################################
####               DonutDiagramm mit AbcAffectEmotion            #####
######################################################################




class DonutAbc_Archive(customtkinter.CTkFrame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.labels = ['Agressiv', 'Cheerful', 'Intoxicated', 'Nervous', 'Neutral', 'Tired']
        self.list1 = [1,1,1,1,1,1]

    

    def create_chart(self):
        # Create a new figure
        fig = Figure(figsize=(4,4))
        fig.set_layout_engine("constrained")
        fig.set_facecolor(c_background)
        self.ax = fig.add_subplot(111)

        self.ax.set_title('Mix of Emotions over the whole Session', color = c_white, pad=20)

        # Add the donut chart to the figure
        self.wedges, self.texts = self.ax.pie(self.list1, radius=0.8, wedgeprops=dict(width=0.4, edgecolor=c_background), colors=c_colors)
        self.ax.pie([1], radius=0.4, wedgeprops=dict(width=0.4, edgecolor=c_background, facecolor=c_background))
        

        # Add labels and lines to the segments
        bbox_props = dict(boxstyle="square,pad=0.3", fc=c_background, ec=c_background, lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-", ec= c_white), bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(self.wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            self.horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            self.ax.annotate(self.labels[i], xy=(x, y), xytext=(1.2*np.sign(x), 1.3*y),
                        horizontalalignment=self.horizontalalignment, color =c_white, **kw)

        # Create a canvas to display the chart
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def update_chart(self, abcAffect_list:list):

        if len(abcAffect_list) == 6:
            self.list1 = abcAffect_list
        else:
            self.list1 = [1,3,2,2,1,1]

        try:
            total = sum(self.list1)
            self.list_normed = [i/total for i in self.list1]
        except ZeroDivisionError:
            self.list_normed = self.list1

        
        # Update the data of the wedges and explode list
        for i, wedge in enumerate(self.wedges):
            wedge.set_radius(self.list_normed[i])
            #wedge.set_explode(self.explode_list[i])
        
        # Remove old labels 
        for text in self.ax.texts:
            text.remove()

        # Update the data and redraw the chart
        self.wedges, self.texts = self.ax.pie(self.list_normed, radius=0.8, wedgeprops=dict(width=0.4, edgecolor=c_background), colors=c_colors)
        self.ax.pie([1], radius=0.4, wedgeprops=dict(width=0.4, edgecolor=c_background, facecolor=c_background))
        
        bbox_props = dict(boxstyle="square,pad=0.3", fc=c_background, ec=c_background, lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-", ec= c_white), bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(self.wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            self.horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            self.ax.annotate(self.labels[i], xy=(x, y), xytext=(1.2*np.sign(x), 1.3*y),
                        horizontalalignment=self.horizontalalignment, color =c_white, **kw)

        self.canvas.draw()

