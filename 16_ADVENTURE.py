Intro=input("Guard: Welcome Stranger!\nWelcome to the great city of Dunwall.\nDo you seek passage into the city?(Y/N)\nStranger:- ")
def game_end_G():
    print("\nCongratulations you have successfully survived the First Chapter...")
    quit()
def game_end_B():
    print("\nOH NO!! You met your demise...\nBetter Luck Next Time...\nGAME OVER!!")
    quit()    
def inp_Error():
    print("\nERROR: Enter a valid value next time...\nTIP: The brackets at the end of a decision tell you your input prompts.\nGAME OVER!!")
    quit()
    
if Intro=="Y":
    print("Guard: Okay, But in order to enter the city you need to register yourself")
    name=input("Please Enter your name in the logbook.\nStranger: ")
    print("Guard: "+name+",What a great name.")
    print("Narrator: You enter the city of Dunwall.")
    ch1=input("Narrator: You have two roads in front of you.\n\t  The RIGHT one leading to the the Royal Observatory.\n\t  And the LEFT one leading to the Golden Cat Inn.\n\t  Where do you wish to go?(R/L)\n"+name+": ")
    if ch1=="R":
        print("Narrator: You enter the Royal Observatory.")
        ch1_1=input("Narrator: You come across Dr. Synthia, The Royal Physician. She asks you to visit her in the basement.\n\t  Do you want to go to the basement?(Y/N)\n"+name+": ")
        if ch1_1=="Y":
            end1="Narrator: You got down to the basement with Dr. Synthia.\n\t  There she subdues you and makes you her LABRAT.\n\t  You rot in her cell for 20 years and eventually DIE..."
            print(end1)
            game_end_B()
        elif ch1_1=="N":
            end1_2="You turn back and go to the Golden Cat Inn wher you stay in the city for 3 more days enjoying the city's hospitality.\n\t  You return HOME.  "
            print(end1_2)
            game_end_G()
        else:
            inp_Error()    
    elif ch1=="L":
        print("Narrator: You enter the Golden Cat Inn.")
        ch2_1=input("Narrator: You come across your childhood friends and nobles, the Pendelton Brothers.\n\t  They ask you if you want to join them in the steam bath.\n\t  Will you join them?(Y/N)\n"+name+": ")
        print(ch2_1)
        if ch2_1=="Y":
            end2="Narrator: You go to the steam bath with the Pendelton Brothers.\n\t  As you were about to relax the steam pump bursts KILLING YOU and PENDELTON BROTHERS."
            print(end2)
            game_end_B()
        elif ch2_1=="N":
            end2_1="Narrator: You go to your room.\n\t  You stay in the city for 3 more days enjoying the city's hospitality.\n\t  ṇYou return HOME."
            print(end2_1)
            game_end_G()
        else:
            inp_Error()
    else:
        inp_Error()        
elif Intro=="N":
    print("Guard: Then why the fuck are you here??\n\t FUCK OFF Before I kill you.")
    quit()
else:
    inp_Error()                                    