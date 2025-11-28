'class attributes:  which belongs to class'
'Instance attribute: which belongs to object'


class student:
    clgname ="abc"      #class attribute
    pi=3.1

    def __init__(self,name, roll):    #instance attribute
        self.name=name
        self.roll=roll
        self.pi=3.142


stu1=student("dkfjd",3);
print(stu1.clgname) ;    

print(stu1.pi)    #instance attribute have higher priority

