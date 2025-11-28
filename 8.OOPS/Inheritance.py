# reusing attributes and functions of parent class
'''
class employee:
    company = "Google"
    st_time="5"
    end_time="7"

    def showDetails(self):
        print("This is an employee")

    def change_st_time(self,newtime):
        self.st_time=newtime


class teacher(employee):
   def __init__(self,name):
       self.name=name
    
t1=teacher("fdjs")
t2=teacher("fdfd")
print(t1.name,t1.st_time)

t1.change_st_time("6")
print(t1.name,t1.st_time)
'''


#multilevel inheritance
'''
class emp:
    st_time="5"
    end_time="7"

class admin(emp):
    def __init__(self,role):
        self.role=role

class accountant(admin):
    def __init__(self,salary,role):
        super().__init__(role)         # super() call the parent class constructor
        self.salary=salary

acc1=accountant("3434","ca")
print(acc1.salary,acc1.role)
'''

#multiple inheritance
class teacher :
    def __init__(self,salary):
        self.salary=salary
 

class student :
    def __init__(self,gpa):
        self.gpa=gpa


class TA(teacher,student):
    def __init__(self, salary,gpa,name):
        super().__init__(salary)
        student.__init__(self,gpa)
        self.name=name

ta1=TA(3433,9,"aman")
print(ta1.salary,ta1.gpa,ta1.name)

