from tkinter import *
from math import *
root=Tk()
root.title("Calculator")
e=Entry(root,border=5,width=65)
e.place(height=100)
e.grid(row=0,column=0,columnspan=4)

#button functions
def click(n):
    a=e.get()
    e.delete(0,END)
    e.insert(0,str(a)+str(n))  

def addition():
    first_number=e.get()
    global fnum,OP
    OP="Addition"
    fnum=int(first_number)
    e.delete(0,END)
    
def substraction():
    first_number=e.get()
    global fnum,OP
    OP="Substraction"
    e.delete(0,END)
    fnum=int(first_number)

def multiplication():
    first_number=e.get()
    global fnum,OP
    OP="Multiplication"
    e.delete(0,END)
    fnum=int(first_number)

def division():
    first_number=e.get()
    global fnum,OP
    OP="division"
    e.delete(0,END)
    fnum=int(first_number)

def exponent():
    first_number=e.get()
    global fnum,OP
    OP="exponent"
    e.delete(0,END)
    fnum=int(first_number)

def modulus():
    first_number=e.get()
    global fnum,OP
    OP="modulus"
    e.delete(0,END)
    fnum=int(first_number)

def natural_log():
    first_number=e.get()
    global fnum,OP
    OP="Natural Log"
    e.delete(0,END)
    fnum=int(first_number)

def squareroot():
    first_number=e.get()
    global fnum,OP
    OP="Square root"
    e.delete(0,END)
    fnum=int(first_number)                

def all_clear():
    e.delete(0,END)

def equal():
    second_number=e.get()
    global fnum,snum,OP
    e.delete(0,END)
    snum=int(second_number)

    if OP=="Addition":
        e.insert(0,fnum+snum)

    elif OP=="Substraction":
        e.insert(0,fnum-snum)    

    elif OP=="Multiplication":
        e.insert(0,fnum*snum)

    elif OP=="Division":
        e.insert(0,fnum/snum)    

    elif OP=="exponent":
        e.insert(0,pow(fnum,snum))

    elif OP=="modulus":
        e.insert(0,fnum%snum)

    elif OP=="Natural log":
        e.insert(0,log(fnum,snum))

    elif OP=="Square root":
        e.insert(0,sqrt(fnum))        

#Buttons--NUMBERS
button_1=Button(root,padx=40,pady=20,text="1",border=5,command=lambda:click(1))
button_2=Button(root,padx=40,pady=20,text="2",border=5,command=lambda:click(2))
button_3=Button(root,padx=40,pady=20,text="3",border=5,command=lambda:click(3))

button_4=Button(root,padx=40,pady=20,text="4",border=5,command=lambda:click(4))
button_5=Button(root,padx=40,pady=20,text="5",border=5,command=lambda:click(5))
button_6=Button(root,padx=40,pady=20,text="6",border=5,command=lambda:click(6))

button_7=Button(root,padx=40,pady=20,text="7",border=5,command=lambda:click(7))
button_8=Button(root,padx=40,pady=20,text="8",border=5,command=lambda:click(8))
button_9=Button(root,padx=40,pady=20,text="9",border=5,command=lambda:click(9))

button_0=Button(root,padx=40,pady=20,text="0",border=5,command=lambda:click(0))

#Buttons--OPERATIONS
button_add=Button(root,padx=51.5,pady=20,text="+",border=5,command=addition)
button_substract=Button(root,padx=53,pady=20,text="-",border=5,command=substraction)
button_multiply=Button(root,padx=53,pady=20,text="*",border=5,command=multiplication)

button_divide=Button(root,padx=40,pady=20,text="/",border=5,command=division)
button_equal=Button(root,padx=39,pady=20,text="=",border=5,command=equal)
button_allclr=Button(root,padx=42,pady=20,text="Clear",border=5,command=all_clear)

button_expon=Button(root,padx=40,pady=20,text="^",border=5)
button_modulo=Button(root,padx=40,pady=20,text="%",border=5)
button_natLog=Button(root,padx=37,pady=20,text="Ln",border=5)

button_sqrt=Button(root,padx=44,pady=20,text="Sqrt",border=5)

#button positions
button_1.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=0)

button_4.grid(row=2,column=2)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=0)

button_7.grid(row=1,column=2)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=0)

button_0.grid(row=4,column=1)

button_add.grid(row=1,column=3)
button_substract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)

button_divide.grid(row=4,column=0)
button_equal.grid(row=5,column=2)
button_allclr.grid(row=5,column=3)

button_expon.grid(row=5,column=0)
button_modulo.grid(row=5,column=1)
button_natLog.grid(row=4,column=2)

button_sqrt.grid(row=4,column=3)

root.mainloop()