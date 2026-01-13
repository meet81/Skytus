# Write a program to read a file and display its contents.
with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "r") as file:
    content = file.read()
    print(content)
# Write a program to count the number of lines in a file.
filename=r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt"
try:
    with open(filename,"r") as file:
        line_count =sum(1 for line in file)
    print(f"numbers of lines in'{filename}':{line_count}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Write a program to count how many times each word appears in a file.
filename = r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
    words = content.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.items():
        print(f"{word}: {count}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Write a program to write 5 user-entered sentences to a file.
filename = r"C:\Users\meet1\OneDrive\Desktop\Python\sentences.txt"
with open(filename, "w") as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        file.write(sentence + "\n")  
print(f"5 sentences have been written to '{filename}' successfully.")

# Write a program to append a list of strings to an existing file.
filename = r"C:\Users\meet1\OneDrive\Desktop\Python\sentences.txt"
lines_to_append = ["My name is meet"]
with open(filename, "a") as file:
    for line in lines_to_append:
        file.write(line + "\n") 
print(f"Lines have been appended to '{filename}' successfully.")

# Write a program to read a file and print only lines containing a specific word.
filename = r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt"
word_to_search = input("Enter the word to search for: ").lower() 
try:
    with open(filename, "r") as file:
        for line in file:
            if word_to_search in line.lower():  
                print(line, end="") 
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# 6 Write a program to read a file and print only lines containing a specific word.

specific_word = input("Enter the word to search for: ")
try:
    with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "r") as file:
        lines = file.readlines()
        print(f"Lines containing the word '{specific_word}':")
        for line in lines:
            if specific_word in line:
                print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")

# 7 Write a program to replace a specific word in a file and save changes.
specific_word = input("Enter the word to be replaced: ")
replacement_word = input("Enter the replacement word: ")
try:
    with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "r") as file:
        content = file.read()

    updated_content = content.replace(specific_word, replacement_word)

    with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "a") as file:
        file.write(updated_content)
    print("Word replaced successfully.")
except FileNotFoundError:
    print("Error: File not found.")

# 8 Write a program to merge the contents of two text files into a third file.
file1=input("Enter the first file name:")
file2=input("Enter the second file name:")
file3=input("Enter the output file name:")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()
    with open(file3, "w") as f3:
        f3.write(content1 + "\n" + content2)
    print("Files merged successfully into", file3)
except FileNotFoundError:
    print("Error: One or more files not found.")

# 9 Write a program to read a CSV file and display its content in a formatted way.

import csv
try:
    with open(r"c:\Users\meet1\OneDrive\Desktop\Python\m.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)

        print(f"{' | '.join(headers)}")
        print("-" * 40)

        for row in csvreader:
            print(f"{' | '.join(row)}")
except FileNotFoundError:
    print("Error: CSV file not found!!.")

# 10 Write a program to back up a file by copying its contents into another file.
try:
    with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "r") as source_file:
        content = source_file.read()

    with open(r"c:\Users\meet1\OneDrive\Desktop\Python\sample2.txt", "a") as backup_file:
        backup_file.write(content)

    print("File backup created successfully.")

except FileNotFoundError:
    print("Error: Original file not found.")