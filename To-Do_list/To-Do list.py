import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")
root.configure(bg="White Smoke")
root.geometry("550x400")
root.resizable(0,0)


def add_task():

    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
        save_tasks()
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task. ")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
        save_tasks()
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def update_task():
    try:
        task_index1 = listbox_tasks.curselection()[0]

        task = entry_task.get()
        if task != "":
            delete_task()
            listbox_tasks.insert(task_index1, task)
            entry_task.delete(0, tkinter.END)
            save_tasks()
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task to update. ")


    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)

        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="warning!", message="Cannot find task.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def remove() :
    listbox_tasks.delete(0, tkinter.END)
    save_tasks()

tkinter.Label(root, text="To-Do Tasks", font=('Times New Roman', 20), bg="White Smoke").place(x=200, y=20)


frame_tasks = tkinter.Frame(root)
frame_tasks.place(x=15,y=70)


listbox_tasks = tkinter.Listbox(frame_tasks, height=6, width=45, font=("Times New Roman", 16), bg='White', borderwidth=5)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks, borderwidth=5)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=42, font=("arial", 16), borderwidth=5)
entry_task.place(x=15, y=230)

button_add_task = tkinter.Button(root, text="Add task",width=51,font=("arial", 12, "bold"), bd=1, fg="#fff", bg="#3697f5", command=add_task)
button_add_task.place(x=15, y=265)

button_delete_task = tkinter.Button(root, text="Delete task", width=51, font=("arial", 12, "bold"),bd=1, fg="#fff", bg="#ff0000", command=delete_task)
button_delete_task.place(x=15,y=298)

button_update_task = tkinter.Button(root, text="Update task",width=51,font=("arial", 12, "bold"), bd=1, fg="#fff", bg="aqua", command=update_task)
button_update_task.place(x=15,y=331)

#button_load_tasks = tkinter.Button(root, text="View tasks", width=50, font=("arial", 12, "bold"),bd=1, fg="#fff", bg="#ffff00", command=load_tasks)
#button_load_tasks.pack()

#button_save_tasks = tkinter.Button(root, text="Submit Tasks", width=40, font=("arial", 12, "bold"), bd=1, fg="#fff", bg="#00ffff", command=save_tasks)
#button_save_tasks.pack()

button_delete_task = tkinter.Button(root, text="Remove all tasks",width=51,font=("arial", 12, "bold"), bd=1, fg="#fff", bg="lime", command=remove)
button_delete_task.place(x=15,y=364)

load_tasks()
root.mainloop()


