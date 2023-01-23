#
# Use Canvas to create a basic gauge
#
from tkinter import *
import random
 
def update_gauge():
    newvalue = random.randint(low_r,hi_r)
    cnvs.itemconfig(id_text,text = str(newvalue) + " %")
    # Rescale value to angle range (0%=120deg, 100%=30 deg)
    angle = 120 * (hi_r - newvalue)/(hi_r - low_r) + 30
    cnvs.itemconfig(id_needle,start = angle)
    root.after(3000, update_gauge)
 
     
# Create Canvas objects    
 
canvas_width = 400
canvas_height =300
 
root = Tk()
 
cnvs = Canvas(root, width=canvas_width, height=canvas_height)
cnvs.grid(row=2, column=1, padx = 30, pady = 30)
 
coord = 10, 10, 300, 300 #define the size of the gauge
low_r = 0 # chart low range
hi_r = 100 # chart hi range
 

# add hi/low bands
cnvs.create_arc(coord, start=330, extent=240, outline="red", style= "arc", width=20)
cnvs.create_arc(coord, start=330, extent=160, outline="yellow", style= "arc", width=20)
cnvs.create_arc(coord, start=330, extent=80, outline="green", style= "arc", width=20)

# add needle/value pointer
id_needle = cnvs.create_arc(coord, start= 119, extent=1, width=7)
 
# Add some labels
#cnvs.create_text(180,15,font="Times 20 italic bold", text="Humidity")
#cnvs.create_text(25,140,font="Times 12 bold", text=low_r)
#cnvs.create_text(330,140,font="Times 12 bold", text=hi_r)
id_text = cnvs.create_text(170,210,font="Times 15 bold")
 
root.after(3000, update_gauge)
 
root.mainloop()