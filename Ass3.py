# Take a string input and print its length.
string=("My name is meet.")
a=len(string)
print(a)

# Convert a sentence to lowercase.
A=("MEET")
print(A.lower())

# Replace spaces with underscores in a string.
sentence=("I am Intern")
print(sentence.replace(" ","_"))

# Extract the first and last character of a string.
string=("Meet live in Valsad")
print(string[0:1])
print(string[-1])

# Reverse a string using slicing.
string1=("Meet")
print(string1[-1:-5:-1])

# Count how many times a letter appears in a string.
a=("Meet is playing chess.")
letter=input("Enter a letter: ")
print(a.count(letter))

# Check if a word is present in a sentence.
b = ("stand is eampty")
word=("is")
if word in b:
    print("word is present")
else:
    print("word is not present")


# Take name & age and print using f-string formatting.
Name =("Meet")
Age =("21")
print(f"My name is {Name} & my age is {Age}.")

# Remove extra spaces from the start and end of a string.
D=("My project is good.")
print(D.replace(" ",""))

# Join a list of words into a single string with - between them.
D=("My project is good.")
print(D.replace(" ","-"))

# Create a list of your 5 favorite movies.
Movies=["3idiot","Chhelo divas","K.G.F","Lallo","Avatar"]
print(Movies)

# Add a new movie to the list.
Movies=["3idiot","Chhelo divas","K.G.F","Lallo","Avatar"]
Movies.append("toxic")
print(Movies)

# Remove the first movie from the list.
Movies=["3idiot","Chhelo divas","K.G.F","Lallo","Avatar"]
Movies.pop(3)
print(Movies)

# Sort a list of numbers in ascending order.
mylist=[1,3,45,95,33]
mylist.sort()
print(mylist)

# Reverse a list.
Movies=["3idiot","Chhelo divas","K.G.F","Lallo","Avatar"]
Movies.reverse()
print(Movies)

# Find the largest number in a list.
list=[1,3,45,95,33]
print(max(list))

# Merge two lists into one.
list1=[1,3,45,95,33]
list2=[55,67,99,2,8]
list3 = list1 + list2
print(list3)

# Access the last element of a list without using index number.
list=[1,3,45,95,33]
M=list.pop()
print(M)

# C6reate a nested list and access a specific inner element.
nested_list =[[10,20,30],["3idiot","Chhelo divas","K.G.F"],[60,40,50,]]
element=nested_list[2][1]
print(element)

# Count how many times an element appears in a list.
list=[33,1,3,3,45,95,33,33]
element=33
M=list.count(element)
print(M)

