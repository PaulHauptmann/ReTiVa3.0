import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from matplotlib.figure import Figure
from TestDataExtractor2 import *
import customtkinter



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