"""To accept students five courses marks and compute his/her result. Student is passing if 
he/she scores marks equal to and above 40 in each course. If student scores aggregate 
greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the 
grade if first division. If aggregate is 50>= and <60, then the grade is second division. If 
aggregate is 40>= and <50, then the grade is third division. """

num=int(input("Enter the number of students: "))

for i in range(num):
    maths=int(input("Enter the marks obtained by roll number in MATHEMATICS: "))
    physics=int(input("Enter the marks obtained by roll number in PHYSICS: "))
    chem=int(input("Enter the marks obtained by roll number in CHEMISTRY: "))
    biology=int(input("Enter the marks obtained by roll number in BIOLOGY: "))
    eng=int(input("Enter the marks obtained by roll number in ENGLISH: "))
    if maths<40 or physics<40 or chem<40 or biology<40 or eng<40:
        print("You Have Failed this year.")
    else:    
        percen=int(((maths+physics+chem+biology+eng)/500)*100)  
        if percen>75:
            print("Your percentage is",percen,"%")
            print("Congratulations you have earned DISTINCTION")
        elif percen>=60 and percen<75:
            print("Your percentage is",percen,"%")
            print("Congratulations you have earned FIRST CLASS")
        elif percen>=50 and percen<60:
            print("Your percentage is",percen,"%")    
            print("Congratulations you have earned SECOND CLASS")
        elif percen>=40 and percen<50:
            print("Your percentage is",percen,"%")    
            print("Congratulations you have earned THIRD CLASS")
        else:
            print("Your percentage is",percen,"%")    
            print("OH NO!!! YOU HAVE FAILED")
    i+=1                         