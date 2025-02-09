

class Banking:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        print(f'im Depsoiting Rs: {amount}')
        self.balance = self.balance + amount


    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(f'Im withdrawing {amount} ')

# b = Banking('akil',5000)
# print(b.balance,b.name)

class Saving_Account(Banking):

    def withdraw(self,amount):
        if amount > self.balance :
            raise Exception(f'amount should be greter than balance')
        super().withdraw(amount)


s = Saving_Account('harsha',2000)

# s.withdraw(1000)
# s.deposit(3000)


# tha above example is for inheritance and polymorphism

######################################################################

# method overloading  # here am partially overloading


def add(*args):
    print(sum(args))

# add(1)
# add(1,2)
# add(23,45)


############################################ constructor overloading

class Company:

    def __init__(self,a):
        print(f'the name of comapny is {a}')

    def __init__(self,a,b):
        print(f'the name of comany and ceo is {a}and {b}')


# c = Company(4,5)

############################################ Encapsulation
class Demo:

    value = 10   # class Variable

    def __init__(self,a):
        self.a = a           # class instanse variable

    def spam(self):   # instance method
        print(f'in Spam Demo {self.a},{self.value}')

d = Demo(20)
d.spam()
print(d.value)
print(d.a)


