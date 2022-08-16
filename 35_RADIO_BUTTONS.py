from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Radio Buttons.")
r=IntVar()
r.set("2")
def click(value):
    mylabel=Label(root,text=value)
    mylabel.pack()
    
    
Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:click(r.get())).pack()
Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:click(r.get())).pack()
mylabel=Label(root,text=r.get())
mylabel.pack()


root.mainloop()