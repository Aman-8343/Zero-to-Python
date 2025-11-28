# Wrapping up data and functions into a single unit 
# data hiding  (pubic(.), protected(._), private(.__))

class bank:
    def __init__(self,id,balance):
        self.id=id
        self.__balance=balance

    
    def get_val(self):    #getter
        return self.__balance
    
    def set_val(self,newbal):   #setter
        self.__balance=newbal



acc1=bank("33",2300)
acc2=bank("34",4500)
acc3=bank("35",700)

acc2.set_val(5000)
print (f"{acc2.id} new balbance is {acc2.get_val()}")

#acces private values  (clears data hiding)
print(acc3.id, acc3._bank__balance)



