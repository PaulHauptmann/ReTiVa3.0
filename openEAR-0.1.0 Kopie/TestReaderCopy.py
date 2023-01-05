import tkinter as tk
import customtkinter
import re
from dataclasses import dataclass#
import openpyxl

#listen Initialisierung
DataTime = [0]
DataArousal = [0]
DataValence = [0]
DataEmodbEmotionAnger = [0]
DataEmodbEmotionBoredom = [0]
DataEmodbEmotionDisgust = [0]
DataEmodbEmotionFear = [0]
DataEmodbEmotionHappiness = [0]
DataEmodbEmotionNeutral = [0]
DataEmodbEmotionSadness = [0]
DataAbcAffectAgressiv = [0]
DataAbcAffectCheerfull = [0]
DataAbcAffectIntoxicated = [0]
DataAbcAffectNervous = [0]
DataAbcAffectNeutral = [0]
DataAbcAffectTired = [0]
DataLoi1 = [0]
DataLoi2 = [0]
DataLoi3 = [0]

FaktorDataTime = 1
FaktorDataArousal = 1
FaktorDataValence = 1
FaktorDataEmodbEmotionAnger = 1
FaktorDataEmodbEmotionBoredom = 1
FaktorDataEmodbEmotionDisgust = 1
FaktorDataEmodbEmotionFear = 1
FaktorDataEmodbEmotionHappiness = 1
FaktorDataEmodbEmotionNeutral = 1
FaktorDataEmodbEmotionSadness = 1
FaktorDataAbcAffectAgressiv = 1
FaktorDataAbcAffectCheerfull = 1
FaktorDataAbcAffectIntoxicated = 1
FaktorDataAbcAffectNervous = 1
FaktorDataAbcAffectNeutral = 1
FaktorDataAbcAffectTired = 1
FaktorDataLoi1 = 1
FaktorDataLoi2 = 1
FaktorDataLoi3 = 1

@dataclass
class EMO:
    time: float
    Arousal: float
    Valence: float
    emodbEmotionAnger: float	
    emodbEmotionBoredom: float	
    emodbEmotionDisgust: float	
    emodbEmotionFear: float	
    emodbEmotionHappiness: float	
    emodbEmotionNeutral: float	
    emodbEmotionSadness: float	
    abcAffectAgressiv: float	
    abcAffectCheerfull: float	
    abcAffectIntoxicated: float	
    abcAffectNervous: float	
    abcAffectNeutral: float	
    abcAffectTired: float	
    Loi1: float	
    Loi2: float	
    Loi3: float


def update_text_window(text_window, file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        contents = str(file.readlines()[-25:])
        errorcatch= re.findall(r"\d{2}\.\d{2}\.\d{4}", contents)
        
        if len(errorcatch) != 0:
            # text_window.insert('1.0', "HAHAHAHAH")
            return

        result=re.findall(r"\d+\.\d+", contents)

        # 2 4 12 19
        result.pop(19)
        result.pop(12)
        result.pop(4)
        result.pop(2)

        emo = EMO(*result)

        
        


        
        #schreibt pro tick in die jeweilige Liste hinten dran neuesten wert, wenn der wert sich ändert
        if DataTime[-1] != emo.time:
            DataTime.append(emo.time)
            DataArousal.append(emo.Arousal)
            DataValence.append(emo.Valence)
            DataEmodbEmotionAnger.append(emo.emodbEmotionAnger)
            DataEmodbEmotionBoredom.append(emo.emodbEmotionBoredom)
            DataEmodbEmotionDisgust.append(emo.emodbEmotionDisgust)
            DataEmodbEmotionFear.append(emo.emodbEmotionFear)
            DataEmodbEmotionHappiness.append(emo.emodbEmotionHappiness)
            DataEmodbEmotionNeutral.append(emo.emodbEmotionNeutral)
            DataEmodbEmotionSadness.append(emo.emodbEmotionSadness)
            DataAbcAffectAgressiv.append(emo.abcAffectAgressiv)
            DataAbcAffectCheerfull.append(emo.abcAffectCheerfull)
            DataAbcAffectIntoxicated.append(emo.abcAffectIntoxicated)
            DataAbcAffectNervous.append(emo.abcAffectNervous)
            DataAbcAffectNeutral.append(emo.abcAffectNeutral)
            DataAbcAffectTired.append(emo.abcAffectTired)
            DataLoi1.append(emo.Loi1)
            DataLoi2.append(emo.Loi2)
            DataLoi3.append(emo.Loi3)



            #Ausgabe der Listen
            print('Time:                  ', DataTime)
            print('Arousal:               ', DataArousal)
            print('Valence:               ', DataValence)
            print('EmodbEmotionAnger:     ', DataEmodbEmotionAnger)
            print('EmodbEmotionBoredom:   ', DataEmodbEmotionBoredom)
            print('EmodbEmotionDisgust:   ', DataEmodbEmotionDisgust)
            print('EmodbEmotionFear:      ', DataEmodbEmotionFear)
            print('EmodbEmotionHappiness: ', DataEmodbEmotionHappiness)
            print('EmodbEmotionNeutral:   ', DataEmodbEmotionNeutral)
            print('EmodbEmotionSadness:   ', DataEmodbEmotionSadness)
            print('AbcAffectAgressiv:     ', DataAbcAffectAgressiv)
            print('AbcAffectCheerfull:    ', DataAbcAffectCheerfull)
            print('AbcAffectIntoxicated:  ', DataAbcAffectIntoxicated)
            print('AbcAffectNervous:      ', DataAbcAffectNervous)
            print('AbcAffectNeutral:      ', DataAbcAffectNeutral)
            print('AbcAffectTired:        ', DataAbcAffectTired)
            print('Loi1:                  ', DataLoi1)
            print('Loi2:                  ', DataLoi2)
            print('Loi3:                  ', DataLoi3)

            
            
        
        
        # Excel stuff
        #filename = "/Users/paul/Desktop/openEAR-0.1.0/output2.xlsx"
        #wb = openpyxl.load_workbook(filename)
        #ws = wb.worksheets[0]
        #ws.append(emo.abcAffectAgressiv)

        #wb.save(filename)
                

        

        # Update the text widget with the contents of the file
        text_window.config(state='normal')
        text_window.delete('1.0', tk.END)
        text_window.insert('1.0', result)
        text_window.config(state='disabled')
        text_window.see(tk.END)











# Create the tkinter window
window = tk.Tk()
window.title("Live Text Mirror")

# Create a text widget to display the contents of the file
text_window = tk.Text(window)
text_window.pack()

# Set the file path
file_path = '/Users/paul/Desktop/openEAR-0.1.0/smile.log'

# Update the text widget with the initial contents of the file
update_text_window(text_window, file_path)

# Create a function that will be called every 1 second to update the text widget
def update_text_window_periodically():
    update_text_window(text_window, file_path)
    window.after(10, update_text_window_periodically)

# Call the function to start the updating
update_text_window_periodically()

# Run the tkinter event loop
window.mainloop()