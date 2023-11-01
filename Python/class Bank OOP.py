class Bank:
    def __init__(self,rate):
        self.rate = rate
        
    def calculate_amount(self,principal):
        return principal * (1 + self.rate) ** 10
    
class BankING(Bank):
    def __init__(self):
        super().__init__(0.1)
        
class BankICIC(Bank):
    def __init__(self):
        super().__init__(0.2)
        
class BankIS(Bank):
    def __init__(self):
        super().__init__(0.3)
        
        
bank_name = input("Enter the bank (ING/ICIC/IS): ")

if bank_name == "ING":
    bank_class = BankING()
elif bank_name == "ICIC":
    bank_class = BankICIC()
elif bank_name == "IS":
    bank_class = BankIS()
else:
    print("invalid!")
    exit()
    
principal = float(input("Enter the principal: "))

total = principal + bank_class.calculate_amount(principal)

print(f"Total amount after 10 years: {total}")