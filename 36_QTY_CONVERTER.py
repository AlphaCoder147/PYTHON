print("Enter the conversion you wish to perform: \n 1)Length Conversion \n 2)Temperature Conversion. ")
inp=int(input("Input: "))

if inp==1:
    print("Enter the conversion you wish to perform: \n 1) Kms to Miles \n 2)Miles to Kms \n 3)Meters to Feet \n 4)Feet to Meters")
    t=int(input("Input: "))
    if t==1:
        e1=float(input("Enter Distance in Kilometers: "))
        r1=e1*0.621
        print("Output:",r1,"miles.")
    elif t==2:
        e2=float(input("Enter Distance in Miles: "))
        r2=e2*1.609
        print("Output:",r2,"Kilometers.")
    elif t==3:
        e3=float(input("Enter distance in meters: "))
        r3=e3*3.28084
        print("Output:",r3,"Ft")
    elif t==4:
        e4=float(input("Enter distance in Feet: "))
        r4=e4*0.305
        print("Output:",r4,"m")
    else:
        print("Invalid Input.\nRefer the list displayed above.")
elif inp==2: #MADE BY APK
    print("Enter the conversion you wish to perform: \n 1)C to F \n 2)F to C \n 3)C to K \n 4)K to C")
    s=int(input("Input: "))
    if s==1:
        f1=float(input("Enter Temperature in Centigrade: "))
        g1=(f1*1.8)+32
        print("Output:",f1,"F")
    elif s==2:
        f2=float(input("Enter Temperature in Fahrenheit: "))
        g2=(f2-32)/1.8
        print("Output:",g2,"Centigrade.")
    elif s==3:   #MADE BY APK
        f3=float(input("Enter Temperature in Celcius: "))
        print(float(map(lambda f3: f3+273.14)),"Kelvin.")
    elif s==4:
        f4=float(input("Enter Temperature in Kelvin: "))
        print(float(map(lambda f4: f4-273.14)),"Celcius.")
    else:
        print("Invalid Input")                           
else:
    print("Invalid Input.")    
    #ALPHA PANTHER KILO
    
    