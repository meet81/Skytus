# Create a base class Animal and subclasses Dog and Cat.
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("The souand animal makes")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says:Bark")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says:Miyau")
dog = Dog("Tommy")
cat =Cat("Miku")
dog.speak()
cat.speak()
# Create a class hierarchy for Vehicle → Car → ElectricCar.
class Vehical:
    def  __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def start(self):
        print(f"{self.brand} Vehecal is starting.")
    def show_speed(self):
        print(f"Speed:{self.speed}km/h")
class Car(Vehical):
    def __init__(self,brand,speed,doors):
        super().__init__(brand,speed)
        self.doors=doors
    def car_info(self):
        print(f"Brand:{self.brand},Doors:{self.doors}")
class ElectricCar(Car):
    def __init__(self,brand,speed,doors,battery_capacity):
        super().__init__(brand,speed,doors)
        self.battery_capacity=battery_capacity
    def charge(self):
        print(f"Battery_capacity:{self.battery_capacity}kwh")
    def fuel_type(self):
        print("Fuel_type:Electric")
Ec=ElectricCar("EV",180,4,120)
Ec.start()
Ec.show_speed()
Ec.car_info()
Ec.charge()
Ec.fuel_type()
    
# Implement method overriding in a base and derived class.
class Vehicle:
    def __init__(self,start):
        self.start=start
    def Car(self):
        print(f"Car is start with {self.start}")
class EV(Vehicle):
    def __init__(self,start,key):
        super().__init__(start)
        self.key=key
    def ElectericEv(self):
        print(f"EV start with both {self.key} or without {self.start}.")
car1=EV("carkey","key")
car1.Car()
car1.ElectericEv()

# Demonstrate multiple inheritance with two parent classes.
class Animal:
    def __init__(self,animal):
        self.animal=animal
    def animal_name(self):
        print(f"{self.animal} is a Running")
class Bird(Animal):
    def __init__(self, animal, bird):
        super().__init__(animal)
        self.bird = bird
    def bird_name(self):
        print(f"{self.bird} is flying")
class Zoo(Bird):
    def __init__(self,animal,bird):
        super().__init__(animal,bird)
    def zoo_name(self):
        print(f"{self.animal},{self.bird} in a Zoo.")
Z=Zoo("tiger","peacock")
Z.animal_name()
Z.bird_name()
Z.zoo_name()
     
# Create a polymorphic function that works with different shapes.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
def calculate_area(shape):
    print("Area:", shape.area())
c = Circle(5)
r = Rectangle(4, 6)
calculate_area(c)
calculate_area(r)

# Create a Bank system with SavingsAccount and CurrentAccount classes.
class SavingsAccount:
    def __init__(self, account_holder, balance=0, interest_rate=0.04):
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.balance}")
        else:
            print("Insufficient balance")
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added {interest}. Balance: {self.balance}")
class CurrentAccount(SavingsAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")
s = SavingsAccount("Meet", 10000)
s.deposit(2000)
s.withdraw(3000)
s.add_interest()
c = CurrentAccount("Alay", 5000)
c.withdraw(8000)
c.deposit(2000)

# Create a class with private attributes and getter/setter methods.
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age >0:
            self.__age=age
        else:
            print("Age must be positive")
s = Student("Meet", 21)
print(s.get_name())
print(s.get_age())
s.set_name("Alay")
s.set_age(25)
print(s.get_name())
print(s.get_age())
  
# Create a Teacher and Student class to show inheritance.
class Teacher:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub
    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.sub}")
class Student(Teacher):  
    def __init__(self, name, sub, enrollment_no):
        super().__init__(name, sub)  
        self.enrollment_no = enrollment_no
    def Num(self):
        print(f"Enrollment No: {self.enrollment_no}")
s = Student("Meet", "Maths", 101)
s.display()  
s.Num()     
# Create a MusicPlayer class and subclass Spotify to override play method.
class MusicPlayer:
    def __init__(self, song):
        self.song = song
    def play(self):
        print(f"Playing {self.song} on generic music player")
class Spotify(MusicPlayer):
    def play(self):
        print(f"Playing {self.song} on Spotify with premium features")
player1 = MusicPlayer("Shape of You")
player1.play() 
player2 = Spotify("Blinding Lights")
player2.play()  
# Demonstrate the use of super() in inheritance.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"Name:{self.name},Age:{self.age}")
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    def show(self):
        super().show()
        print(f"Employee_Id:{self.employee_id}")
E=Employee("Meet",29,33)
E.show()
        
