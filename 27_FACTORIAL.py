def Factorial(n):
    if(n>=1):
        result=n*Factorial(n-1)
        print(result)
    else:
        result=1
    return result  

n=int(input("Enter a number: "))
print("\n\nFactorial results:")
Factorial(n)      
        