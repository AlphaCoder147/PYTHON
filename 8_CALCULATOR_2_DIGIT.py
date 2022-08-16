import math
print("\t\t\t\t1)'+' = ADDITION\n\t\t\t\t2)'-' = SUBSTRACTION\n\t\t\t\t3)'*' = MULTIPLICATION\n\t\t\t\t4)'/' = DIVISION\n")
print("\t\t\t\t5)'%' = REMAINDER\n\t\t\t\t6)'^' = EXPONENTIAL VALUES\n\t\t\t\t7)'//' = ABSOLUTE QUOTIENT\n\t\t\t\t8)'log' = LOGARITHM\n")
print("\t\t\t\t9)'root' = ROOT\n\t\t\t\t10)'ln' = NATURAL LOG\n\t\t\t\t11)'dist' = DISTANCR FROM ORIGIN ")


num1=float(input("Enter First Number:- "))
op=input("Enter Operator:- ")
num2=float(input("Enter Second Number:- "))

if(op=="+"):          #Addition
    print(num1+num2)
elif(op=="-"):        #Substraction
    print(num1-num2)
elif(op=="*"):        #Multiplication
    print(num1*num2)    
elif(op=="/"):        #Division
    print(num1/num2)
elif(op=="%"):        #Remainder of any number divided by any number
    print(num1%num2)    
elif(op=="^"):        #Any  number raised to any number   
    print(pow(num1,num2))
elif(op=="//"):       #Absolute Quotient of any number divided by any number
    print(num1//num2)    
elif(op=="log"):     #Log of base any number to any number
    print(math.log(num1,num2)) 
elif(op=="root"):    # Nth root of any number 
    print(pow(num1,1/num2))    
elif(op=="ln"):      #Natural log of any number   # ENTER NUM2=0
    print(math.log(2.71,num1))   
elif(op=="dist"):    # Distance of any point from Origin  #POINT=(NUM1,NUM2)
    print(math.sqrt(num1*num1+num2*num2))             
else:
    print("Invalid Operator")                