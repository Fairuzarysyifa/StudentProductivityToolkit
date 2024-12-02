import tkinter as tk
from tkinter import messagebox
import time
import threading

class Timer:
    def __init__(self, root):
        self.timer_window = tk.Toplevel(root)
        self.timer_window.title("Timer")
        self.timer_window.geometry("300x200")
        
        self.label = tk.Label(self.timer_window, text="Set Timer (minutes):")
        self.label.pack()
        
        self.entry = tk.Entry(self.timer_window)
        self.entry.pack()

        self.start_button = tk.Button(self.timer_window, text="Start", command=self.start_timer)
        self.start_button.pack()
        
        self.time_label = tk.Label(self.timer_window, text="", font=("Arial", 20))
        self.time_label.pack()

    def start_timer(self):
        try:
            minutes = int(self.entry.get())
            total_seconds = minutes * 60
            threading.Thread(target=self.countdown, args=(total_seconds,)).start()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def countdown(self, total_seconds):
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            self.time_label.config(text=time_str)
            self.timer_window.update()
            time.sleep(1)
            total_seconds -= 1
        messagebox.showinfo("Timer Finished", "Time's up!")
