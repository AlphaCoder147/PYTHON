import random
Range_top=input("Enter a Number:-")
if Range_top.isdigit():
    Range_top=int(Range_top)
    if Range_top<=0:
        print("Enter a number Greater than ZERO next time...")
        quit()
else:
    print("Enter a number next time..")
    quit()
            
random_num=random.randint(0,Range_top)
guesses=0
while True:
    guesses+=1
    userGuess=input("Enter your guess:- ")
    if userGuess.isdigit():
        userGuess=int(userGuess)
        if userGuess<0:
            print("Your Guess should be Greater than ZERO...")
            quit()
    else:
        print("Your Guess should be an Integer...")
        quit()
        continue
#MADE BY ADVAIT KESKAR(ALPHA PANTHER KILLER)    
    if userGuess==random_num:
        print("You guessed it CORRECT!!")
        break
    else:
        print("Try Again!!")         
print("You guessed the number in "+str(guesses)+" guesses.")
if guesses==1:
    print("CONGRATULATIONS!! You Guessed it in First Try...")
                   