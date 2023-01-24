import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from TestDataExtractor2 import *
import customtkinter



#########################################################################
#### Graph mit zeitlichem Verlauf der einzelnen Emotionen von EmoDb #####
#########################################################################


class GraphEmoOverTime(customtkinter.CTkFrame):
    def __init__(self, master):
        self.master = master
        self.lists = [Main.DataEmodbEmotionAnger, Main.DataEmodbEmotionBoredom, Main.DataEmodbEmotionDisgust, Main.DataEmodbEmotionFear, Main.DataEmodbEmotionHappiness, Main.DataEmodbEmotionNeutral, Main.DataEmodbEmotionSadness]
        self.figure, self.ax = plt.subplots(facecolor='blue', figsize=(20, 2))
        

    def create_graph(self):
        #for i in range(7):
        self.ax.plot(self.lists[0], label=f'Anger')
        self.ax.plot(self.lists[1], label=f'Boredom')
        self.ax.plot(self.lists[2], label=f'Disgust')
        self.ax.plot(self.lists[3], label=f'Fear')
        self.ax.plot(self.lists[4], label=f'Happiness')
        self.ax.plot(self.lists[5], label=f'Neutral')
        self.ax.plot(self.lists[6], label=f'Sadness')
        self.ax.set_ylabel('Percentage')
        self.ax.set_ylim(0,1)
        self.ax.set_xlabel('Time')
        self.ax.set_xticklabels(["start"])
        self.ax.legend()
        self.ax.xaxis.set_visible(False)
        self.ax.legend().set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)







#############################################################################
#### Graph mit zeitlichem Verlauf der einzelnen Emotionen von AbcAffect #####
#############################################################################


class GraphAbcOverTime(customtkinter.CTkFrame):
    def __init__(self, master):
        self.master = master
        self.lists = [Main.DataAbcAffectAgressiv, Main.DataAbcAffectCheerfull,  Main.DataAbcAffectIntoxicated, Main.DataAbcAffectNervous, Main.DataAbcAffectNeutral, Main.DataAbcAffectTired]
        
        self.figure, self.ax = plt.subplots(facecolor='blue', figsize=(20, 2))
        

    def create_graph(self):
        #for i in range(7):
        self.ax.plot(self.lists[0], label=f'Agressive')
        self.ax.plot(self.lists[1], label=f'Cheerfull')
        self.ax.plot(self.lists[2], label=f'Intoxicated')
        self.ax.plot(self.lists[3], label=f'Nervous')
        self.ax.plot(self.lists[4], label=f'Neutral')
        self.ax.plot(self.lists[5], label=f'Tired')
        self.ax.set_ylabel('Percentage')
        self.ax.set_ylim(0,1)
        self.ax.set_xlabel('Time')
        self.ax.set_xticklabels(["start"])
        self.ax.legend()
        self.ax.xaxis.set_visible(False)
        self.ax.legend().set_visible(False)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)





##################################################################
#### Balkendiagramm zum vergleich von soll und ist bei EmoDb #####
###################################################################


class BarChartEmo(customtkinter.CTkFrame):
    def __init__(self, root):
        self.root = root
        self.list1 = Main.Abs_MW_Data_EmodbEmotion_List
        self.list2 = Main.Soll_Data_EmodbEmotion_List


    

    def create_chart(self):
        x = [i for i in range(1,8)]
        
        # Create a new figure
        fig = Figure(figsize=(5,5))
        ax = fig.add_subplot(111)
        
        # Add the bar chart to the figure
        ax.bar(x, self.list1, width=0.4)
        ax.bar([i+0.4 for i in x], self.list2, width=0.4)
        
        # Set the y-axis range and hide the x-axis
        ax.set_ylim(0, max(max(self.list1), max(self.list2))+1)
        ax.set_xlim(-1,8)
        ax.set_xticks([])
        
        # Create a canvas to display the chart
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()






######################################################################
#### Balkendiagramm zum vergleich von soll und ist bei AbcAffect #####
######################################################################


class BarChartAbc(customtkinter.CTkFrame):
    def __init__(self, root):
        self.root = root
        self.list1 = Main.Abs_MW_Data_AbcAffect_List
        self.list2 = Main.Soll_Data_AbcAffect_List

    def create_chart(self):
        x = [i for i in range(1,7)]
        
        # Create a new figure
        fig = Figure(figsize=(5,5))
        ax = fig.add_subplot(111)
        
        # Add the bar chart to the figure
        ax.bar(x, self.list1, width=0.4)
        ax.bar([i+0.4 for i in x], self.list2, width=0.4)
        
        # Set the y-axis range and hide the x-axis
        ax.set_ylim(0, max(max(self.list1), max(self.list2))+1)
        ax.set_xlim(0,7)
        ax.set_xticks([])
        
        # Create a canvas to display the chart
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()