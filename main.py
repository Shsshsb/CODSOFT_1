import tkinter as tk
from tkinter import font, messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to edit a selected task
def edit_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        edited_task = task_entry.get()
        if edited_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, edited_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task to edit.")

# Function to remove a selected task
def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

# Create the main window and edges
root = tk.Tk()
root.title("To-Do List")

# Create a custom font
custom_font = font.Font(family="Helvetica", size=12)

# Create three frames with Indian flag's tricolors
saffron_frame = tk.Frame(root, bg="#FF9933", height=50)
white_frame = tk.Frame(root, bg="white", height=50)
green_frame = tk.Frame(root, bg="#138808", height=50)

saffron_frame.pack(fill=tk.X)
white_frame.pack(fill=tk.X)
green_frame.pack(fill=tk.X)

# Create a Label widget on the white frame to display the text "Shreyash"
shreyash_label = tk.Label(white_frame, text="Shreyash", font=custom_font, bg="white")
shreyash_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a task entry widget
task_entry = tk.Entry(root, font=custom_font, width=40)
task_entry.pack(pady=10)

# Create buttons for adding, editing, and removing tasks with custom styles
add_button = tk.Button(root, text="Add Task", font=custom_font, command=add_task, padx=10)
edit_button = tk.Button(root, text="Edit Task", font=custom_font, command=edit_task, padx=10)
remove_button = tk.Button(root, text="Remove Task", font=custom_font, command=remove_task, padx=10)
add_button.pack()
edit_button.pack()
remove_button.pack()

# Create a listbox to display tasks with custom styles
task_list = tk.Listbox(root, font=custom_font, width=40, selectbackground="#a6a6a6")
task_list.pack()

#
root.mainloop()
