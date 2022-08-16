from tkinter import *
from webbrowser import get
window=Tk()
window.title("GUI")
label1=Label(window,text="Hello world!").pack()
label2=Label(window,text="This is the second line.").pack()

enter=Entry(window,width=50,bg="Black",fg="Red",borderwidth=5,border=10)
enter.pack()
enter.insert(1,"Enter Your name")
def Click():
    label3=Label(window,text="Hello "+enter.get()).pack()
#global label3
myButton=Button(window,text="Print",padx=50,pady=10,command=Click,fg="Red",bg="Black").pack()

window.mainloop()