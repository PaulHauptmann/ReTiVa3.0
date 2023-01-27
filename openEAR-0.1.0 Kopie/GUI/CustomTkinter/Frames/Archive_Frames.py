import customtkinter
import tkinter as tk
import os
from openpyxl import *
import Frames.Archiv_Reader_3 as AR
from Frames.Archive_Graphs import *



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
        self.title_label = customtkinter.CTkLabel(self, text = "Archiv: ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row = 0, column = 0, pady = 20)
        
        #Grid
        self.rowconfigure(1, weight=1)
        #self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        # create listbox
        self.listbox = tk.Listbox(self, borderwidth=0, selectbackground= '#F2F2F2', background='#212121', fg="#F2F2F2", width=30)
        self.listbox.grid(row = 1, column = 0, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        self.archive_frame = GraphEmoOverTime_Archive(self)
        self.archive_frame.create_graph()
        self.archive_frame.grid(row = 1, column = 1, sticky = "nsew")

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
        workbook = load_workbook(os.path.join(self.filepath, selected_file))
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
            archive__Data_DateTime                           = AR.data.get("Archive_Data_DateTime", "Key not found"),
            archive__Data_SessionNme                         = AR.data.get("Archive_Data_SessionName", "Key not found"),
            archive__Data_Time                               = AR.data.get("Archive_Data_Time", "Key not found"),
            archive__Data_Aroual                             = AR.data.get("Archive_Data_Arousal", "Key not found"),
            archive__Data_Valence                            = AR.data.get("Archive_Data_Valence", "Key not found"),
            archive__Data_EmodbEmtionAnger                   = AR.data.get("Archive_Data_EmodbEmotionAnger", "Key not found"),
            archive__Data_EmodbEmotionBoredm                 = AR.data.get("Archive_Data_EmodbEmotionBoredom", "Key not found"),
            archive__Data_EmodbEmotionDisgust                = AR.data.get("Archive_Data_EmodbEmotionDisgust", "Key not found"),
            archive__Data_EmodbEmotionFear                   = AR.data.get("Archive_Data_EmodbEmotionFear", "Key not found"),
            archive__Data_EmodbEmotionHappness               = AR.data.get("Archive_Data_EmodbEmotionHappiness", "Key not found"),
            archive__Data_EmodbEmotionNeutral                = AR.data.get("Archive_Data_EmodbEmotionNeutral", "Key not found"),
            archive__Data_EmodbEmotionSadness                = AR.data.get("Archive_Data_EmodbEmotionSadness", "Key not found"),
            archive__Data_AbcAffectAgressiv                  = AR.data.get("Archive_Data_AbcAffectAgressiv", "Key not found"),
            archive__Data_AbcAffectCheerful                  = AR.data.get("Archive_Data_AbcAffectCheerfull", "Key not found"),
            archive__Data_AbcAffectIntoxicatd                = AR.data.get("Archive_Data_AbcAffectIntoxicated", "Key not found"),
            archive__Data_AbcAffectNervous                   = AR.data.get("Archive_Data_AbcAffectNervous", "Key not found"),
            archive__Data_AbcAffectNeutral                   = AR.data.get("Archive_Data_AbcAffectNeutral", "Key not found"),
            archive__Data_AbcAffectTired                     = AR.data.get("Archive_Data_AbcAffectTired", "Key not found"),
            archive__Data_Loi1                               = AR.data.get("Archive_Data_Loi1", "Key not found"),
            archive__Data_Loi2                               = AR.data.get("Archive_Data_Loi2", "Key not found"),
            archive__Data_Loi3                               = AR.data.get("Archive_Data_Loi3", "Key not found"),
            Archive_Soll_DataEmodbEmotionAnger               = AR.data.get('Archive_Soll_DataEmodbEmotionAnger', "Key not found"),
            Archive_Soll_DataEmodbEmotionBoredom             = AR.data.get('Archive_Soll_DataEmodbEmotionBoredom', "Key not found"),
            Archive_Soll_DataEmodbEmotionDisgust             = AR.data.get('Archive_Soll_DataEmodbEmotionDisgust', "Key not found"),
            Archive_Soll_DataEmodbEmotionFear                = AR.data.get('Archive_Soll_DataEmodbEmotionFear', "Key not found"),
            Archive_Soll_DataEmodbEmotionHappiness           = AR.data.get('Archive_Soll_DataEmodbEmotionHappiness', "Key not found"),
            Archive_Soll_DataEmodbEmotionNeutral             = AR.data.get('Archive_Soll_DataEmodbEmotionNeutral', "Key not found"),
            Archive_Soll_DataEmodbEmotionSadness             = AR.data.get('Archive_Soll_DataEmodbEmotionSadness', "Key not found"),
            Archive_Soll_DataEmodbEmotion_List               = AR.data.get('Archive_Soll_DataEmodbEmotion_List',  "Key not found"),
            Archive_Soll_DataAbcAffectAgressiv               = AR.data.get('Archive_Soll_DataAbcAffectAgressiv', "Key not found"),
            Archive_Soll_DataAbcAffectCheerfull              = AR.data.get('Archive_Soll_DataAbcAffectCheerfull', "Key not found"),
            Archive_Soll_DataAbcAffectIntoxicated            = AR.data.get('Archive_Soll_DataAbcAffectIntoxicated', "Key not found"),
            Archive_Soll_DataAbcAffectNervous                = AR.data.get('Archive_Soll_DataAbcAffectNervous', "Key not found"),
            Archive_Soll_DataAbcAffectNeutral                = AR.data.get('Archive_Soll_DataAbcAffectNeutral', "Key not found"),
            Archive_Soll_DataAbcAffectTired                  = AR.data.get('Archive_Soll_DataAbcAffectTired', "Key not found"),
            Archive_Soll_DataAbcAffect_List                  = AR.data.get('Archive_Soll_DataAbcAffect_List',  "Key not found"),
            Archive_Abs_MW_Data_Arousal                      = AR.data.get('Archive_Abs_MW_Data_Arousal', "Key not found"),
            Archive_Abs_MW_Data_Valence                      = AR.data.get('Archive_Abs_MW_Data_Valence', "Key not found"),
            Archive_Abs_MW_Data_EmodbEmotionAnger            = AR.data.get('Archive_Abs_MW_Data_EmodbEmotionAnger', "Key not found"),
            Archive_Abs_MW_Data_EmodbEmotionBoredom          = AR.data.get('Archive_Abs_MW_Data_EmodbEmotionBoredom', "Key not found"),
            Archive_Abs_MW_Data_EmodbEmotionDisgust          = AR.data.get('Archive_Abs_MW_Data_EmodbEmotionDisgust', "Key not found"),
            Archive_Abs_MW_Data_EmodbEmotionFear             = AR.data.get('Archive_Abs_MW_Data_EmodbEmotionFear', "Key not found"),
            Archive_Abs_MW_Data_EmodbEmotionHappiness        = AR.data.get('Archive_Abs_MW_Data_EmodbEmotionHappiness', "Key not found"),
            Archive_Abs_MW_Data_EmodbEmotionNeutral          = AR.data.get('Archive_Abs_MW_Data_EmodbEmotionNeutral', "Key not found"),
            Archive_Abs_MW_Data_EmodbEmotionSadness          = AR.data.get('Archive_Abs_MW_Data_EmodbEmotionSadness', "Key not found"),
            Archive_Abs_MW_Data_EmodbEmotion_List            = AR.data.get('Archive_Abs_MW_Data_EmodbEmotion_List',  "Key not found"),
            Archive_Abs_MW_Data_AbcAffectAgressiv            = AR.data.get('Archive_Abs_MW_Data_AbcAffectAgressiv', "Key not found"),
            Archive_Abs_MW_Data_AbcAffectCheerfull           = AR.data.get('Archive_Abs_MW_Data_AbcAffectCheerfull', "Key not found"),
            Archive_Abs_MW_Data_AbcAffectIntoxicated         = AR.data.get('Archive_Abs_MW_Data_AbcAffectIntoxicated', "Key not found"),
            Archive_Abs_MW_Data_AbcAffectNervous             = AR.data.get('Archive_Abs_MW_Data_AbcAffectNervous', "Key not found"),
            Archive_Abs_MW_Data_AbcAffectNeutral             = AR.data.get('Archive_Abs_MW_Data_AbcAffectNeutral', "Key not found"),
            Archive_Abs_MW_Data_AbcAffectTired               = AR.data.get('Archive_Abs_MW_Data_AbcAffectTired', "Key not found"),
            Archive_Abs_MW_Data_AbcAffect_List               = AR.data.get('Archive_Abs_MW_Data_AbcAffect_List',  "Key not found"),
            Archive_Abs_MW_Data_Loi1                         = AR.data.get('Archive_Abs_MW_Data_Loi1', "Key not found"),
            Archive_Abs_MW_Data_Loi2                         = AR.data.get('Archive_Abs_MW_Data_Loi2', "Key not found"),
            Archive_Abs_MW_Data_Loi3                         = AR.data.get('Archive_Abs_MW_Data_Loi3', "Key not found"),
            Archive_Score_EmodbEmotions                      = AR.data.get('Archive_Score_EmodbEmotions', "Key not found"),
            Archive_Score_AbcAffect                          = AR.data.get('Archive_Score_AbcAffect', "Key not found"),
            Archive_Score_Retiva                             = AR.data.get('Archive_Score_Retiva', "Key not found"),
            Archive_Abs_MW_Loi_Score                         = AR.data.get('Archive_Abs_MW_Loi_Score', "Key not found")
        )
        
        
        
        
        
        
        # Hier Klassenmethode zum Laden des Archivs feuern
        print(selected_file)
        
#print("Hello World")