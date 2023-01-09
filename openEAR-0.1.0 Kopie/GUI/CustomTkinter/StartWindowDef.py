import customtkinter

class StartFrame (customtkinter.CTkToplevel):
    def __init__(self, *args, title, **kwargs):
        super().__init__(*args,  **kwargs)

        self.title = title
        
        
