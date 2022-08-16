from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Second lecture of Tkinter")

root.iconbitmap('FINAL_LOGO.ico')

Img1=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy1.jpeg"))
Img2=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy2.jpeg"))
Img3=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy3.jpeg"))
Img4=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy4.jpeg"))
Img5=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy5.jpeg"))
Img6=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy6.jpeg"))
Img7=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy7.jpeg"))
Img8=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy8.jpeg"))
Img9=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy9.jpeg"))
Img10=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy10.jpeg"))
Img11=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy11.jpeg"))
Img12=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy12.jpeg"))
Img13=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy13.jpeg"))
Img14=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy14.jpeg"))
Img15=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy15.jpeg"))
Img16=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy16.jpeg"))
Img17=ImageTk.PhotoImage(Image.open("C:\Programming\Python Programming\Practice\Dimpy Pics\Dimpy17.jpeg"))


image_list=[Img1,Img2,Img3,Img4,Img5,Img6,Img7,Img8,Img9,Img10,Img11,Img12,Img13,Img14,Img15,Img16,Img17]
label=Label(image=Img1)
label.grid(row=0,column=0,columnspan=3)

def next(n):
    global label,button_next,button_back
    label.grid_forget()
    label=Label(image=image_list[n-1])
    label.grid(row=0,column=0,columnspan=3)
    #button_next=Button(root,text=">>",command=lambda:next(n+1))
    if n==len(image_list):
        button_next=Button(root,text=">>",state=DISABLED)
        button_next.grid(row=1,column=2)
    else:
        button_next=Button(root,text=">>",command=lambda:next(n+1))   
    
    button_next.grid(row=1,column=2)
def back(n):
    global label,button_next,button_back
    label.grid_forget()
    label=Label(image=image_list[n-1])
    label.grid(row=0,column=0,columnspan=3)
    if n<2:
        button_back=Button(root,text="<<",command=lambda:back(n-1),state=DISABLED)
        button_back.grid(row=1,column=0)
    else:
        button_back=Button(root,text="<<",command=lambda:back(n-1))
        button_back.grid(row=1,column=0)

button_back=Button(root,text="<<",command=lambda:back(2))
button_next=Button(root,text=">>",command=lambda:next(2))
button_quit=Button(root,text="Exit Program",command=root.quit)

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_next.grid(row=1,column=2)

root.mainloop()