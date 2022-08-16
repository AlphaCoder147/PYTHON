def Addition(num1,num2):
    """Calling this function will result in addition of the given digits"""
    print("Addition: ",num1+num2,"\n")
def Substraction(num1,num2):
    """Calling this function will result in substraction of the given digits"""
    print("Substraction: ",num1-num2,"\n")
def Multiplication(num1,num2):
    """Calling this function will result in multiplication of the given digits"""
    print("Multiplication: ",num1*num2,"\n")
def Division(num1,num2):
    """Calling this function will result in division of the given digits"""
    print("Division: ",num1/num2,"\n")

num1=int(input("Enter Number 1: "))
num2=int(input("Enter number 2: "))
help(Addition)
Addition(num1,num2)
print("\n\n")
help(Substraction)
Substraction(num1,num2)
print("\n\n")
help(Multiplication)
Multiplication(num1,num2)
print("\n\n")
help(Division)
Division(num1,num2)
