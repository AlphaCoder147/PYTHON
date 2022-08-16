"""to accept n numbers from user compute and display max in list min in list sum and average of numbers"""
n=int(input("Enter the number of inputs: "))

list=[]
while(n>=1):
    i=int(input("Enter elements: "))
    list.append(i)
    n-=1
print("the list is ",list)
print("The maximum element in list is ",max(list))
print("The minimum element in list is",min(list))
x=sum(list)
print("The sum of elements in the list is ",x)
print("The average of elemnts in the list is ",x/len(list))
    
    