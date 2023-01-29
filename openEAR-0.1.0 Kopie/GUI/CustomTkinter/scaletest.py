import tkinter as tk

class ColorScale(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)

        self.gradient = ["#0000ff", "#00ff00", "#ffff00", "#ff0000"]

        self.arrow = self.create_polygon([0, 0, 5, -10, -5, -10], fill="black")
        self.tag_lower("arrow")

        self.bind("<Configure>", self.draw_gradient)
        self.bind("<Button-1>", self.move_arrow)

    def draw_gradient(self, event=None):
        self.delete("gradient")

        height = self.winfo_height()
        width = self.winfo_width()

        step = height / len(self.gradient)

        for i, color in enumerate(self.gradient):
            self.create_rectangle(0, i*step, width, (i+1)*step, fill=color, tags="gradient")

    def move_arrow(self, event):
        self.coords(self.arrow, [event.x, event.y, event.x+5, event.y-10, event.x-5, event.y-10])

if __name__ == "__main__":
    root = tk.Tk()
    scale = ColorScale(root, bg="white", height=300, width=50)
    scale.pack()
    root.mainloop()
