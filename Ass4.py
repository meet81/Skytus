#1 Print numbers from 1 to 10.
for i in range(1,11):
    print(i)

#2 Display multiplication table for a given number.
num = int(5)
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#3 Find factorial of a number.
n = int(input("enter a number: "))
fact = 1
for i in range(1,n+1):
    fact *=i
print("Factorial= ",fact)

#4 Generate the first N Fibonacci numbers.
num = int(5)
a,b=0,1
for i in range(num):
    print(a)
    a,b = a+b,a

#5 Check if a number is prime.
num=int(input("Enter a number: "))
count = 0
for i in range(1,num+1):
    if num % i ==0:
        count +=1
if count == 2:
    print("prime is number")
else:
    print("Not prime is number")
    
#6 Reverse a number (e.g., 123 → 321).
num = int(123)
rev =0
while num > 0:
    digit = num %10
    rev = rev * 10 + digit
    num//=10
print("Reverse num: ",rev)

#7 Count digits in a number.
n=int(input("enter a num: "))
count=0
while n > 0:
    count +=1
    n//=10
print("Digigts num: ",count)

#8 Find sum of even numbers between 1–100.
sum=0
for i in range(1,100):
    if i %2 ==0:
        sum += i
print(sum)

#9 Print a pyramid pattern.
num=5
for i in range (1,num+1):
    print("*" *i)

#10 Find all divisors of a number.
num=10
for i in range(1,num+1):
    if num % i ==0:
        print(i)