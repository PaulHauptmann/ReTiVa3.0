import customtkinter
import TestDataExtractor2 as T
from Frames.Archive_Frames import *
from Frames.New_Analysis_Frames import *
from Frames.Mini_App_Frames import *
from Frames.SettingsFrames import *
from Frames.GraphFrames import *


class MainContainerFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        
        '''
        self.dummy_frame = customtkinter.CTkFrame(self, fg_color="green")
        self.dummy_frame.grid(row =0, column = 0, sticky = "nsew")
        #self.dummy_frame.grid_remove()
        '''
        
        self.hello = HelloFrame(self)
        self.hello.grid(row = 0, column = 0, sticky = "nsew")
        

        self.archive = ArchiveListFrame(self)
        self.archive.grid(row = 0, column = 0, sticky = "nsew")
        
        self.settings = SettingsFrame(self)
        self.settings.grid(row = 0, column = 0, sticky = "nsew")

        # Hier raus, wird in Windows.py --> NewAnalysisWindow gemacht
        '''self.big_analysis = BigLiveAnalysisFrame(self)
        self.big_analysis.grid(row = 0, column = 0, sticky = "nsew")
'''

        self.hello.lift()



    def show_settings(self):
        self.settings.lift()

    def show_archive(self):
        self.archive.lift()

    

        




class HelloFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(self, text= "Herzlich Willkommen zu ReTiVA – Real Time Voice Analystics!", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.title.grid(row = 0, column = 0, sticky = "n", pady = 30)

        '''self.graph = GraphEmoOverTime(self)
        self.graph.grid(row = 1, column = 0, pady = 20)
'''


class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        
        self.workingmode_selector = WeightsFrame(self)
        self.workingmode_selector.grid(row = 0, column = 0)




class BigLiveAnalysisFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.big_score = ScoreIndicatorFrame(self)
        self.big_score.grid(row = 0, column = 2)

        self.additonal_scores = AdditionalInfoFrame(self)
        self.additonal_scores.grid(row = 1, column = 1, columnspan = 2, pady = 20)

        #Works
        self.graph_soll_vs_ist = BarChartEmo(self)
        self.graph_soll_vs_ist.create_chart()
        self.graph_soll_vs_ist.grid(row = 0, column = 0)
        

        self.graph_emo_over_time = GraphEmoOverTime(self)
        self.graph_emo_over_time.create_graph()
        self.graph_emo_over_time.grid(row = 1, column = 0)

        #Works
        self.donut = DonutEmo(self)
        self.donut.configure(width = 20, height = 20)
        self.donut.create_chart()
        self.donut.grid(row = 0, column = 1, padx = 20, pady = 20)

        






