import tkinter as tk

class ToDo:
    def __init__(self, root):
        self.todo_window = tk.Toplevel(root)
        self.todo_window.title("To-Do List")
        self.todo_window.geometry("300x400")
        
        self.task_list = tk.Listbox(self.todo_window, selectmode='multiple')
        self.task_list.pack(expand=True, fill='both')

        add_button = tk.Button(self.todo_window, text="Add Task", command=self.add_task)
        add_button.pack()

        delete_button = tk.Button(self.todo_window, text="Delete Selected", command=self.delete_task)
        delete_button.pack()

    def add_task(self):
        task = tk.simpledialog.askstring("New Task", "Enter task:")
        if task:
            self.task_list.insert(tk.END, task)

    def delete_task(self):
        selected = self.task_list.curselection()
        for idx in reversed(selected):
            self.task_list.delete(idx)
