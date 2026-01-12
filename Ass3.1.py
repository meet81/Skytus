# Create a tuple with 5 numbers.
tuple=(5,6,7,8,9)
print(tuple)

# Access the third element in a tuple.
tuple=(5,6,7,8,9)
print(tuple[2])

# Unpack a tuple into separate variables.
fruits=["apple","banana","mango","cherry","graps"]
fruits=["banana","apple","mango","graps","cherry"]
print(fruits[0:4])

# Create a set of 5 fruits.
fruits=("apple","banana","mango","cherry","graps")
print(fruits)

# Add a new fruit to the set.
fruit={"apple","banana","mango","cherry","grapes"}
fruit.add("avocado")
print(fruit)

# 3Remove an element from a set.
fruits1={"apple","banana","mango","cherry","grapes"}
fruits1.remove("mango")
print(fruits1)
# Find union of two sets.
set1={2,5,6,8,10}
set2={7,11,12,15,33}
set3=set1.union(set2)
print(set3)

# Find intersection of two sets.
set1={2,5,6,8,33,11,10}
set2={7,11,12,15,33}
set3=set1.intersection(set2)
print(set3)

# Check if one set is subset of another.
set1={33,11}
set2={7,11,12,15,33}
set3=set1.issubset(set2)
print(set3)

# Convert a list with duplicate values into a set to remove duplicates.
set1=[2,5,6,8,33,11,10,7,11,12,15,33]
set2=set(set1)
print(set2)

# Create a dictionary storing student names and marks.
dic={
    "meet":85,"prince":75,"jay":80
}
print(dic)

# Add a new key-value pair to an existing dictionary.
dic={
    "meet":85,"prince":75,"jay":80
}
dic["alay"]=83
print(dic)

# Delete a key-value pair from a dictionary.
dic={
    "meet":85,"prince":75,"jay":80
}
dic.pop("jay")
print(dic)

# Merge two dictionaries into one.
dic1={
    "meet":85,"prince":75,"jay":80
}
dic2={
    "het":85,"sanju":75,"nij":80
}
dic3=dic1 | dic2
print(dic3)

# Check if a key exists in a dictionary.
dic={
    "meet":85,"prince":75,"jay":80
}
if "meet" in dic:
    print("key is exists")
else:
    print("key is not exists")

#Count word frequency in a given string using a dictionary.
string=("meet is a student meet live in valsad.")
words=string.split()
word_count={}
for word in words:
    word_count[word] = word_count.get(word, 0)+1
print(word_count)

#Find the key with the maximum value in a dictionary.
dic={
     "meet":85,"prince":75,"jay":80
}
max_key=max(dic,key=dic.get)
print(max_key)

#Reverse keys and values in a dictionary.
dic={
     "meet":85,"prince":75,"jay":80
}
reversed_dic={value:key for key,value in dic.items()}
print(reversed_dic)

#Update the value for a specific key.
dic={
     "meet":85,"prince":75,"jay":80
}
dic["jay"]=90
print(dic)

#Convert a list of tuples into a dictionary.	
list=[ ("meet",85),("prince",75),("jay",80)]
my_dic=dict(list)
print(my_dic)