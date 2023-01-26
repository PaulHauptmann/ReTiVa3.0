import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from TestDataExtractor2 import *
import customtkinter
import numpy as np
import ctypes







#########################################################################
#### Graph mit zeitlichem Verlauf der einzelnen Emotionen von EmoDb #####
#########################################################################


class GraphEmoOverTime(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        test_list1 = [0.2, 0.3, 0.1, 0.5, 0.3]
        test_list2 = [0.5, 0.6, 0.7, 0.4, 0.2]

        #Daten auf 100er Skala normieren
        DataEmodbEmotionAnger_normed = [i * 100 for i in test_list1 ]
        DataEmodbEmotionBoredom_normed = [i * 100 for i in test_list2 ]
        DataEmodbEmotionDisgust_normed = [i * 100 for i in Main.DataEmodbEmotionDisgust ]
        DataEmodbEmotionFear_normed = [i * 100 for i in Main.DataEmodbEmotionFear ]
        DataEmodbEmotionHappiness_normed = [i * 100 for i in Main.DataEmodbEmotionHappiness ]
        DataEmodbEmotionNeutral_normed = [i * 100 for i in Main.DataEmodbEmotionNeutral ]
        DataEmodbEmotionSadness_normed = [i * 100 for i in Main.DataEmodbEmotionSadness ]
        
        #self.lists = [Main.DataEmodbEmotionAnger, Main.DataEmodbEmotionBoredom, Main.DataEmodbEmotionDisgust, Main.DataEmodbEmotionFear, Main.DataEmodbEmotionHappiness, Main.DataEmodbEmotionNeutral, Main.DataEmodbEmotionSadness]

        #Neue Listen-Liste mit normierten Daten
        self.lists_normed = [DataEmodbEmotionAnger_normed,
                             DataEmodbEmotionBoredom_normed,
                             DataEmodbEmotionDisgust_normed,
                             DataEmodbEmotionFear_normed,
                             DataEmodbEmotionHappiness_normed,
                             DataEmodbEmotionNeutral_normed,
                             DataEmodbEmotionSadness_normed]
            

        self.figure, self.ax = plt.subplots(facecolor='#212121', figsize=(7, 3))
        self.figure.set_layout_engine("constrained")

        self.ax.set_title('Zeitlicher Verlauf – EmoDB', color = '#F2F2F2')

        self.ax.spines['bottom'].set_color('#F2F2F2')
        self.ax.spines['left'].set_color('#F2F2F2')
        self.ax.spines['top'].set_color('#212121')
        self.ax.spines['right'].set_color('#212121')
        

    def create_graph(self):
        #for i in range(7):
        self.ax.tick_params(color = "#F2F2F2", which = "both", labelcolor = "#F2F2F2")
        self.ax.set_facecolor(color = '#212121')
        
        

        self.ax.plot(self.lists_normed[0], label=f'Anger')
        self.ax.plot(self.lists_normed[1], label=f'Boredom')
        #self.ax.plot(self.lists_normed[2], label=f'Disgust')
        #self.ax.plot(self.lists_normed[3], label=f'Fear')
        #self.ax.plot(self.lists_normed[4], label=f'Happiness')
        #self.ax.plot(self.lists_normed[5], label=f'Neutral')
        #self.ax.plot(self.lists_normed[6], label=f'Sadness')
        self.ax.set_ylabel('Prozent', color = "#F2F2F2")
        self.ax.set_ylim(0,100)
        self.ax.set_xlabel('Time', color = '#F2F2F2')
        self.ax.set_xticklabels(["start"])
        self.ax.legend()
        self.ax.xaxis.set_visible(True)
        self.ax.legend().set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        #self.canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10, pady = 10)

#############################################################################
#### Graph mit zeitlichem Verlauf der einzelnen Emotionen von AbcAffect #####
#############################################################################


class GraphAbcOverTime(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.lists = [Main.DataAbcAffectAgressiv, Main.DataAbcAffectCheerfull,  Main.DataAbcAffectIntoxicated, Main.DataAbcAffectNervous, Main.DataAbcAffectNeutral, Main.DataAbcAffectTired]
        
        #Daten auf 100er Skala normieren
        DataAbcAffectAgressiv_normed = [i * 100 for i in Main.DataAbcAffectAgressiv]
        DataAbcAffectCheerfull_normed = [i * 100 for i in Main.DataAbcAffectCheerfull]
        DataAbcAffectIntoxicated_normed = [i * 100 for i in Main.DataAbcAffectIntoxicated]
        DataAbcAffectNervous_normed = [i * 100 for i in Main.DataAbcAffectNervous]
        DataAbcAffectNeutral_normed = [i * 100 for i in Main.DataAbcAffectNeutral]
        DataAbcAffectTired_normed = [i * 100 for i in Main.DataAbcAffectTired]

        #Neue Listen-Liste mit normierten Daten
        self.lists_normed = [
                                DataAbcAffectAgressiv_normed,
                                DataAbcAffectCheerfull_normed,
                                DataAbcAffectIntoxicated_normed,
                                DataAbcAffectNervous_normed,
                                DataAbcAffectNeutral_normed,
                                DataAbcAffectTired_normed
                            ]





        self.figure, self.ax = plt.subplots(facecolor='#212121', figsize=(20, 2))
        self.ax.set_title('Zeitlicher Verlauf – AbcAffect', color = '#F2F2F2')
        

    def create_graph(self):
        #for i in range(7):
        self.ax.plot(self.lists_normed[0], label=f'Agressive')
        self.ax.plot(self.lists_normed[1], label=f'Cheerfull')
        self.ax.plot(self.lists_normed[2], label=f'Intoxicated')
        self.ax.plot(self.lists_normed[3], label=f'Nervous')
        self.ax.plot(self.lists_normed[4], label=f'Neutral')
        self.ax.plot(self.lists_normed[5], label=f'Tired')
        self.ax.set_ylabel('Prozent', color = "#F2F2F2")
        self.ax.set_ylim(0,100)
        self.ax.set_xlabel('Time')
        self.ax.set_xticklabels(["start"])
        self.ax.legend()
        self.ax.xaxis.set_visible(False)
        self.ax.legend().set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


##################################################################
#### Balkendiagramm zum vergleich von soll und ist bei EmoDb #####
###################################################################


class BarChartEmo(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        if len(Main.Soll_Data_EmodbEmotion_List) == 7 and len(Main.Abs_MW_Data_EmodbEmotion_List) == 7:
            self.list1 = Main.Abs_MW_Data_EmodbEmotion_List
            self.list2 = Main.Soll_Data_EmodbEmotion_List
        else:
            self.list1 = [0.14,0.28,0.42,0.56,0.70,0.85,1]
            self.list2 = [0.14,0.28,0.42,0.56,0.70,0.85,1]

        self.list1_normed = [i * 100 for i in self.list1]
        self.list2_normed = [i * 100 for i in self.list2]
        

    

    def create_chart(self):
        x = [i for i in range(1,8)]
        
        # Create a new figure
        fig = Figure(figsize=(25,4))
        fig.set_facecolor('#212121')
        ax = fig.add_subplot(111)
        ax.set_facecolor("#212121")
        ax.tick_params(colors = "#F2F2F2", which = "both")

        ax.set_title('Emotionsmix – EmoDB', color = '#F2F2F2', pad=10)
        ax.set_ylabel('Prozent', color = "#F2F2F2")



        ax.spines['bottom'].set_color('#F2F2F2')
        ax.spines['left'].set_color('#F2F2F2')
        ax.spines['top'].set_color('#212121')
        ax.spines['right'].set_color('#212121')
        
        # Add the bar chart to the figure
        ax.bar(x, self.list1_normed, width=0.4)
        ax.bar([i+0.4 for i in x], self.list2_normed, width=0.4)
        
        # Set the y-axis range and hide the x-axis
        #ax.set_ylim(0, max(max(self.list1), max(self.list2)))
        ax.set_ylim(0,100)
        ax.set_xlim(0,8)
        ax.set_xticks([])
        
        # Create a canvas to display the chart
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



######################################################################
#### Balkendiagramm zum vergleich von soll und ist bei AbcAffect #####
######################################################################


class BarChartAbc(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if len(Main.Soll_Data_AbcAffect_List) == 6 and len(Main.Abs_MW_Data_AbcAffect_List) == 6:
            self.list1 = Main.Abs_MW_Data_AbcAffect_List
            self.list2 = Main.Soll_Data_AbcAffect_List
        else:
            self.list1 = [0.17,0.34,0.51,0.68,0.85,1]
            self.list2 = [0.17,0.34,0.51,0.68,0.85,1]

        self.list1_normed = [i * 100 for i in self.list1]
        self.list2_normed = [i * 100 for i in self.list2]

    def create_chart(self):
        x = [i for i in range(1,7)]
        
        # Create a new figure
        fig = Figure(figsize=(5,5))
        ax = fig.add_subplot(111)

        ax.set_title('Emotionsmix – AbcAffect', color = '#F2F2F2')
        ax.set_ylabel('Prozent', color = "#F2F2F2")
        
        # Add the bar chart to the figure
        ax.bar(x, self.list1_normed, width=0.4)
        ax.bar([i+0.4 for i in x], self.list2_normed, width=0.4)
        
        # Set the y-axis range and hide the x-axis
        ax.set_ylim(0, 100)
        ax.set_xlim(0,7)
        ax.set_xticks([])
        
        # Create a canvas to display the chart
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        
        
######################################################################
####               DonutDiagramm mit EmoDbEmotion                #####
######################################################################
        
        
class DonutEmo(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if len(Main.Abs_MW_Data_EmodbEmotion_List) == 7:
            self.list1 = Main.Abs_MW_Data_EmodbEmotion_List
        else:
            self.list1 = [1,1,1,1,1,1,1]
        
        self.labels = ["Anger", "Boredom" , "Disgust", "Fear", "Happiness", "Neutral", "Sadness"]
        self.explode_list = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        print(len(self.explode_list))

    def create_chart(self):
        # Create a new figure
        fig = Figure(figsize=(4,4))
        fig.set_layout_engine("constrained")
        fig.set_facecolor('#212121')
        ax = fig.add_subplot(111)

        ax.set_title('Mittlerer Emotionsmix der letzten 20 Sekunden', color = '#F2F2F2', pad=20)

        # Add the donut chart to the figure
        wedges, texts = ax.pie(self.list1, radius=1.0, wedgeprops=dict(width=0.5, edgecolor='#212121'), explode=self.explode_list)
        ax.pie([1], radius=0.5, wedgeprops=dict(width=0.5, edgecolor='#212121', facecolor='#212121'))

        # Add labels and lines to the segments
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(self.labels[i], xy=(x, y), xytext=(1.2*np.sign(x), 1.3*y),
                        horizontalalignment=horizontalalignment, color ="red", **kw)

        # Create a canvas to display the chart
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)






    