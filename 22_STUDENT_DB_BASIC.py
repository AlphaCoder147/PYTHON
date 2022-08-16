num=int(input("Enter number of students:"))
stud=[]
for x in range(num):
    roll=int(input("Enter Roll no. :"))
    name=input("Enter name: ")
    marks=float(input("Enter marks:"))
    stud.append((roll,name,marks))
for x in stud:
    print('%d%5s%10f'%(x[0],x[1],x[2]))  
topper=max(stud)   
for x in topper:
    print("topper is:",name)
    #print(topper)
    break
# if x[2]==max:
#     print("topper")
# else:
#     print("Not topper")    