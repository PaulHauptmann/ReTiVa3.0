import tkinter as tk
import re
from dataclasses import dataclass#
import openpyxl

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
        filename = "/Users/paul/Desktop/openEAR-0.1.0/output2.xlsx"
        wb = openpyxl.load_workbook(filename)
        ws = wb.worksheets[0]
        ws["Z1"] = emo.abcAffectAgressiv

        wb.save(filename)
                

        

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