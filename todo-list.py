import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.root.config(bg="#f5f5f5")

        self.tasks = []

        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f5f5f5")
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        self.add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), bg="#4caf50", fg="white",
                                    command=self.add_task)
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="#a0a0a0", activestyle="none")
        self.listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.delete_button = tk.Button(root, text="Delete Selected Task", font=("Helvetica", 12), bg="#f44336", fg="white",
                                       command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", font=("Helvetica", 12), bg="#2196f3", fg="white",
                                     command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            task_index = selected[0]
            self.tasks.pop(task_index)
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
