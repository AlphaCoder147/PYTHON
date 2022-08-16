"""To accept an object mass in kilograms and velocity in meters per second and display its 
momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is 
its velocity. """

m=float(input("enter mass of object in Kgs: "))
c=float(input("Enter the velocity of the object in m/s^2 : "))
e=m*c*c
print("The momentum of the object is",e,"kg m^2 s^-4.")