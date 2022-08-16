"""To calculate salary of an employee given his basic pay (take as input from user). 
Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of 
basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary 
payable after deductions"""

employees={
    "1901":"Rocky",
    "1902":"Ricky",
    "1903":"Chandrachud",
}

emp_id=input("Enter your employee id: ")
basic_pay=int(input("Enter your basic pay: "))
hra_val=int(input("Enter your HRA percentage: "))
ta_val=int(input("Enter your TA percentage: "))
tax_val=int(input("Enter your TAX percentage: "))

hra=basic_pay * (hra_val/100)
ta=basic_pay * (ta_val/100)
gross_sal=basic_pay+ta+hra
tax=gross_sal * (tax_val/100)
total_salary=gross_sal-tax
print("Your name is",employees[emp_id])
print("Your total salry is:",total_salary)
