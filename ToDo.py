import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass

def toggle_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(selected_task_index, bg="lightgrey")
    except IndexError:
        pass

root = tk.Tk()
root.title("ToDo List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Selected Task", width=48, command=delete_task)
button_delete_task.pack()

button_toggle_task = tk.Button(root, text="Toggle Completed Task", width=48, command=toggle_task)
button_toggle_task.pack()

root.mainloop()

