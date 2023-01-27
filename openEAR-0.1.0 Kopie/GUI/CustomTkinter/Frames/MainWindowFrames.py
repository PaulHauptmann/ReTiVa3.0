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
    big_analysis_emo = None
    big_analysis_abc = None
    analysis_frame = None
    current_time = None
    current_session_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rowconfigure(1, weight=1)
        
        self.hello = HelloFrame(self)
        self.hello.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.hello = self.hello
        

        self.archive = ArchiveListFrame(self)
        self.archive.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.archive = self.archive

        
        self.settings = SettingsFrame(self)
        self.settings.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.settings = self.settings

        #Frame für große Analyse mit Tabs für emo und abc
        self.analysis_frame = customtkinter.CTkFrame(self)
        self.analysis_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.analysis_frame = self.analysis_frame

        '''self.current_time = customtkinter.CTkLabel(self.analysis_frame, text="00:05:43", font=customtkinter.CTkFont(size=20))
        self.current_time.grid(row = 0, column = 0, sticky = "ne", padx = 20, pady = (10,0))'''

        self.current_time = Stopwatch(self.analysis_frame)
        self.current_time.grid(row = 0, column = 0, sticky = "ne", padx = 20, pady = (15,0))
        self.__class__.current_time= self.current_time


        self.current_session_name = customtkinter.CTkLabel(self.analysis_frame, text=" ", font=customtkinter.CTkFont(size=20))
        self.current_session_name.grid(row = 0, column = 0, sticky = "nw", padx = 20, pady = (10,0))
        self.__class__.current_session_name = self.current_session_name


        #Tabs erstellen
        self.tabview = customtkinter.CTkTabview(self.analysis_frame)
        self.tabview.grid(row = 1, column = 0, sticky = "nsew")

        emo_tab = self.tabview.add('EmoDB')
        abc_tab = self.tabview.add('AbcAffect')


        self.big_analysis_emo = BigLiveAnalysisFrame_Emo(emo_tab)
        self.big_analysis_emo.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.big_analysis_emo = self.big_analysis_emo

        self.big_analysis_abc = BigLiveAnalysisFrame_Abc(abc_tab)
        self.big_analysis_abc.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.big_analysis_abc = self.big_analysis_abc
        

        self.analysis_frame.lift()
        #self.archive.lift()
        

        

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
        cls.analysis_frame.lift()

    @classmethod
    def update_analysis_window(cls):
        cls.big_analysis_emo.updade_widgets()
        cls.big_analysis_abc.updade_widgets()

    @classmethod
    def start_clock(cls):
        cls.current_time.start()
    
    @classmethod
    def set_window_session_name(cls):
        cls.current_session_name.configure(text = Main.Excel_Filename)
    
    @classmethod
    def stop_clock(cls):
        cls.current_time.stop()

        
    



        




class HelloFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(self, text= "Herzlich Willkommen zu ReTiVA – Real Time Voice Analystics!", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.title.grid(row = 0, column = 0, sticky = "n", pady = 30)

        
        


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



#Alt
class BigLiveAnalysisFrame_old(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color = "#212121")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.big_score = ScoreIndicatorFrame(self)
        self.big_score.grid(row = 0, column = 2)

        self.additonal_scores = AdditionalInfoFrame(self, show_all_scales=True)
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
        

    
    def updade_widgets(self):
        
        self.donut.update_widget()
        self.big_score.indicator.update_widget(Main.Score_Retiva)
        print("Updated Donut")
        


        #Mini Fenster Update der Emotions-Labels
        try:
            self.additonal_scores.emotion_label.set(Main.get_highest_EmoDb())
            self.additonal_scores.double_label.set(Main.get_highest_EmoDb(), Main.get_highest_AbcAffect())
        except AttributeError:
            pass
        
        #Mini Fenster Update der Scores
        self.additonal_scores.loi_indicator.update_widget(Main.Abs_MW_Loi_Score)
        self.additonal_scores.arousal_indicator.update_widget(Main.Abs_MW_Data_Arousal)
        self.additonal_scores.valence_indicator.update_widget(Main.Abs_MW_Data_Valence)
        self.additonal_scores.redeanteil.update_widget(Main.DataSpeakRatio[-1])


#EmoDB Analyse Übersicht
class BigLiveAnalysisFrame_Emo(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color = "#212121")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        self.scores_frame = customtkinter.CTkFrame(self)
        self.scores_frame.grid(row = 1, column = 1, columnspan = 2, pady = (0,20), padx = (150,0))

        self.big_score = ScoreIndicatorFrame(self.scores_frame)
        self.big_score.grid(row = 0, column = 2)

        self.additonal_scores = AdditionalInfoFrame(self.scores_frame, show_all_scales=True)
        self.additonal_scores.grid(row = 0, column = 1, pady = (0,20))


        self.graph_emo = BarChartEmo(self)
        self.graph_emo.create_chart()
        self.graph_emo.grid(row = 0, column = 0, padx = 5)

        self.graph_emo_over_time = GraphEmoOverTime(self)
        self.graph_emo_over_time.grid(row = 1, column = 0, padx = 20, sticky = "n")
        self.graph_emo_over_time.create_graph()

        self.donut = DonutEmo(self)
        self.donut.configure(width = 20, height = 20)
        self.donut.create_chart()
        self.donut.grid(row = 0, column = 1, padx = 20)
        

    
    def updade_widgets(self):
        #TODO: Fehlende Updater schreiben und hinzufügen
        self.donut.update_chart(Main.Abs_MW_Data_EmodbEmotion_List)

        self.big_score.indicator.update_widget(Main.Score_Retiva)
        


        #Mini Fenster Update der Emotions-Labels
        try:
            self.additonal_scores.emotion_label.set(Main.get_highest_EmoDb())
            self.additonal_scores.double_label.set(Main.get_highest_EmoDb(), Main.get_highest_AbcAffect())
        except AttributeError:
            pass
        
        #Mini Fenster Update der Scores
        self.additonal_scores.loi_indicator.update_widget(Main.Abs_MW_Loi_Score)
        self.additonal_scores.arousal_indicator.update_widget(Main.Abs_MW_Data_Arousal)
        self.additonal_scores.valence_indicator.update_widget(Main.Abs_MW_Data_Valence)
        self.additonal_scores.redeanteil.update_widget(Main.DataSpeakRatio[-1])
        

#Abc Analyse Übersicht
class BigLiveAnalysisFrame_Abc(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color = "#212121")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.scores_frame = customtkinter.CTkFrame(self)
        self.scores_frame.grid(row = 1, column = 1, columnspan = 2, pady = (0,20), padx = (150,0))

        self.big_score = ScoreIndicatorFrame(self.scores_frame)
        self.big_score.grid(row = 0, column = 2)

        self.additonal_scores = AdditionalInfoFrame(self.scores_frame, show_all_scales=True)
        self.additonal_scores.grid(row = 0, column = 1, pady = (0,20))

       
        self.graph_abc= BarChartAbc(self)
        self.graph_abc.create_chart()
        self.graph_abc.grid(row = 0, column = 0, padx = 5)

        self.graph_abc_over_time = GraphAbcOverTime(self)
        self.graph_abc_over_time.grid(row = 1, column = 0, padx = 20, sticky = "n")
        self.graph_abc_over_time.create_graph()    


        self.donut = DonutAbc(self)
        self.donut.configure(width = 20, height = 20)
        self.donut.create_chart()
        self.donut.grid(row = 0, column = 1, padx = 20)
        

    
    def updade_widgets(self):
        #TODO: Fehlende Updater schreiben und hinzufügen
        self.donut.update_chart(Main.Abs_MW_Data_AbcAffect_List)
        self.big_score.indicator.update_widget(Main.Score_Retiva)
        

        #Mini Fenster Update der Emotions-Labels
        try:
            self.additonal_scores.emotion_label.set(Main.get_highest_EmoDb())
            self.additonal_scores.double_label.set(Main.get_highest_EmoDb(), Main.get_highest_AbcAffect())
        except AttributeError:
            pass
        
        #Mini Fenster Update der Scores
        self.additonal_scores.loi_indicator.update_widget(Main.Abs_MW_Loi_Score)
        self.additonal_scores.arousal_indicator.update_widget(Main.Abs_MW_Data_Arousal)
        self.additonal_scores.valence_indicator.update_widget(Main.Abs_MW_Data_Valence)
        self.additonal_scores.redeanteil.update_widget(Main.DataSpeakRatio[-1])



