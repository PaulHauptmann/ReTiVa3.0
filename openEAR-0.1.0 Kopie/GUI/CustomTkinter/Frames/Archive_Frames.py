import customtkinter
import tkinter as tk
import os
#from openpyxl import *
import openpyxl
import Frames.Archiv_Reader_3 as AR
from Frames.Archive_Graphs import *
from CustomObjects import *
from Frames.Mini_App_Frames import *


class ShelfListbox(tk.Listbox):
    def __init__(self, master):
        tk.Listbox.__init__(master, width=60)



class ArchiveListFrame(customtkinter.CTkFrame):    
    
    
    archive__Data_DateTime= []
    
    
    def __init__(self, master = None):
        super().__init__(master)

        # define filepath
        self.filepath = "openEAR-0.1.0 Kopie/SmileArchiv"

        #Label
        self.title_label = customtkinter.CTkLabel(self, text = "Archive: ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row = 0, column = 0, pady = 20)
        
        #Grid
        self.rowconfigure(1, weight=1)
        #self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        # create listbox
        self.listbox = tk.Listbox(self, borderwidth=0, selectbackground= '#F2F2F2', background='#212121', fg="#F2F2F2", width=23)
        self.listbox.grid(row = 1, column = 0, rowspan=2, padx=10, pady=10, sticky="nsew")

        #create Archive view
        self.archive_frame = ArchiveGraphsFrame(self)
        self.archive_frame.grid(row = 0, column = 1, rowspan = 2, padx = 10, pady = 10, sticky = "nsew")
        
        

        # populate listbox with Excel file names
        for file in os.listdir(self.filepath):
            if file.endswith(".xlsx"):
                self.listbox.insert(tk.END, file)

        '''# create textbox
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row = 0, column= 1, rowspan = 3, padx = 10, pady = 10, sticky="nsew")'''

        #Graphen-Frame importieren
        






        # bind listbox to open_excel_file function
        #self.listbox.bind("<Button-1>", self.open_excel_file)
        self.listbox.bind("<Button-1>", self.load_archive)

    def open_excel_file(self, event):
        widget = event.widget
        idx = widget.nearest(event.y)
        widget.activate(idx)
        selected_file = widget.get(idx)
        workbook = openpyxl.load_workbook(os.path.join(self.filepath, selected_file))
        sheet = workbook.active
        # Clear the textbox
        self.textbox.delete("1.0", tk.END)
        for row in sheet.iter_rows():
            for cell in row:
                try:
                    self.textbox.insert(tk.END, cell.value)
                except:
                    self.textbox.insert(tk.END, " ")

                self.textbox.insert(tk.END, " ")
            self.textbox.insert(tk.END, "\n")
    

    def load_archive(self, event):
        widget = event.widget
        idx = widget.nearest(event.y)
        widget.activate(idx)
        selected_file = widget.get(idx)

        data = AR.Get_Data("openEAR-0.1.0 Kopie/SmileArchiv/" + selected_file)
        Variablen.Set_Values(
            Set_Archive_Data_Time                                = data.get("Archive_Data_Time", "Key not found"),
            Set_Archive_Data_Aroual                              = data.get("Archive_Data_Arousal", "Key not found"),
            Set_Archive_Data_Valence                             = data.get("Archive_Data_Valence", "Key not found"),
            Set_Archive_Data_EmodbEmotionAnger                   = data.get("Archive_Data_EmodbEmotionAnger", "Key not found"),
            Set_Archive_Data_EmodbEmotionBoredm                  = data.get("Archive_Data_EmodbEmotionBoredom", "Key not found"),
            Set_Archive_Data_EmodbEmotionDisgust                 = data.get("Archive_Data_EmodbEmotionDisgust", "Key not found"),
            Set_Archive_Data_EmodbEmotionFear                    = data.get("Archive_Data_EmodbEmotionFear", "Key not found"),
            Set_Archive_Data_EmodbEmotionHappness                = data.get("Archive_Data_EmodbEmotionHappiness", "Key not found"),
            Set_Archive_Data_EmodbEmotionNeutral                 = data.get("Archive_Data_EmodbEmotionNeutral", "Key not found"),
            Set_Archive_Data_EmodbEmotionSadness                 = data.get("Archive_Data_EmodbEmotionSadness", "Key not found"),
            Set_Archive_Data_AbcAffectAgressiv                   = data.get("Archive_Data_AbcAffectAgressiv", "Key not found"),
            Set_Archive_Data_AbcAffectCheerful                   = data.get("Archive_Data_AbcAffectCheerfull", "Key not found"),
            Set_Archive_Data_AbcAffectIntoxicatd                 = data.get("Archive_Data_AbcAffectIntoxicated", "Key not found"),
            Set_Archive_Data_AbcAffectNervous                    = data.get("Archive_Data_AbcAffectNervous", "Key not found"),
            Set_Archive_Data_AbcAffectNeutral                    = data.get("Archive_Data_AbcAffectNeutral", "Key not found"),
            Set_Archive_Data_AbcAffectTired                      = data.get("Archive_Data_AbcAffectTired", "Key not found"),
            Set_Archive_Data_Loi1                                = data.get("Archive_Data_Loi1", "Key not found"),
            Set_Archive_Data_Loi2                                = data.get("Archive_Data_Loi2", "Key not found"),
            Set_Archive_Data_Loi3                                = data.get("Archive_Data_Loi3", "Key not found"),
            Set_Archive_Soll_DataEmodbEmotionAnger               = data.get("Archive_Soll_DataEmodbEmotionAnger", "Key not found"),
            Set_Archive_Soll_DataEmodbEmotionBoredom             = data.get("Archive_Soll_DataEmodbEmotionBoredom", "Key not found"),
            Set_Archive_Soll_DataEmodbEmotionDisgust             = data.get("Archive_Soll_DataEmodbEmotionDisgust", "Key not found"),
            Set_Archive_Soll_DataEmodbEmotionFear                = data.get("Archive_Soll_DataEmodbEmotionFear", "Key not found"),
            Set_Archive_Soll_DataEmodbEmotionHappiness           = data.get("Archive_Soll_DataEmodbEmotionHappiness", "Key not found"),
            Set_Archive_Soll_DataEmodbEmotionNeutral             = data.get("Archive_Soll_DataEmodbEmotionNeutral", "Key not found"),
            Set_Archive_Soll_DataEmodbEmotionSadness             = data.get("Archive_Soll_DataEmodbEmotionSadness", "Key not found"),
            Set_Archive_Soll_DataAbcAffectAgressiv               = data.get("Archive_Soll_DataAbcAffectAgressiv", "Key not found"),
            Set_Archive_Soll_DataAbcAffectCheerfull              = data.get("Archive_Soll_DataAbcAffectCheerfull", "Key not found"),
            Set_Archive_Soll_DataAbcAffectIntoxicated            = data.get("Archive_Soll_DataAbcAffectIntoxicated", "Key not found"),
            Set_Archive_Soll_DataAbcAffectNervous                = data.get("Archive_Soll_DataAbcAffectNervous", "Key not found"),
            Set_Archive_Soll_DataAbcAffectNeutral                = data.get("Archive_Soll_DataAbcAffectNeutral", "Key not found"),
            Set_Archive_Soll_DataAbcAffectTired                  = data.get("Archive_Soll_DataAbcAffectTired", "Key not found"),
            Set_Archive_Abs_MW_Data_Arousal                      = data.get("Archive_Abs_MW_Data_Arousal", "Key not found"),
            Set_Archive_Abs_MW_Data_Valence                      = data.get("Archive_Abs_MW_Data_Valence", "Key not found"),
            Set_Archive_Abs_MW_Data_EmodbEmotionAnger            = data.get("Archive_Abs_MW_Data_EmodbEmotionAnger", "Key not found"),
            Set_Archive_Abs_MW_Data_EmodbEmotionBoredom          = data.get("Archive_Abs_MW_Data_EmodbEmotionBoredom", "Key not found"),
            Set_Archive_Abs_MW_Data_EmodbEmotionDisgust          = data.get("Archive_Abs_MW_Data_EmodbEmotionDisgust", "Key not found"),
            Set_Archive_Abs_MW_Data_EmodbEmotionFear             = data.get("Archive_Abs_MW_Data_EmodbEmotionFear", "Key not found"),
            Set_Archive_Abs_MW_Data_EmodbEmotionHappiness        = data.get("Archive_Abs_MW_Data_EmodbEmotionHappiness", "Key not found"),
            Set_Archive_Abs_MW_Data_EmodbEmotionNeutral          = data.get("Archive_Abs_MW_Data_EmodbEmotionNeutral", "Key not found"),
            Set_Archive_Abs_MW_Data_EmodbEmotionSadness          = data.get("Archive_Abs_MW_Data_EmodbEmotionSadness", "Key not found"),
            Set_Archive_Abs_MW_Data_AbcAffectAgressiv            = data.get("Archive_Abs_MW_Data_AbcAffectAgressiv", "Key not found"),
            Set_Archive_Abs_MW_Data_AbcAffectCheerfull           = data.get("Archive_Abs_MW_Data_AbcAffectCheerfull", "Key not found"),
            Set_Archive_Abs_MW_Data_AbcAffectIntoxicated         = data.get("Archive_Abs_MW_Data_AbcAffectIntoxicated", "Key not found"),
            Set_Archive_Abs_MW_Data_AbcAffectNervous             = data.get("Archive_Abs_MW_Data_AbcAffectNervous", "Key not found"),
            Set_Archive_Abs_MW_Data_AbcAffectNeutral             = data.get("Archive_Abs_MW_Data_AbcAffectNeutral", "Key not found"),
            Set_Archive_Abs_MW_Data_AbcAffectTired               = data.get("Archive_Abs_MW_Data_AbcAffectTired", "Key not found"),
            Set_Archive_Abs_MW_Data_Loi1                         = data.get("Archive_Abs_MW_Data_Loi1", "Key not found"),
            Set_Archive_Abs_MW_Data_Loi2                         = data.get("Archive_Abs_MW_Data_Loi2", "Key not found"),
            Set_Archive_Abs_MW_Data_Loi3                         = data.get("Archive_Abs_MW_Data_Loi3", "Key not found"),
            Set_Archive_Score_EmodbEmotions                      = data.get("Archive_Score_EmodbEmotions", "Key not found"),
            Set_Archive_Score_AbcAffect                          = data.get("Archive_Score_AbcAffect", "Key not found"),
            Set_Archive_Score_Retiva                             = data.get("Archive_Score_Retiva", "Key not found"),
            Set_Archive_Abs_MW_Loi_Score                         = data.get("Archive_Abs_MW_Loi_Score", "Key not found")
        )
        
        test = [0.2, 0.1, 0.1, 0.2, 0.2, 0.1, 0.8]

        self.archive_frame.big_analysis_emo.donut.update_chart(test)
        self.archive_frame.big_analysis_abc.donut.update_chart(test)
        
        
        
        
        # Hier Klassenmethode zum Laden des Archivs feuern
        print(selected_file)
        



class ArchiveGraphsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.analysis_frame = customtkinter.CTkFrame(self)
        self.analysis_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.analysis_frame = self.analysis_frame

        self.current_time = Stopwatch(self.analysis_frame)
        #self.current_time.grid(row = 0, column = 0, sticky = "ne", padx = 20, pady = (15,0))
        self.__class__.current_time= self.current_time


        self.current_session_name = customtkinter.CTkLabel(self.analysis_frame, text=" ", font=customtkinter.CTkFont(size=20))
        #self.current_session_name.grid(row = 0, column = 0, sticky = "nw", padx = 20, pady = (10,0))
        self.__class__.current_session_name = self.current_session_name


        #Tabs erstellen
        self.tabview = customtkinter.CTkTabview(self.analysis_frame)
        self.tabview.grid(row = 0, column = 0, sticky = "nsew")

        emo_tab = self.tabview.add('EmoDB')
        abc_tab = self.tabview.add('AbcAffect')


        self.big_analysis_emo = BigLiveAnalysisFrame_Emo_Archive(emo_tab)
        self.big_analysis_emo.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.big_analysis_emo = self.big_analysis_emo

        self.big_analysis_abc = BigLiveAnalysisFrame_Abc_Archive(abc_tab)
        self.big_analysis_abc.grid(row = 0, column = 0, sticky = "nsew")
        self.__class__.big_analysis_abc = self.big_analysis_abc




class BigLiveAnalysisFrame_Emo_Archive(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color = "#212121")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        self.scores_frame = customtkinter.CTkFrame(self)
        self.scores_frame.grid(row = 1, column = 1, columnspan = 2, pady = (0,5), padx = (10,0))

        self.big_score = ScoreIndicatorFrame(self.scores_frame)
        self.big_score.grid(row = 0, column = 2)

        self.additonal_scores = AdditionalInfoFrame(self.scores_frame, show_all_scales=True)
        self.additonal_scores.grid(row = 0, column = 1)


        self.graph_emo = BarChartEmo_Archive(self)
        self.graph_emo.create_chart()
        self.graph_emo.grid(row = 0, column = 0, padx = 5)

        self.graph_emo_over_time = GraphEmoOverTime_Archive(self)
        self.graph_emo_over_time.grid(row = 1, column = 0, padx = 10, sticky = "s")
        self.graph_emo_over_time.create_graph()

        self.donut = DonutEmo_Archive(self)
        self.donut.configure(width = 20, height = 20)
        self.donut.create_chart()
        self.donut.grid(row = 0, column = 1, padx = 10)



class BigLiveAnalysisFrame_Abc_Archive(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color = "#212121")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.scores_frame = customtkinter.CTkFrame(self)
        self.scores_frame.grid(row = 1, column = 1, columnspan = 2, pady = (0,5), padx = (10,0))


        self.big_score = ScoreIndicatorFrame(self.scores_frame)
        self.big_score.grid(row = 0, column = 2)

        self.additonal_scores = AdditionalInfoFrame(self.scores_frame, show_all_scales=True)
        self.additonal_scores.grid(row = 0, column = 1)

       
        self.graph_abc= BarChartAbc_Archive(self)
        self.graph_abc.create_chart()
        self.graph_abc.grid(row = 0, column = 0, padx = 5)

        self.graph_abc_over_time = GraphAbcOverTime_Archive(self)
        self.graph_abc_over_time.create_graph()    
        self.graph_abc_over_time.grid(row = 1, column = 0, padx = 10, sticky = "s")


        self.donut = DonutAbc_Archive(self)
        self.donut.configure(width = 20, height = 20)
        self.donut.create_chart()
        self.donut.grid(row = 0, column = 1, padx = 20)