class Bank :
    def __init__ (self, name: str, bank: str, account: int, balance: int) -> None:
        self.name = name
        self.bank = bank
        self.account = account
        self.balance = balance

    def __str__(self) -> str:
        return f"[name: {self.name} bank: {self.bank} account:{self.account} balance {self.balance}]"

    def add_money(self, money) -> None:
        self.balance += money
    
    def remove_money(self, money) -> bool:
        if self.balance - money < 1 :
            print("error, vous serrez à découvert si vous faites ça, opération annulée.")
            return False
        self.balance -= money
        return True
    
    def transfer(self, money, destinataire) -> bool:
        if self.balance - money > 0 :
            if self.bank == destinataire.bank:
                self.balance -= money
                destinataire.balance += money
                return True
            else :
                print("error, les banques ne correspondent pas, opération annulée.")
                return False
        else :
            print("error, vous serrez à découvert si vous faites ça, opération annulée.")
            return False
        

paul = Bank("Paul", "LCL", 15455, 100)
gregoire = Bank("Grégoire", "LCL", 21983, 100)
jean = Bank("Jean", "BNP", 8527, 100)

paul.add_money(500)
paul.remove_money(200)
gregoire.remove_money(200)
paul.transfer(200, gregoire)

print(paul)
print(gregoire)
print(jean)