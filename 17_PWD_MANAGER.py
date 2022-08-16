from cryptography.fernet import Fernet
# def writeKey():
#     key=Fernet.generate_key()
#     with open("key.key","wb") as keyFile:
#         keyFile.write(key)
# writeKey()     
   
def loadKey():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key        
master_password=input("Enter master password: ")
key=loadKey()+master_password.encode()
fer=Fernet(key)

def view():
    with open("17_PWDS.txt","r") as X:
        for line in X.readlines():
            info=line.rstrip()
            id, pswd=info.rsplit(" | ")
            print("Login ID:",id,"\t","Password:",str(fer.decrypt(pswd.encode().decode())))        
def enter():
    ID=input("Enter the USERNAME/LOGIN ID: ")
    pwd=input("Enter the PASSWORD: ")
    
    with open("17_PWDS.txt","a") as X:
        X.write("Login ID:"+str(ID)+" | "+"Password: ",str(fer.encrypt(pwd.encode()).decode())+"\n\n")


while True:
    Operat=input("Would you like to view your passwords or Create a new entry to the list?\nType 'view' to view your passwords\nType 'enter' to add a new entry\nType 'q' to quit the program.").lower()
    if Operat=="q":
        print("Thank You for Using PASSWORD MANAGER v1.01.")
        break
    elif Operat=="enter":
        enter()
        continue
    elif Operat=="view":
        view()
        continue
    else:
        print("Invalid Input\nTRY AGAIN!")
        continue
