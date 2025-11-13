import tkinter as tk
from tkinter import messagebox
import json
import os

# ---------- File to save tasks ----------
TASKS_FILE = "tasks.json"

# ---------- Load tasks from file ----------
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# ---------- Save tasks to file ----------
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# ---------- Add a new task ----------
def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    task_entry.delete(0, tk.END)
    update_listbox()

# ---------- Delete selected task ----------
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# ---------- Mark as done ----------
def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["done"] = not tasks[selected_index]["done"]
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

# ---------- Update Listbox ----------
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        display_text = f"✔ {task['task']}" if task["done"] else f"• {task['task']}"
        task_listbox.insert(tk.END, display_text)

# ---------- UI Setup ----------
root = tk.Tk()
root.title("📝 Simple To-Do List")
root.geometry("400x400")
root.config(bg="#f5f5f5")

# ---------- Title ----------
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

# ---------- Entry ----------
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=25, font=("Arial", 12))
task_entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(frame, text="Add", width=10, command=add_task, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=1)

# ---------- Listbox ----------
task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12), selectbackground="#90CAF9")
task_listbox.pack(pady=10)

# ---------- Buttons ----------
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

done_button = tk.Button(button_frame, text="Mark Done", width=12, command=mark_done, bg="#2196F3", fg="white")
done_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete", width=12, command=delete_task, bg="#F44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

# ---------- Load and Display ----------
tasks = load_tasks()
update_listbox()

# ---------- Run the app ----------
root.mainloop()
