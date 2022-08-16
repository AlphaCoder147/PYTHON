#Prime or Not
'''num=int(input("Enter a Number:-"))
if(num>1):
    for i in range(2,num//2):
        if(num%i==0):
            print(" Is not a prime number.")
            break
        else:
            print(" Is a prime number.")'''
        #(OR)
from math import sqrt
num=int(input("Enter a Number:-"))
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
        
        
        