import time
import tkinter as tk

class Watch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Watch")
        self.clock_label = tk.Label(self.root, font=('times', 20, 'bold'), bg='white')
        self.clock_label.pack(fill='both', expand=1)
        self.stopwatch_label = tk.Label(self.root, font=('times', 20, 'bold'), bg='white')
        self.stopwatch_label.pack(fill='both', expand=1)
        self.stopwatch_running = False
        self.stopwatch_start_time = 0
        self.stopwatch_button = tk.Button(self.root, text="Start", command=self.start_stopwatch)
        self.stopwatch_button.pack()
        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_start_time = time.time()
            self.stopwatch_running = True
            self.stopwatch_button.config(text="Stop")
            self.update_stopwatch()
        else:
            self.stopwatch_running = False
            self.stopwatch_button.config(text="Start")

    def update_stopwatch(self):
        if self.stopwatch_running:
            elapsed_time = time.time() - self.stopwatch_start_time
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            stopwatch_time = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
            self.stopwatch_label.config(text=stopwatch_time)
            self.root.after(1000, self.update_stopwatch)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    watch = Watch()
    watch.run()
