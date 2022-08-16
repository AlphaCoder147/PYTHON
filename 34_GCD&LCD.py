from numpy import product


num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
ls1=[]
ls2=[]
for i in range(1,num1+1):
    if num1%i==0:
        ls1.append(i) 
        print(ls1)           
for j in range(1,num2+1):
    if num2%j==0:
        ls2.append(j)
        print(ls2)
Fl=set(ls1)
Sl=set(ls2)      

x=list(Fl&Sl)
print("The least common divisor is: ",x[0])
print("The greatest common divisor is: ",product(x))
            