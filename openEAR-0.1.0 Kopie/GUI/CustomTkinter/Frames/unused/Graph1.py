import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
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


