#Sum of squares of first n natural numbers by ADVAIT KESKAR
#defining function
def sqr_Sum(n):
    sum=0
    for i in range(1,n+1):    #for every number in range the command will be executed, starting from ZERO
        sum=sum+(i*i)
    print("The sum of Squres of",n,"is",sum)                #Value will be returned
n=int(input("Enter a number: "))
sqr_Sum(n)    