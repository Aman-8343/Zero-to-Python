#instance method -> First parameter self ,acces instance and class attributes

class laptop:
    storage_type="ssd"

    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage

    def get_info(self):
        print(f"laptop has {self.ram} and {self.storage} {self.storage_type}") 


l1=laptop("16gb",256)
print(l1.ram)

l1.get_info()



#class methods -> First parameter cls, access class attributes, use decorator(@classmethod)

class laptop:
    storage_type="ssd"

    @classmethod
    def get_storage_type(cls):
        print(f"storage type ={cls.storage_type}")

l1=laptop()
l1.get_storage_type()



#static method ->  no compulsory parameter , cannot acces class and instance attributes, decorator(@staticmethod)


class laptop:
    storage_type="ssd"

    @staticmethod
    def calc_price(price,discount):
        final_price=price-(discount*price/100)
        print(f"final price is : {final_price}")


l1=laptop()
l1.calc_price(40_000,10)


