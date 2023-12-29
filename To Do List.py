import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []  # List to store tasks

        # Styling
        self.root.geometry("500x500")
        self.root.configure(bg="#ffffb3")

        # Create Frames
        self.frame_list = tk.Frame(root, bg="#c6ffb3", padx=20, pady=10)
        self.frame_list.pack(pady=20, fill=tk.BOTH, expand=True)

        self.frame_buttons = tk.Frame(root, bg="#ffb3c6")
        self.frame_buttons.pack()

        # Listbox to display tasks
        self.listbox = tk.Listbox(self.frame_list, width=40, height=10, font=("Arial", 12))
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.show_task_details)

        # Entry for adding/updating tasks
        self.entry = tk.Entry(root, width=30, bg="#c6ffb3",font=("Arial Bold", 12))
        self.entry.pack()

        # Add Task button
        self.add_task_btn = tk.Button(self.frame_buttons, text="Add Task", bg="#90d5d5", width=12, command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT, padx=5)

        # Update Task button
        self.update_task_btn = tk.Button(self.frame_buttons, text="Update Task",bg="#90d5d5", width=12, command=self.update_task)
        self.update_task_btn.pack(side=tk.LEFT, padx=5)

        # Delete Task button
        self.delete_task_btn = tk.Button(self.frame_buttons, text="Delete Task", bg="#90d5d5", width=12, command=self.delete_task)
        self.delete_task_btn.pack(side=tk.LEFT, padx=5)

        # Mark as Completed button
        self.mark_completed_btn = tk.Button(self.frame_buttons, text="Mark as Completed", bg="#90d5d5", width=15, command=self.mark_completed)
        self.mark_completed_btn.pack(side=tk.LEFT, padx=5)

        # Quit Application button
        self.quit_btn = tk.Button(self.frame_buttons, text="Quit", bg="#90d5d5", width=12, command=self.quit_application)
        self.quit_btn.pack(side=tk.LEFT, padx=5)

        self.list_tasks()  # Display existing tasks

    def list_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            self.listbox.insert(tk.END, f"{task['task']} - {status}")

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.list_tasks()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            updated_task = self.entry.get()
            if updated_task:
                self.tasks[selected_task_index]["task"] = updated_task
                self.list_tasks()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.list_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.list_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def show_task_details(self, event=None):
        try:
            selected_task_index = self.listbox.curselection()[0]
            selected_task = self.tasks[selected_task_index]["task"]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected_task)
        except IndexError:
            pass

    def quit_application(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
