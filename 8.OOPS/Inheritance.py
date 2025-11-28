# reusing attributes and functions of parent class

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