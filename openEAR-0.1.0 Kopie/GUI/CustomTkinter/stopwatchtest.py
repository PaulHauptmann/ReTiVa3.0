import tkinter as tk
import time

class Stopwatch(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Stopwatch")
        self.time = 0.0
        self.running = False
        self.time_string = tk.StringVar()
        self.time_string.set("0:00:00")
        self.label = tk.Label(self, textvariable=self.time_string)
        self.label.pack()
        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.pack()
        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack()

    def start(self):
        self.running = True
        self.start_time = time.time()
        self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0.0
        self.time_string.set("0:00:00")

    def update_time(self):
        if self.running:
            self.time = time.time() - self.start_time
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.time_string.set("%d:%02d:%02d" % (hours, minutes, seconds))
            self.label.after(10, self.update_time)

stopwatch = Stopwatch()
stopwatch.mainloop()
