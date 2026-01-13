# Write a program to handle division by zero error.
num1=int(input("Enter a num: "))
num2=int(input("Enter a num: "))
try:
    result=num1/num2
    print("Result: ",result)
except ZeroDivisionError:
    print("Error division by zero is not allowed")
    
# Write a program to handle invalid integer input.
try:
    num=int(input("Enter a num: "))
    print("valid integer: ",num)
except ValueError:
    print("integer is not valid integer")
    
# Write a program to open a file and handle the “file not found” error.
try:
    file = open("Ass3.py","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error:file not found")
    
# Write a program to demonstrate multiple exception blocks.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Calculation successful.")

# Write a program to use finally for resource cleanup.
try:
    file = open("Ass2.py","r")
    print(file.read())
except FileNotFoundError:
    print("Error:file not found")
finally:
    print("File close successfully") 
  
# Write a program to create a custom exception for invalid age (<18).
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age<18:
        raise InvalidAgeError("Age must be 18 or above")
    print("acess granted")
except InvalidAgeError as e:
    print("custom exception:",e)
except ValueError:
    print("Please enter a valid number")
    
# Write a program to handle IndexError when accessing a list.
num=[10,20,30,40,50]
try:
    index=int(input("Enter a  index: "))
    print("value at index:",num[index])
except IndexError:
    print("Error:index out of range")
except ValueError:
    print("Erroe:please enter a valid integer")
    
# Write a program that takes two numbers and handles all possible errors.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Program execution completed.")

# Write a program to log errors to a file instead of printing them.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except Exception as e:
    file = open("Ass4.py","a")
    file.write(str(e)+"\n")
    file.close()
    
# Write a program that validates an email format and raises an exception for invalid ones.	
class InvalidEmailError(Exception):
    pass
try:
    email = input("Enter your email: ")
    if "@"  not in email or "." not in email :
        raise InvalidEmailError("Invalid email format")
    print("Valid email address")
except InvalidEmailError as e:
    print("Error:", e)