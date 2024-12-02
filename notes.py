import tkinter as tk
from tkinter import filedialog

class Notes:
    def __init__(self, root):
        self.notes_window = tk.Toplevel(root)
        self.notes_window.title("Notes")
        self.notes_window.geometry("400x300")
        
        self.text_area = tk.Text(self.notes_window, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        save_button = tk.Button(self.notes_window, text="Save", command=self.save_note)
        save_button.pack(side='left')

        load_button = tk.Button(self.notes_window, text="Load", command=self.load_note)
        load_button.pack(side='right')

    def save_note(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))

    def load_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, file.read())
