#1 Check if a person is eligible to vote (age ≥ 18).
num=int(input("enter a age: "))
for i in range(1):
    if num >=18:
        print("Person is eligible")
    else:
        print("Person is not eligible")  

#2 Grade calculator based on marks: 90+ = A, 80+ = B, else C.
Marks=int(input("enter a marks: "))
if Marks >=95<=100:
    print("Grade A+")
if Marks >=90<=95:
    print("Grade A")
if Marks >=80<=90:
    print("Grade B")
if Marks >=70<=80:
    print("Grade c")
if Marks >=60 <=70:
    print("Grade D")
if Marks >=50 <=60:
    print("Grade E")
else:
    print("Fail")
    
#3 Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
signal=input("enter a signal light: ")
if signal == "Red":
    print("stop")
elif signal == "Yellow":
    print("Wait")
elif signal == "Green":
    print("Go")
else:
    print("Invalid color")
    
#4 ATM withdrawal check: sufficient balance or not.
balance=33000
amount=int(input("Enter a amount: "))
if balance >= amount:
    print("sufficient balance")
else:
     print("sufficient not balance")

#5 Check if a number is positive, negative, or zero.
num=int(input("Enter a num: "))
if num < 0:
    print("number is positive")
elif num > 0:
    print("number is negative")
else:
    print("number is zero")

#6 Check if a number lies within a given range.
num=int(input("Enter a num: "))
if num >=1 & num <=100:
    print("number is in range.")
else:
    print("number is in not a range.")

#7 Username & password verification.
Username=input("Enter a Username: ")
password=int(input("Enter a password: "))
if Username == "Meet" and password == "1876" :
    print("User is verified.")
else:
    print("User is not verified.")

#8 Electricity bill calculator based on units consumed.
unit=int(input("Enter a Bill units: "))
if unit <=100:
    Bill = unit *7.3
elif unit >100 and unit <=200:
    Bill = unit *7.3+150
elif unit  >200 and unit <=300:
    Bill = unit *7.3+350
elif unit  >300 and unit <=400:
    Bill = unit *7.3+500
elif unit  >400 and unit <=500:
    Bill = unit *7.3+800
else:
    Bill = unit * 7.3 + 1000
print("Electricity bill: ",Bill)
    
#9 Simple calculator (add, subtract, multiply, divide).
num1=int(input("Enter a num: "))
num2=int(input("Enter a num: "))
operation=input("enter a operation:(+,-,*,/,%): ")
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
elif operation == "%":
    print(num1%num2)
else:
    print("Invalid operation.")
#10 Check type of triangle (equilateral, isosceles,scalene).
a=int(input("Enter a num: "))
b=int(input("Enter a num: "))
c=int(input("Enter a num: "))
if a==b==c:
    print("triangle is equilateral")
elif a==b or b==c or c ==a:
    print("triangle is  isosceles")
else:
    print("triangle is scalene")