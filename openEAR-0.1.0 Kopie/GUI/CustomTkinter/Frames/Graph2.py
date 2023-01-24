import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from TestDataExtractor2 import *
import customtkinter



#############################################################################
#### Graph mit zeitlichem Verlauf der einzelnen Emotionen von AbcAffect #####
#############################################################################


class Graph(customtkinter.CTkFrame):
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


