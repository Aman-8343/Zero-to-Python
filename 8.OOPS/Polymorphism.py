#many forms

#fuction  overriding -> redefing parent class func in child class

class emp:
    def get_design(self):
        print("dessination= emp")

class admin(emp):
    def get_design(self):
        print("dessination= admin")

a1=admin()
a1.get_design()

e1=emp()
e1.get_design()


#duck Typing -> if it walk like a duck and quacks like a duck , it is a duck

class pycharm:
    def execute(self):
        print("compiling")
          

class laptop:
    def execute(self,):
        print("running")

l1=laptop()
l1.execute()

p1=pycharm()
p1.execute()
