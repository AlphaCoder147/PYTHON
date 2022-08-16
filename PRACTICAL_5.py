'''To accept the number and Compute a) square root of number, b) Square of number, c) 
Cube of number d) check for prime, d) factorial of number e) prime factors'''
from math import *
num=int(input("Enter a number: "))

def prime(num):
    prime_flag=0
    if(num>1):
        for i in range(2,int(sqrt(num))+1):
            if(num%i==0):
                prime_flag=1
            break
        if(prime_flag==0):
            print (num,"is a Prime Number.")
        else: 
            print (num,"is not a prime number.") 
    else:
        print("Enter a number greater than 1.")

def primefactors(num):
    c=2
    while(num>1):
        if(num%c==0):
            print(c,end=" ")
            num/=c
        else:
            c+=1
            
squareroot=sqrt(num)
sqr=num*num
cube=num*num*num
fact=factorial(num)
print("The Squreroot of number is",squareroot)
print("The squre of the number is",sqr)
print("The cube of number is",cube)
print("The factorial of number is",fact)
prime(num)
print("Prime factors are")
primefactors(num)