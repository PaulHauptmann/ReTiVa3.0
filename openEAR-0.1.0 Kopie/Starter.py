import subprocess
from tkinter import *

def run_smilextract():
    subprocess.run(["SMILExtract", "-C", "config/emobase_live4.conf"], cwd="/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/")

root = Tk()
button = Button(root, text="Run SMILExtract", command=run_smilextract)
button.pack()
root.mainloop()
