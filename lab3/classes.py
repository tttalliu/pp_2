#task1
class MyClass:
    def getString(self):
        self.string=input()
    def printString(self):
        print(self.string)
f=MyClass()

f.getString()
f.printString()

#task2
class Shape:
    def __init__(self):
        self.area_v=0
    def area(self):
        return self.area_v
        
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.area_v
a=Shape()
print(a.area())

#task3
class Shape:
    def __init__(self):
        self.area_v=0
    def area(self):
        return self.area_v

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width   
b=Rectangle(2,3)
print(b.area())

#task4
import math
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def show(self):
        print(f"({self.x},{self.y})")

    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y

    def dist(self,point2):
        D=math.sqrt((self.x-point2.x)**2 + (self.y-point2.y)**2)
        return D
p1=Point(2, 3)
p2=Point(5, 7)

p1.show()

p1.move(4, 6)
p1.show()

D=p1.dist(p2)
print(D)

#task5
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print(f"Deposit amount {amount} must be positive.")
            return False
    def withdraw(self, amount):
        if amount <=self.balance:
            self.balance -= amount
            return True
        else:
            print(f"Insufficient balance to withdraw {amount}.")
            return False
account = Account("AA")

account.deposit(-12000)
account.withdraw(0)

print("Current balance:", account.balance) 

#task6
def is_prime(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers=list(filter(lambda x: is_prime(x),numbers))
print(prime_numbers) 
