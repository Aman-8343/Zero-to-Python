class online_store :
    count=0;

    def __init__(self,name,price):
        self.name=name
        self.price=price
        online_store.count+=1

    def getinfo(self):     #instance method
        print(f"price of {self.name} is {self.price}")

    @classmethod
    def cnt_product(cls):
        print(f"total product is {cls.count}")

p1=online_store("pen",10);
p1=online_store("phone",10000);
p1=online_store("phoN",1000);

p1.getinfo()

online_store.cnt_product()