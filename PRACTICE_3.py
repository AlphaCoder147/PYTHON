"""To accept N numbers from user. Compute and display maximum in list, minimum in list, 
sum and average of numbers."""
n=int(input("Enter the number of inputs: "))
list=[]
i=0
for i in range(n):
    x=int(input("Enter element: "))
    list.append(x)
    i+=1
print(list)    
print("Largest element in the list is",max(list))
print("Smallest element is the list is",min(list))
print("Summation of elements is",sum(list))
print("The average of elements is",sum(list)/n)