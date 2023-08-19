import tkinter
from tkinter import *
import tkinter.messagebox
import random
import string
import pyperclip
from pyperclip import *


root=Tk()
root.title("Random Password Generator")
root.geometry("500x410")
root.resizable(0,0)
root.configure(bg="White Smoke")

def gen_password() :
    entry_task3.delete(0, END)
    try :
     length=int(entry_task2.get())
     name=str(entry_task1.get())
     if length >0 and name!='':

        password = ''
        for x in range(length):
            password += chr(random.randint(33,126))
        entry_task3.insert(0, password)

    except :
        tkinter.messagebox.showwarning(title="Warning!", message="Username or Length of Password is missing.")

def accept() :
    return exit()

def copy() :
    temp=entry_task3.get()
    pyperclip.copy(temp)
    tkinter.messagebox.showinfo(title='info', message="Password Copied successfully")

def reset() :
    if entry_task1.get()!='' and entry_task2.get()!='' :
        entry_task1.delete(0, END)
        entry_task2.delete(0, END)
        entry_task3.delete(0, END)
    else :
        tkinter.messagebox.showwarning(title="Warning!", message="Username or Length of Password is missing.")


frame_tasks = tkinter.Frame(root)
frame_tasks.place(x=25, y=70)
#frame_tasks.pack(padx=0, pady=0)

tkinter.Label(root, text="Password Generator", font=('Times New Roman', 20), bg="White Smoke").place(x=130, y=20)
tkinter.Label(frame_tasks, text="Enter User name      : ", font=('Times New Roman', 15), bg="White Smoke").grid(row=0)
tkinter.Label(frame_tasks, text="Length of password  : ", font=('Times New Roman', 15), bg="White Smoke").grid(row=1)
tkinter.Label(frame_tasks, text="Password Generated : ", font=('Times New Roman', 15), bg="White Smoke").grid(row=2)


entry_task1 = tkinter.Entry(frame_tasks, width=20, font=("arial", 16), bg="White", borderwidth=5)
entry_task2 = tkinter.Entry(frame_tasks, font=("arial", 16), bg="White", borderwidth=5)
entry_task3 = tkinter.Entry(frame_tasks, font=("arial", 16), bg="White", borderwidth=5)
#label_result=Label(frame_tasks, text="", width=20, font=("arial", 16), bg='white', borderwidth=5, highlightthickness=5, highlightcolor='Black')

entry_task1.grid(row=0, column=1)
entry_task2.grid(row=1, column=1)
entry_task3.grid(row=2, column=1)
#label_result.grid(row=2, column=1)

Button(root, text="Generate Password", bg="Yellow", command=gen_password, font=('Times New Roman', 17)).place(x=133, y=200)
Button(root, text="Accept", bg= 'Green', command=accept, font=('Times New Roman', 17)).place(x=179, y=300)
Button(root, text="Reset", bg= 'Orange', command=reset, font=('Times New Roman', 17)).place(x=182, y=350)
Button(root, text="Copy To Clipboard", bg= 'aqua', command=copy, font=('Times New Roman', 17)).place(x=133, y=250)

root.mainloop()