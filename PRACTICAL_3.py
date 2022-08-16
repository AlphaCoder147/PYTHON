"""To simulate simple calculator that performs basic tasks such as addition, subtraction, 
multiplication and division with special operations like computing xy
and x!."""
 
fnum=int(input("Enter the first number: ")) #FIRST NUMBER
op=input("Enter operator: ")                #OPERATOR
snum=int(input("Enter the second number: ")) #SECOND NUMBER

#SUMMATION
def sum(fnum,snum):
    sum=fnum+snum
    print("The sum of the given numbers is ",sum)
#SUBTRACTION
def substract(fnum,snum):
    substract=fnum-snum
    print("The difference between the give numbers is ",substract)
#MULTIPLICATION
def multiply(fnum,snum):
    multiply=fnum*snum
    print("The product of the given numbers is ",multiply)
#DIVISION
def division(fnum,snum):
    division=fnum/snum
    print("The quotient of the given numbers is ",division)
#EXPONENT
def expo(fnum,snum):
    expo=fnum**snum 
    print("The value of fnum raise to snum is ",expo)
#FACTORIAL
def factorial(fnum):
    if(fnum>=1):
        result=fnum*factorial(fnum-1)
        print(result)
    else:
        result=1
    return result 
#SWITCH CASE
if op=="+":
    sum(fnum,snum)
elif op=="-":
    substract(fnum,snum)
elif op=="*":
    multiply(fnum,snum)
elif op=="/":
    division(fnum,snum)
elif op=="^":
    expo(fnum,snum)
elif op=="!":
    factorial(fnum)                    
