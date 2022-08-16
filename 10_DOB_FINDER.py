#CReate a program that takes day, month and year from you and tells you your Date of Birth, Day of birth and Age.
import calendar

day=int(input("Enter your DAY of birth:- "))

if(day<32):
    month=int(input("Enter your MONTH of birth in numerical:- "))
    year=int(input("Enter your YEAR of birth:- "))

    month_dic1={
       1:"January",
       2:"February",
       3:"March",
       4:"April",
       5:"May",
       6:"June",
       7:"July",
       8:"August",
       9:"September",
       10:"October",
       11:"November",
       12:"December"
    
    }

    def findDay(year,month,day):
       x=calendar.weekday(year,month,day)
       y=calendar.day_name[x]
       print("AND YOU WERE BORN ON",y)
       if calendar.isleap(year)==True :
           print("YOU WERE BORN ON A LEAP YEAR.")
       else:
           print("YOU WERE NOT BORN ON A LEAP.\n")
       #1
       # print(calendar.prmonth(year,month))       
       

#if(month=="Feb") and (day>28):
#   print("Ivalid Date in accordance to the month")    
    if day==1 or day==21 or day==31:
       print("Your date of Birth is",day,"st",month_dic1[month],year)
    elif day== 2 or day==22:
       print("Your date of Birth is",day,"nd",month_dic1[month],year)
    elif day==3 or day==23:
       print("Your date of Birth is",day,"rd",month_dic1[month],year)
    else:
       print("Your date of Birth is",day,"th",month_dic1[month],year)     

      
else:
    print("VALUE ERROR:There does not exist a month with 32 days.")
#1st Method-Zeller's Rule
#F= k+[(13*m-1)/5] +D+ [D/4] +[C/4]-2*C where
#k is  the day of the month.                      #HIGHLY Inaccurate
#m is the month number.
#D is the last two digits of the year.
#C is the first two digits of the year. 

#2nd Method THE KEY VALUE METHOD              #ACCURATE ON PAPER BUT NOT ON CODE...
#take the last twodidgits of a year
#divide it by 4 and discard remainder
#Add months key value
# if the date is january or february of a leap year substract 1 from the step above
#add year code from the table
#add the last two digits of the year
#divide the obained value by 7
# Take the remainder and correspond.


