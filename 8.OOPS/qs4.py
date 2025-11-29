'''
class BankAccount:
    def __init__(self,accountno,owner,balance):
        self.accountno=accountno
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
            self.balance+=amount
            print(f"deposited {amount} current balance :{self.balance}")

    def withdraw(self,amount):
         self.balance-=amount
         print(f"{amount} withdraw current balance is {self.balance}" )

    def  check_balance(self):
         return self.balance

acc1=BankAccount(1,"aman",500)
acc1.deposit(1000)
acc1.withdraw(200)
'''

'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []       # list of reviews
    
    def add_review(self, review):
        self.reviews.append(review)
        print("Review added.")

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        if not self.reviews:
            print("No reviews yet.")
        else:
            print("Reviews:")
            for r in self.reviews:
                print("-", r)


# Example Usage
b = Book("Atomic Habits", "James Clear")
b.add_review("Very helpful book!")
b.add_review("Loved the writing style.")
print("Total reviews:", b.count_reviews())
b.display_reviews()
'''

# class student :
#     def __init__(self,name,roll,marks):
#         self.__name=name
#         self.__roll=roll
#         self.__marks=marks

#     def setval(self,newname,newroll,newmarks):
#         self.name=newname
#         self.roll=newroll
#         self.marks=newmarks




#fuction overriding
'''
class shape:
    def area(self):
        print("area is :")

class circle(shape):
    def area(self,radius):
        pi=3.14
        self.radius=radius
        area=pi*radius*radius
        print(f"area of circle is : {area}")

class rectangle(shape):
    def area(self,len,breadth):
        self.len=len
        self.breadth=breadth
        area=len*breadth
        print(f"area of rectangle  is : {area}")

class triangle(shape):
    def area(self,base,height):
        self.height=height;
        self.base=base
        area=1/2*base*height
        print(f"area of triangle is : {area}")


c1=circle()
c1.area(5)
r1=rectangle()
r1.area(5,6)
t1=triangle()
t1.area(4,5)
        
'''


#abstract class
from abc import ABC,abstractmethod

class Emp:
    @abstractmethod
    def calc_salary(self):
        pass

class Intern(Emp):
    def calc_salary(self,salary):
        self.salary=salary
        print(self.salary)
        
class full_time(Emp):
    def calc_salary(self,salary):
        self.salary=salary
        print(self.salary)

class contract(Emp):
    def calc_salary(self,salary):
        self.salary=salary
        print(self.salary)

i1=Intern()
i1.calc_salary(5000)
ft=full_time()
ft.calc_salary(6000)
c1=contract()
c1.calc_salary(9000)






        
        


