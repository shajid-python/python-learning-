# 1. Try to open a file that doesn't exist
try:
    with open('non_existent.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("Error: The file you tried open does not exist.")

#2. try to do math with invalid types
try:
    result = "10" + 5
except TypeError:
    print("Error: You can't add a string and an integer directly.")