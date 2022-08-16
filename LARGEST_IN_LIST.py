numbers=[]  #initializing the list
n=int(input("Enter the number of elements to be inserted in a list: "))    #Setting up number of inputs
while(n>=1):
    i=int(input("Enter your elements: "))
    numbers.append(i)
    n-=1
print(numbers)
print("Largest element in the list is:",max(numbers))    
