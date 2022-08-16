"""Create class EMPLOYEE for storing details (Name, Designation, gender, Date of Joining 
and Salary). Define function members to compute a)total number of employees in an 
organization b) count of male and female employee c) Employee with salary more than 
10,000 d) Employee with designation “Asst Manager”"""

class employee():
    count=0
    def __init__(self,name,designation,gender,doj,salary):
        employee.count+=1
        self.name=name
        self.designation=designation
        self.gender=gender
        self.doj=doj
        self.salary=salary
    def number_of_employees(self):
        print("Number of employees are",employee.count)
    def male_and_female_employees(self,emp):
        male=0
        female=0
        for x in emp:
            if x.gender=="Male":
                male+=1
            else:
                female+=1
        print("No. of Male employees:",male)
        print("No. of Female employees:",female)            
    def high_salary(self,emp):
        print("Employees with salary more than 10,000/- are:\n")
        for x in emp:
            if x.salary>10000:
                print(x.name)
    def asst_managers(self,emp):
        print("Assistant managers of the company are:\n")
        for x in emp:
            if x.designation=="Asst.Manager":
                print(x.name)
             
emp1=employee("Harsh J","Asst.Manager","Male","01/03/2019",15000)
emp2=employee("Sanika K","Manager","Female","01/07/2017",25000)      
emp3=employee("Aniruddha T","Designer","Male","01/02/2020",5000)
emp4=employee("Parth D","Content Writer","Male","01/09/2019",6500)
emp5=employee("Anamika J","HR","Female","01/05/2019",10000)
emp6=employee("Rasmika T","Sales Rep","Female","01/01/2020",4000)
emp7=employee("Ananya M","Asst.Manager","Female","01/09/2019",15000)
emp8=employee("Yash D","Sales Rep","Male","01/03/2021",5000)
emp9=employee("Harshita M","Sales Rep","Female","01/04/2021",5000)
emp_list=[emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9]
emp1.number_of_employees()
emp1.male_and_female_employees(emp_list)
emp1.high_salary(emp_list)
emp1.asst_managers(emp_list)