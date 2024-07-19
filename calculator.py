from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry('800x200')

def calculate_sum():
    num1=float(entry1.get())
    num2=float(entry2.get())
    total=num1+num2
    result.config(text=f"Sum: {total}")

def calculate_sub():
    num1=float(entry1.get())
    num2=float(entry2.get())
    total=num1-num2
    result.config(text=f"Subtraction: {total}")

def calculate_mul():
    num1=float(entry1.get())
    num2=float(entry2.get())
    total=num1*num2
    result.config(text=f"Multiplication: {total}")

def calculate_div():
    num1=float(entry1.get())
    num2=float(entry2.get())
    total=num1/num2
    result.config(text=f"Division: {total}")

label1=Label(window, text="Number1:")
label1.grid(row=0,column=0,padx=10,pady=5)

entry1=Entry(window)
entry1.grid(row=0,column=1,padx=10,pady=5)

label2=Label(window, text="Number2:")
label2.grid(row=1,column=0,padx=10,pady=5)

entry2=Entry(window)
entry2.grid(row=1,column=1,padx=10,pady=5)

submit_button = Button(window,text="Sum", command=calculate_sum)
submit_button.grid(row=3,column=0,columnspan=2,pady=10)

submit_button = Button(window,text="Subtraction", command=calculate_sub)
submit_button.grid(row=3,column=1,columnspan=2,pady=10)

submit_button = Button(window,text="Multiplication", command=calculate_mul)
submit_button.grid(row=3,column=2,columnspan=2,pady=10)

submit_button = Button(window,text="Division", command=calculate_div)
submit_button.grid(row=3,column=4,columnspan=2,pady=10)

result=Label(window,text="Result")
result.grid(row=4,column=1,columnspan=2,pady=10)

window.mainloop()