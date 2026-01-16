# Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
class Car:
    def __init__(self,brand,model,speed=33):
        self.brand=brand
        self.model=model
        self.speed=speed
    def accelerate(self,increase):
        self.speed += increase
        print(f"Accelerate.Current.speed:{self.speed}km/h")
    def brake(self,decrease):
        self.speed -=decrease
        if self.speed < 0:
            self.speed =0
        print(f"Brake.current.sppeed:{self.speed}km/h")
car1=Car("toyato","fortuner")
car1.accelerate(20)
car1.brake(5)
        
# Create a BankAccount class with deposit and withdraw methods. 
class BankAccount:
    def __init__(self,amount=33000):
        self.amount=amount
    def deposit(self,increase):
        self.amount +=increase
        print(f"Total.amount:{self.amount}RS")
    def withdraw(self,decrease):
        if decrease > self.amount:
            print("Insufficient balance!")
        else:
            self.amount -=decrease
            print(f"Total.amount:{self.amount}RS")
User=BankAccount()
User.deposit(50000)
User.withdraw(20000)
        
        
# Create a Student class with a method to calculate average marks. 
class Student:
    def __init__(self,maths,eng,che,phy):
        self.maths=maths
        self.eng=eng
        self.che=che
        self.phy=phy
        self.Total_marks=sum([self.maths,self.eng,self.che,self.phy])
    def Avg_marks(self):
        Avgmarks = self.Total_marks/4
        print("Avgmarks:",Avgmarks)
student=Student(50,60,70,80) 
student.Avg_marks()

# Create a Rectangle class with methods to find area and perimeter. 
class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def area(self):
        return self.lenght*self.width
    def perimeter(self):
        return 2*(self.lenght+self.width)
Rec = Rectangle(50,25)
print("Area:",Rec.area())
print("Perimeter:",Rec.perimeter())
# Create an Employee class that displays salary details. 
class Employee:
    def __init__(self,day_basic_salary):
        self.day_basic_salary=day_basic_salary
    def salary1(self):
        month_day=int(input("enter a day in wok togo: "))
        bouns=5000
        if month_day >= 24:
            Total_salary=(month_day*self.day_basic_salary)+bouns
            print("salary:",Total_salary)
        elif month_day <= 24 and month_day>0 :
            Total_salary=(24-month_day*self.day_basic_salary)+bouns
            print("salary:",Total_salary)
        else:
            month_day=0
            Total_salary=0
            print("salary:",Total_salary)
emp =Employee(600)
emp.salary1()
     
# Create a Book class to store title, author, and price, and display details. 
class Book:
    def __init__(self,title,author,price):
        self.title=title 
        self.author=author
        self.price=price
    def display(self):
        print("Book_Title:",self.title)
        print("Author_Name:",self.author)
        print("Book_Price:",self.price,"RS")
book1=Book("Python Programming","Gudio","850")
book1.display()
        
# Create a Circle class to find area and circumference. 
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 3.14*self.radius
c=Circle(8)
print("Area:",c.area())
print("Circumference:",c.circumference())
        
# Create a Laptop class with a method to apply discounts on price. 
class Leptop:
    def __init__(self,company_name,modal,price):
        self.company_name=company_name
        self.modal=modal
        self.price=price
    def discounts(self):
        discount = (self.price/100)*10
        discount_amount=self.price-discount
        print(discount_amount)
price=Leptop("HP","Victus",75000)
price.discounts()
# Create a Flight class with seat booking functionality. 
class Flight:
    def __init__(self,flight_no,seat):
        self.flight_no=flight_no
        self.seat=seat
    def seat_book(self):
        print("Flight_no:",self.flight_no)
        print("Seat_no:",self.seat)
booking=Flight("AB13245","B15")
booking.seat_book()
# Create a Shop class with a method to add and list products.
class Shop:
    def __init__(self, name):
        self.name = name
        self.products = [] 

    def add_product(self, product_name, product_price):
        product = {"name": product_name, "price": product_price}
        self.products.append(product)
        print(f"Product '{product_name}' added successfully!")

    def list_products(self):
        if not self.products:
            print("No products in the shop.")
        else:
            print(f"Products in {self.name}:")
            for idx, product in enumerate(self.products, start=1):
                print(f"{idx}. {product['name']} - ${product['price']}")

my_shop = Shop("HP")
my_shop.add_product("Laptop", 800)
my_shop.add_product("Mouse", 25)
my_shop.list_products()

    