# 1. Conditionals (If/Elif/Else)
age = int(input("Enter your age: ")) # We use int() because input() always returns a string

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 2. For Loop (Repeating a task 5 times)
print("\n--- For Loop ---")
for i in range(5):
    print(f"Hello! This is loop number {i}")

# 3. While Loop (Countdown)
print("\n--- While Loop ---")
count = 5
while count > 0:
    print(count)
    count = count - 1 # This is crucial! Without this, it loops forever.
print("Blast off!")

# 4. Looping through a list (Combining Day 2 & Day 4)
print("\n--- Looping through a list ---")
courses = ['Math', 'Physics', 'Python']
for course in courses:
    print(f"I am studying {course}")