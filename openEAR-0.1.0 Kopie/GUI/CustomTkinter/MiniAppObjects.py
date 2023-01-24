import tkinter as tk
from tkinter import PhotoImage, Image
import sys
from PIL import ImageTk, Image
import customtkinter
from CustomObjects import *
import TestDataExtractor2 as T
import json as j

'''class LinearIndicator_old(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Load the image file as a PhotoImage object
        self.arrow_image = PhotoImage(file="openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/Ampel.png").subsample(4,4)
        self.image = PhotoImage(file="openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/arrow_red.png").subsample(3,3)
        
        # Create a canvas 
        self.canvas = tk.Canvas(self, width=self.arrow_image.width(), height=self.arrow_image.height())
        self.canvas.pack()
        
        # Create an image item on the canvas
        self.arrow_image = self.canvas.create_image(0, 0, image=self.arrow_image, anchor="center")
        self.rectangle_image = self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.tag_raise(self.arrow_image)

    def set_position(self, pos):
        # Move the arrow to the specified position
        self.canvas.move(self.arrow_image,0, pos)
'''

class ScoreIndicator(customtkinter.CTkFrame):
    def __init__(self, master = None):
        super().__init__(master)

        self.columnconfigure(0, weight=1)

        rows = 100
        for i in range(rows):
            self.rowconfigure(i, weight=1)


        # Load the image file as a PhotoImage object
        self.arrow_image = customtkinter.CTkImage(light_image=Image.open("openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/arrow.png"))
        self.image = customtkinter.CTkImage(light_image=Image.open("openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/Ampel.png"), size=(40, 180))
        #self.img = ImageTk.PhotoImage(Image.open("openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/Ampel.png"))

        
        self.dummy_label = customtkinter.CTkLabel(self, text="", width=20, height=1, fg_color="transparent")
        self.dummy_label.grid(row = 0, column = 0, sticky = "e")
        self.dummy_label.lower()
        
        self.label = customtkinter.CTkLabel(self, image=self.image, text="")
        self.label.grid(row = 0, column = 1,rowspan = 100, sticky = "e", padx = 10)

        self.arrow = customtkinter.CTkLabel(self, image=self.arrow_image, text="", fg_color='transparent')
        self.arrow.grid(row = 0, column = 0, sticky = "e")
        
        #self.arrow_char = customtkinter.CTkLabel(self, text= ">", fg_color="transparent", font=customtkinter.CTkFont(size=20, weight="bold"))
        #self.arrow_char.grid(row = 0, column = 0)
        self.update_widget(rel_y = 0.8)



    def update_widget(self, rel_y):
        # Get the number of rows in the grid
        rows = self.grid_size()[1]

        # Calculate the row number to place the label at
        row_num = int((1-rel_y) * rows)

        # Remove the label from its current position
        self.arrow.grid_remove()

        # Place the label at the new position
        self.arrow.grid(row=row_num, column=0)
        
        


class HorizontalIndicator(customtkinter.CTkFrame):
    def __init__(self, *args , left, middle, right, **kwargs):
        super().__init__(*args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.configure(fg_color = "transparent")

        self.left_title = left
        self.middle_title = middle
        self.right_title = right

        #

        # Farbe = Alles Grau
        ## fg_color="#343434", progress_color="#BFBFBF"
        
        #

        self.progressbar = customtkinter.CTkProgressBar(self, width=250, height=20, corner_radius=10, orientation="horizontal",fg_color="#343434", progress_color="#BFBFBF" )
        self.progressbar.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady=(10,0))

        self.left_title = customtkinter.CTkLabel(self, text=self.left_title)
        self.left_title.grid(row = 1, column = 0, padx = 5, sticky = "w")

        self.middle_title = customtkinter.CTkLabel(self, text=self.middle_title)
        self.middle_title.grid(row = 1, column = 1, padx = 5)

        self.right_title = customtkinter.CTkLabel(self, text=self.right_title)
        self.right_title.grid(row = 1, column = 2, padx = 5, sticky = "e")



## Bewertung der einzelnen Emotionen, -1 ist sad, 1 ist happy und 0 ist neutral


emoji_dict = {

    "Anger" : "-1" , 
    "Boredom" : "0" , 
    "Disgust" : "-1" , 
    "Fear ="  : "-1" , 
    "Happiness" : "1" , 
    "Neutral" : "0" , 
    "Sadness" : "-1" , 
}



class EmotionwithEmoji(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(1, weight=1)
        
        
        self.emotion_text = ""
        self.image_path = "openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/happy.png"

        self.emotion_label = customtkinter.CTkLabel(self, text=self.emotion_text, font=customtkinter.CTkFont(size = 20))
        self.emotion_label.grid(row = 0, column = 1, columnspan = 3, padx = 10, sticky = "e")

        self.image = customtkinter.CTkImage(light_image=Image.open(self.image_path), size=(50,50))
        
        self.emoji = customtkinter.CTkLabel(self, image=self.image, text = "", fg_color="transparent")
        self.emoji.grid(row = 0, column = 0, sticky = "w")
                
        

# TODO: Implementation mit TestDataExtractor, von da wird aktuell stärkste Emo als String gezogen
# Dazu diese Methode in Main mit Daten aus Extractor aufrufen

    def set(self, emotion:str):
        
        self.emotion_text = emotion
        
        match emoji_dict.get(self.emotion_text, "Word not found"):
            case "1":
                self.image_path = "openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/happy.png"
                
                print(self.emotion_text)
            case "0": 
                self.image_path =  "openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/neutral.png"
                print(self.emotion_text)

            case "-1": 
                self.image_path = "openEAR-0.1.0 Kopie/GUI/CustomTkinter/PNG Files/sad.png"
                print(self.emotion_text)
            
            case _: 
                print("Fehler bei der Emoji-Zuordnung")

        self.image.configure(light_image =Image.open(self.image_path))
        
        self.emoji.configure(image=self.image)
        self.emotion_label.configure(text = self.emotion_text)

        


class DualEmotions(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color = "transparent")
        self.columnconfigure(1, weight=1)

        self.left_frame = customtkinter.CTkFrame(self, fg_color= "#343434")
        self.left_frame.grid(row = 0, column = 0)

        self.right_frame = customtkinter.CTkFrame(self, fg_color= "#343434")
        self.right_frame.grid(row = 0, column = 2)

    
        self.emo_label = customtkinter.CTkLabel(self.left_frame, text="", corner_radius=5, fg_color="#343434", font=customtkinter.CTkFont(size = 20))
        self.emo_label.grid(row = 0, column = 0, padx = 30, pady = 5)

        self.abc_label = customtkinter.CTkLabel(self.right_frame, text="", corner_radius=5, fg_color="#343434", font=customtkinter.CTkFont(size = 20))
        self.abc_label.grid(row = 0, column = 0, padx = 30, pady = 5)


    def set(self, emo_emotion:str, abc_emotion:str):

        self.emo_emotion = emo_emotion
        self.abc_emotion = abc_emotion

        self.emo_label.configure(text = self.emo_emotion)
        self.abc_label.configure(text = self.abc_emotion)


        


    