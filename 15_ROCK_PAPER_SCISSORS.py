import random
userWins=0
compWins=0

choices=["rock","paper","scissors"]

while True:    
    userPick=input("Type ROCK/PAPER/SCISSORS or Q to quit: ").lower()
    if userPick=="q":
        break
    if userPick not in choices:
        continue
    
    random_num=random.randint(0,2)
    compPick=choices[random_num]
    
    print("Computer picked",compPick+".")
    
    if userPick=="rock" and compPick=="scissors":
        print("You won this round.")
        userWins+=1
        
    elif userPick=="paper" and compPick=="rock":
        print("You won this round.")
        userWins+=1
        
    elif userPick=="scissors" and compPick=="paper":
        print("You won this round.")
        userWins+=1
        
    elif userPick==compPick:
        print("Its a tie.")
        
    else:
        print('You lost this round')
        compWins+=1

if userWins>=compWins:
    if userWins==compWins:
        print("\n\nIts a tie!!")
    else:
        print("CONGRATULATIONS!! You won.")
else:
    print("\n\nYOUL LOST!! Better Luck next time")                           
print("GOODBYE!!")        
                           
                           