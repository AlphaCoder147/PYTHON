print("Welcome to my COMPUTER QUIZ.")
Play=input("Do you wish to play the quiz?\nAns:-  ")
if Play != "yes":
    quit()
print("GET READY TO RUMBLE!!!")
score=0
answer=input("Q1)\tWhat does CPU stand for?\nAns:-\t")
if answer.lower()=="central processing unit":
    score+= 1
answer=input("Q2)\tWhat does GPU stand for?\nAns:-\t")
if answer.lower()=="graphics processing unit":
    score+= 1 
answer=input("Q3)\tWhat does RAM stand for?\nAns:-\t")
if answer.lower()=="random access memory":
    score+= 1    
answer=input("Q4)\tWhat does ROM stand for?\nAns:-\t")
if answer.lower()=="read only memory":
    score+= 1
answer=input("Q5)\tWhat does PSU stand for?\nAns:-\t")
if answer.lower()=="power supply unit":
    score+= 1
print("Your Score is "+str(score)+"/5")
print("You have got "+str((score/5)*100)+"%"+" questions correct")                    