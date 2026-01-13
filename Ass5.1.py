# Function to check if a number is prime.
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True 
num = 17
if is_prime (num):
    print("Prime num")
else:
    print("Not prime num")

# Function to reverse a string.
def reverse_string(s):
    return "".join(reversed(s))
text="Meet"
print(reverse_string(text))

# Function to find factorial.
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
num=5
print(factorial(num))

# Function to calculate simple interest.
def simple_interest(principle,rate,time):
    return(principle*rate*time)/100
p=1000
r=5
t=2
interest=simple_interest(p,t,r)
print("simple_interest:",interest)

# Function to check if a word is palindrome.
def is_palindrom(word):
    word = word.lower()
    return word == word[::-1]
print(is_palindrom("madam"))
print(is_palindrom("meet"))

# Function to count vowels in a string.
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count
text="Meet Patel"
print(count_vowels(text))
# Function to merge two lists.
def merge_list(list1,list2):
    return list1+list2
a=[1,2,3]
b=[4,5,6]
print(merge_list(a,b))
# Function to find GCD of two numbers.
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
num1=33
num2=81
print("Gcd:",gcd(num1,num2))

# Function to find area of rectangle.
def rectangle_area(lenght,width):
    return lenght*width
le=33
wi=11
print("Rectangle area: ",rectangle_area(le,wi))

# Function to check Armstrong number.
def is_armstrong(n):
    num_str=str(n)
    num_digits=len(num_str)
    sum_digits=sum(int(digit)**num_digits for digit in num_str)
    return n == sum_digits
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
