class Bank:
    def __init__(self, IFSC_Code, bankname, branchname, loc):
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc

class Customer:
    def __init__(self, CustomerID, custname, address, contactdetails):
        self.CustomerID = CustomerID
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails

class Account(Bank):
    def __init__(self, IFSC_Code, bankname, branchname, loc, AccountID, Cust, balance):
        super().__init__(IFSC_Code, bankname, branchname, loc)
        self.AccountID = AccountID
        self.Cust = Cust
        self.balance = balance

    def getAccountInfo(self):
        return f"Account ID: {self.AccountID}\nCustomer Name: {self.Cust.custname}\nBalance: {self.balance}"

    def deposit(self, amount, is_cash=True):
        if is_cash:
            self.balance += amount
            return f"Deposited {amount} (cash). New balance: {self.balance}"
        else:
            return "Non-cash deposits are not supported."

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient balance for withdrawal."

    def getBalance(self):
        return f"Current balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, IFSC_Code, bankname, branchname, loc, AccountID, Cust, balance, SMinBalance):
        super().__init__(IFSC_Code, bankname, branchname, loc, AccountID, Cust, balance)
        self.SMinBalance = SMinBalance

    def getSavingAccountInfo(self):
        return f"Account ID: {self.AccountID}\nCustomer Name: {self.Cust.custname}\nBalance: {self.balance}"

    def withdraw(self, amount):
        if self.balance - amount >= self.SMinBalance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient balance for withdrawal."

if __name__ == "__main__":
    # Create a customer
    customer1 = Customer(101, "DikshaY", "123 Barra Street", "diksha@gmail.com")

    # Create a savings account
    savings_account1 = SavingsAccount("ABC123", "SBI", "Kanpur", "Uttar Pradesh", 1001, customer1, 5000, 1000)

    print(savings_account1.getAccountInfo())
    print(savings_account1.deposit(2000))
    print(savings_account1.withdraw(500))
    print(savings_account1.getBalance())
