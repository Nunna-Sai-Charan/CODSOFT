
from tkinter import *

cal = Tk()
cal.title("Nunna's Calculator")
cal.geometry("570x600+100+200")
cal.resizable(0,0)
cal.configure(bg="#17161b")

equation=''

def display(value) :
    global equation
    equation += value
    label_result.config(text=equation)

def clear() :
    global equation
    equation=''
    label_result.config(text=equation)

def calculate() :
    global equation
    result=""
    if equation != "" :
        try :
            result = eval(equation)
        except :
            result='error'
            equation=''
    label_result.config(text=result)


label_result=Label(cal, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

Button(cal, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#ff0000", command=lambda: clear()).place(x=10, y=100)
Button(cal, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("/")).place(x=150, y=100)
Button(cal, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("%")).place(x=290, y=100)
Button(cal, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("*")).place(x=430, y=100)

Button(cal, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("7")).place(x=10, y=200)
Button(cal, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("8")).place(x=150, y=200)
Button(cal, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("9")).place(x=290, y=200)
Button(cal, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("-")).place(x=430, y=200)

Button(cal, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("4")).place(x=10, y=300)
Button(cal, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("5")).place(x=150, y=300)
Button(cal, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("6")).place(x=290, y=300)
Button(cal, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("+")).place(x=430, y=300)

Button(cal, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("1")).place(x=10, y=400)
Button(cal, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("2")).place(x=150, y=400)
Button(cal, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("3")).place(x=290, y=400)
Button(cal, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display(".")).place(x=430, y=400)

Button(cal, text="(", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("(")).place(x=10, y=500)
Button(cal, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display("0")).place(x=150, y=500)
Button(cal, text=")", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: display(")")).place(x=290, y=500)
Button(cal, text="=", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3D85C6", command=lambda: calculate()).place(x=430, y=500)

cal.mainloop()