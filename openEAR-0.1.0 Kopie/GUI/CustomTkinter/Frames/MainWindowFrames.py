import customtkinter
import TestDataExtractor2 as T
from Frames.Archive_Frames import *
from Frames.New_Analysis_Frames import *
from Frames.Mini_App_Frames import *
from Frames.SettingsFrames import *
from Frames.GraphFrames import *
from CustomObjects import *
import threading


class MainContainerFrame(customtkinter.CTkFrame):
    settings = None
    archive = None
    hello = None
    big_analysis = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        
        '''
        self.dummy_frame = customtkinter.CTkFrame(self, fg_color="green")
        self.dummy_frame.grid(row =0, column = 0, sticky = "nsew")
        #self.dummy_frame.grid_remove()
        '''
        
        self.hello = HelloFrame(self)
        self.hello.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.hello = self.hello
        

        self.archive = ArchiveListFrame(self)
        self.archive.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.archive = self.archive

        
        self.settings = SettingsFrame(self)
        self.settings.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.settings = self.settings


        self.big_analysis = BigLiveAnalysisFrame(self)
        self.big_analysis.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.big_analysis = self.big_analysis
        

        self.hello.lift()
        

        

        

    @classmethod
    def show_hello(cls):
        cls.hello.lift()
        print("Hello")

    @classmethod
    def show_archive(cls):
        cls.archive.lift()
        print("Archiv")

    @classmethod
    def show_settings(cls):
        cls.settings.lift()
        print("Einstellungen")
        
    @classmethod
    def show_big_analysis(cls):
        cls.big_analysis.lift()
    



        




class HelloFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(self, text= "Herzlich Willkommen zu ReTiVA – Real Time Voice Analystics!", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.title.grid(row = 0, column = 0, sticky = "n", pady = 30)

        self.test = GraphAbcOverTime(self)
        self.test.create_graph()
        self.test.grid(row = 1, column = 0)

        


class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.rowconfigure(1, weight=1)
        #self.columnconfigure(1, weight=1)

        self.title = customtkinter.CTkLabel(self, text="Settings", font=customtkinter.CTkFont(size = 30, weight="bold"))
        self.title.grid(row = 0, column = 0, padx = 20, pady = 50, sticky="nw")

        self.button_ok = customtkinter.CTkButton(self, text="Save", command = self.on_ok)
        self.button_ok.grid(row = 5, column = 4, padx = 10, pady = 10, sticky = "se")

        self.button_cancel = customtkinter.CTkButton(self, text="Cancel", command=self.on_cancel)
        self.button_cancel.grid(row = 5, column = 3, padx = 10, pady = 10, sticky = "sw")

        
        self.workingmode_selector = WeightsFrame(self, expand_all=True) 
        self.workingmode_selector.grid(row = 1, column = 1, rowspan = 3, sticky = "ew", padx = 10)

        self.audio_device_selector = AudioDeviceListFrame(self)
        self.audio_device_selector.grid(row = 1, column = 0, sticky = "ew", padx = 10)

        self.scales_selector = ScalesSettingsFrame(self)
        self.scales_selector.grid(row = 2, column = 0, padx = 10)

        self.emotions_settings_frame = EmotionSettingsFrame(self)
        self.emotions_settings_frame.grid(row = 3, column = 0, padx = 10)

        self.choose_model = BigAnalysisChooseModel(self)
        self.choose_model.grid(row = 1, column = 2, padx = 10, sticky = "ew")


    def on_ok(self):
        #self.destroy()
        MainContainerFrame.show_hello()

    def on_cancel(self):
        #self.destroy()
        MainContainerFrame.show_hello()




class BigLiveAnalysisFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color = "#212121")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.big_score = ScoreIndicatorFrame(self)
        self.big_score.grid(row = 0, column = 2)

        self.additonal_scores = AdditionalInfoFrame(self)
        self.additonal_scores.grid(row = 1, column = 1, columnspan = 2, pady = 20)

        if Startupsettings.show_abc_graphs == "AbcAffect":
            self.graph_abc= BarChartAbc(self)
            self.graph_abc.create_chart()
            self.graph_abc.grid(row = 0, column = 0)

            self.graph_abc_over_time = GraphAbcOverTime(self)
            self.graph_abc_over_time.grid(row = 1, column = 0, padx = 20, pady = 20)
            self.graph_abc_over_time.create_graph()

            print(Startupsettings.show_abc_graphs, "if")

        elif Startupsettings.show_abc_graphs == "EmoDB":
            self.graph_emo = BarChartEmo(self)
            self.graph_emo.create_chart()
            self.graph_emo.grid(row = 0, column = 0)

            self.graph_emo_over_time = GraphEmoOverTime(self)
            self.graph_emo_over_time.grid(row = 1, column = 0, padx = 20, pady = 20)
            self.graph_emo_over_time.create_graph()

            print(Startupsettings.show_abc_graphs,  "else")

    


        #Works
        self.donut = DonutEmo(self)
        self.donut.configure(width = 20, height = 20)
        self.donut.create_chart()
        self.donut.grid(row = 0, column = 1, padx = 20, pady = 20)

        






