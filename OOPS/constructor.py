#constructor is called by using __init__ method

class student :

    # def _init(self):
    #     print("only one paramenter i.e self") # default constructor

    def __init__ (self,name,gpa):            # parameterized construtor
        self.name=name;
        self.gpa=gpa;

    
    def get_cgpa(self):
        return self.gpa
        


stu1=student("aman",9.8)
print(stu1.name,stu1.gpa)

stu2=student("raj",6.6)

print(f"{stu1.name} cgpa is {stu1.get_cgpa()}")
print(stu1.get_cgpa())

