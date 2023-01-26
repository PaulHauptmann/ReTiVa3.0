import subprocess
from tkinter import *

def run_smilextract():
    global process
    process = subprocess.Popen(["SMILExtract", "-C", "config/emobase_live4.conf"], cwd="/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/")

def stop_smilextract():
    process.kill()

root = Tk()
start_button = Button(root, text="Start SMILExtract", command=run_smilextract)
stop_button = Button(root, text="Stop SMILExtract", command=stop_smilextract)
start_button.pack()
stop_button.pack()
root.mainloop()
