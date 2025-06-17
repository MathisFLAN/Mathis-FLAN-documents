class Bank :
    def __init__ (self, name: str, bank: str, account: int, balance: int):
        self.name = name
        self.bank = bank
        self.account = account
        self.balance = balance

    def add_money(self, money):
        self.balance += money
        return f"[name: {self.name} bank: {self.bank} account:{self.account} balance {self.balance}]"
    
    def remove_money(self, money):
        retenu = self.balance
        self.balance -= money
        if self.balance > 0 :
            return f"[name: {self.name} bank: {self.bank} account:{self.account} balance {self.balance}]"
        else :
            self.balance = retenu
            print("error, vous serrez à découvert si vous faites ça, opération annulée.")
            return f"[name: {self.name} bank: {self.bank} account:{self.account} balance {self.balance}]"
    
    #def withdraw():
        

paul = Bank("Paul", "LCL", 15455, 100)
gregoire = Bank("Grégoire", "LCL", 21983, 100)
jean = Bank("Jean", "BNP", 8527, 100)

print(paul.add_money(500))
print(paul.remove_money(200))
print(gregoire.remove_money(200))
