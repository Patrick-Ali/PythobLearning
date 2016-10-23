class BankAccount:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__balance = 0

    def deposit(self, amount):
        if type(amount) ==  int:
            self.__balance += amount
        else:
            raise TypeError("That is not a vailid input")

    def withdraw(self, amount):
        if type(amount) ==  int :
            if self.__balance > 0:
                if (self.__balance - amount) >= 0:
                    self.__balance -= amount
                else:
                    hold = amount - self.__balance
                    print("You are attempting to with draw £ %d more than you have" % (hold))
            else:
                print("The account is empty")
        else:
            raise TypeError("That is not a vailid input")

        
# & amount > 0
