from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Image Viewer.")

img1=ImageTk.PhotoImage(Image.open("C:/Programming/Python_Programming/Practice/media/Dimpy1.jpeg"))
img2=ImageTk.PhotoImage(Image.open("C:/Programming/Python_Programming/Practice/media/Dimpy2.jpeg"))
img3=ImageTk.PhotoImage(Image.open("C:/Programming/Python_Programming/Practice/media/Dimpy3.jpeg"))
img4=ImageTk.PhotoImage(Image.open("C:/Programming/Python_Programming/Practice/media/Dimpy4.jpeg"))
img5=ImageTk.PhotoImage(Image.open("C:/Programming/Python_Programming/Practice/media/Dimpy5.jpeg"))
img6=ImageTk.PhotoImage(Image.open("C:/Programming/Python_Programming/Practice/media/Dimpy6.jpeg"))
img7=ImageTk.PhotoImage(Image.open("C:/Programming/Python_Programming/Practice/media/Dimpy7.jpeg"))

img_list=[img1,img2,img3,img4,img5,img6,img7]
status=Label(root,text="Image 1 of "+str(len(img_list)),bd=1,relief=SUNKEN)
label1=Label(image=img1)
label1.grid(row=0,column=0,columnspan=3)

def next(img_num):
    global label1
    global button_back
    global button_forward
    label1.grid_forget()
    label1=Label(image=img_list[img_num-1])
    label1.grid(row=0,column=0,columnspan=3)
    button_forward=Button(root,text=">>",command=lambda:next(img_num+1))
    button_back=Button(root,text="<<",command=lambda:back(img_num-1))
    if img_num==7:
        button_forward=Button(root,text='>>',state=DISABLED)
    status=Label(root,text="Image "+str(img_num)+" of "+str(len(img_list)),bd=1,relief=SUNKEN)
    status.grid(row=2,column=2,columnspan=3,sticky=W+E)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    status.grid(row=2,column=2,columnspan=3,sticky=W+E)
    
                
def back(img_num):
    global label1
    global button_back
    global button_forward
    label1.grid_forget()
    label1=Label(image=img_list[img_num-1])
    label1.grid(row=0,column=0,columnspan=3)
    button_forward=Button(root,text=">>",command=lambda:next(img_num+1))
    button_back=Button(root,text="<<",command=lambda:back(img_num-1))
    if img_num==1:
        button_back=Button(root,text="<<",state=DISABLED)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    status=Label(root,text="Image "+str(img_num)+" of "+str(len(img_list)),bd=1,relief=SUNKEN)
    status.grid(row=2,column=2,columnspan=3,sticky=W+E)


button_back=Button(root,text="<<",command=back,state=DISABLED)
button_forward=Button(root,text=">>",command=lambda:next(2))
button_quit=Button(root,text="Quit",command=root.quit)
button_quit.grid(row=1,column=1)
button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2,pady=5)
status.grid(row=2,column=2,columnspan=3,sticky=W+E)
root.mainloop()