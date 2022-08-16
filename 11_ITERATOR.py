print("List Iteration")
l=["Alpha","Bravo","Charlie","Delta"]
for i in l:
    print(i)
print("\nTUPLE ITERATION")
t=("Echo","Foxtrot","Golf","Hotel") 
for i in t:
    print(i)
print("\nString Iteration")
s="India","Joker","Kilo"
for i in s:
    print(i)

y=[t]
print(y)        
print(type(y))
for i in range(1,5):#here i is the value to be printed but 
     for j in range(i):#It is also the range of j  
         print(i,end=' ')#Which means j will be executed i printing the value of i
     print()       
     
     
     print(46%7)