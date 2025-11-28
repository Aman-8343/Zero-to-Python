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

    
    @staticmethod
    def calcdiscnt(price,discount):
        print(f"final prince ={ price- price*discount/100}")

p1=online_store("pen",10);
p2=online_store("phone",10000);
p3=online_store("phoN",1000);

p1.getinfo()

online_store.cnt_product()

p2.calcdiscnt(p2.price,13)