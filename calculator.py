import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.calc_window = tk.Toplevel(root)
        self.calc_window.title("Calculator")
        self.calc_window.geometry("300x400")
        
        self.entry = tk.Entry(self.calc_window, width=16, font=("Arial", 24), bd=5, insertwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]

        row, col = 1, 0
        for button in buttons:
            tk.Button(self.calc_window, text=button, padx=20, pady=20, font=("Arial", 18),
                      command=lambda b=button: self.click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, button):
        if button == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif button == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, button)
