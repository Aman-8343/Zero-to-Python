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