#1. Writing to a file (overwrites everything already there)
with open('notes.txt', 'w') as f:
    f.write("line 1: Hello, python!\n")
    f.write("line 2: I am learning file I/O.\n")
    f.write("line 3: This is my third line.\n")

#2. appending to a file (adds to the end)
with open('notes.txt', 'a') as f:
    f.write("line 4: This was added letter.\n")

#3. reading the file back
print("--- Reading the file ---")
with open('notes.txt', 'r') as f:
    content = f.read()
    print(content)

#4. Reading line by line 
print("--- Reading line by line ---") 
with open('notes.txt', 'r') as f:
    for line in f:
        print(f"Line: {line.strip()}")# .strip() removes the newline character