import customtkinter
import TestDataExtractor2 as T

class MainContainerFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        
        
        self.dummy_frame = customtkinter.CTkFrame(self, fg_color="green")
        self.dummy_frame.grid(row =0, column = 0, sticky = "nsew")
        #self.dummy_frame.grid_remove()

        
        self.hello = HelloFrame(self)
        self.hello.grid(row = 0, column = 0)
        #self.hello.grid_remove()

        self.dummy_frame.lift()

    def show_settings(self):
        self.hello.lift()

    

        




class HelloFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(self, text= "Herzlich Willkommen zu ReTiVA – Real Time Voice Analystics!", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.title.grid(row = 0, column = 0, sticky = "n", pady = 30)

        

    def show_settings():
        print("test")


