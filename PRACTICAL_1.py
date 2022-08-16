"""To calculate salary of an employee given his basic pay(Taken fron user), Calculate gross saa of the employee
let HRA be 10 percent of basic pay and TA 5 percent of basic pay 
let employee pay profesiional tax as 2 percent of total salary.
Calculate net salary paid after deduction"""

basic_pay=float(input("Enter Basic Pay: "))  #Taking Input
hra=float(basic_pay*0.1)        #HRA
ta=float(basic_pay*0.05)        #TA

total_salary=basic_pay+hra+ta   #TOTAL SALARY

tax=float(total_salary*0.02)    #TAX

net_salary=total_salary-tax     #NET SALARY

print("Your net salary is ",net_salary,"/- ONLY")