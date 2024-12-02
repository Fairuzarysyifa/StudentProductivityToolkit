import tkinter as tk
from tkinter import Menu
from timer import Timer
from notes import Notes
from todo import ToDo
from calculator import Calculator

# Main application
class ProductivityToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Productivity Toolkit")
        self.root.geometry("600x400")
        
        # Menu bar
        menu = Menu(self.root)
        self.root.config(menu=menu)

        # Adding features to the menu
        menu.add_command(label="Timer", command=self.open_timer)
        menu.add_command(label="Notes", command=self.open_notes)
        menu.add_command(label="To-Do List", command=self.open_todo)
        menu.add_command(label="Calculator", command=self.open_calculator)

    def open_timer(self):
        Timer(self.root)

    def open_notes(self):
        Notes(self.root)

    def open_todo(self):
        ToDo(self.root)

    def open_calculator(self):
        Calculator(self.root)

# Run application
if __name__ == "__main__":
    root = tk.Tk()
    app = ProductivityToolkit(root)
    root.mainloop()
