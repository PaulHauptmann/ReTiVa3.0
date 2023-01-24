import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from TestDataExtractor2 import *
import customtkinter


class Graph(customtkinter.CTkFrame):
    def __init__(self, master):
        self.master = master
        #self.lists = [Main.DataEmodbEmotionAnger, Main.DataEmodbEmotionBoredom, Main.DataEmodbEmotionDisgust, Main.DataEmodbEmotionFear, Main.DataEmodbEmotionHappiness, Main.DataEmodbEmotionNeutral, Main.DataEmodbEmotionSadness]
        List1 = [0.02045,0.017923,0.018713,0.025344,0.023188,0.02045,0.017923,0.018713,0.025344,0.023188,0.02045,0.017923,0.018713,0.025344,0.023188]
        List2 = [0.138412,0.19422,0.186691,0.156366,0.128637,0.138412,0.19422,0.186691,0.156366,0.128637,0.138412,0.19422,0.186691,0.156366,0.128637]
        List3 = [0.04431,0.029865,0.038684,0.04015,0.040236,0.04431,0.029865,0.038684,0.04015,0.040236,0.04431,0.029865,0.038684,0.04015,0.040236]
        List4 = [0.487324,0.466888,0.483346,0.504269,0.484201,0.487324,0.466888,0.483346,0.504269,0.484201,0.487324,0.466888,0.483346,0.504269,0.484201]
        List5 = [0.06931,0.059963,0.064439,0.0648,0.121022,0.06931,0.059963,0.064439,0.0648,0.121022,0.06931,0.059963,0.064439,0.0648,0.121022]
        List6 = [0.095925,0.126325,0.093476,0.154512,0.132145,0.095925,0.126325,0.093476,0.154512,0.132145,0.095925,0.126325,0.093476,0.154512,0.132145]
        List7 = [0.144269,0.104817,0.114652,0.05456,0.070571,0.144269,0.104817,0.114652,0.05456,0.070571,0.144269,0.104817,0.114652,0.05456,0.070571]
        self.lists = [List1,List2,List3,List4,List5,List6,List7]
        self.figure, self.ax = plt.subplots(facecolor='none', figsize=(20, 2))

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


