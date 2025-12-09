class Client:
    def __init__(self, CIN, firstName, lastName, tel=""):
        self.__CIN = CIN
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.__accounts = []   

    #  Getters 
    def getCIN(self):
        return self.__CIN

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getTel(self):
        return self.__tel

    # Setter
    def setTel(self, tel):
        self.__tel = tel

    #  Register an Account 
    def addAccount(self, account):
        self.__accounts.append(account)

    def listAccounts(self):
        print(f"\nAccounts for {self.__firstName} {self.__lastName} ({self.__CIN}):")
        if not self.__accounts:
            print("  -> No accounts.")
        else:
            for acc in self.__accounts:
                print(f"  - Account #{acc.getCode()} | Balance = {acc.getBalance()}")

    # Display Client 
    def display(self):
        print(" Client Information ")
        print("CIN:", self.__CIN)
        print("Name:", self.__firstName, self.__lastName)
        print("Telephone:", self.__tel)


class Account:
    __nbAccounts = 0   # static attribute to count accounts

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__balance = 0
        self.__code = Account.__nbAccounts
        self.__owner = owner
        self.__transactions = []    # NEW history list

        # Register this account in the client 
        owner.addAccount(self)

    #  Getters
    def getBalance(self):
        return self.__balance

    def getCode(self):
        return self.__code

    def getOwner(self):
        return self.__owner

    #  Helper Methods 
    def __record(self, message):
        self.__transactions.append(message)

    def displayTransactions(self):
        print(f"\nTransaction History for Account #{self.__code}")
        if not self.__transactions:
            print("  -> No transactions yet.")
        else:
            for t in self.__transactions:
                print(" -", t)

    # - Credit
    def credit(self, amount):
        if amount <= 0:
            print(" Credit amount must be positive.")
            return

        self.__balance += amount
        self.__record(f"Credit: +{amount}")
        print(f" Credited {amount}. New balance = {self.__balance}")

    # Debit 
    def debit(self, amount):
        if amount <= 0:
            print(" Debit amount must be positive.")
            return
        if amount > self.__balance:
            print(" Insufficient balance.")
            return

        self.__balance -= amount
        self.__record(f"Debit: -{amount}")
        print(f" Debited {amount}. New balance = {self.__balance}")

    #  Transfer 
    def credit(self, amount, fromAccount=None):
                if fromAccount is None:
            # direct credit
            if amount <= 0:
                print(" Credit amount must be positive.")
                return
            self.__balance += amount
            self.__record(f"Credit: +{amount}")
            print(f" Credited {amount}. New balance = {self.__balance}")
        else:
            # transfer credit from another account
            self.__balance += amount
            self.__record(f"Received Transfer: +{amount} from Account #{fromAccount.getCode()}")

    def debit(self, amount, toAccount=None):
        if toAccount is None:
            # simple debit
            if amount <= 0:
                print(" Debit amount must be positive.")
                return
            if amount > self.__balance:
                print(" Insufficient balance.")
                return

            self.__balance -= amount
            self.__record(f"Debit: -{amount}")
            print(f" Debited {amount}. New balance = {self.__balance}")
        else:
            # debit for transfer
            if amount > self.__balance:
                print(" Transfer failed: insufficient balance.")
                return False
            self.__balance -= amount
            self.__record(f"Sent Transfer: -{amount} to Account #{toAccount.getCode()}")
            return True

    def transfer(self, amount, account):
        """Transfer money to another account."""
        if amount <= 0:
            print(" Transfer amount must be positive.")
            return

        # Try to debit this account
        if self.debit(amount, account):
            # Credit the other account
            account.credit(amount, self)
            print(f"✔ Transfer of {amount} to Account #{account.getCode()} completed.")

    #  Display 
    def display(self):
        print("----- Account Summary -----")
        print("Account Code:", self.__code)
        print("Owner:", self.__owner.getFirstName(), self.__owner.getLastName())
        print("Balance:", self.__balance)

    @staticmethod
    def displayNbAccounts():
        print("Total Accounts Created:", Account.__nbAccounts)