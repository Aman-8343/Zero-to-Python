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