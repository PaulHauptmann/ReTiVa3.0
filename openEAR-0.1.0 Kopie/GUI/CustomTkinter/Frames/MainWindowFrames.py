import customtkinter
import TestDataExtractor2 as T
from Frames.Archive_Frames import *
from Frames.New_Analysis_Frames import *
from Frames.SettingsFrames import *

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


class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        
        self.workingmode_selector = WeightsFrame(self)
        self.workingmode_selector.grid(row = 0, column = 0)
        






