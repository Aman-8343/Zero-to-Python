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