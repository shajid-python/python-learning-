# --- Numbers ---
num1 = 10
num2 = 3
print(num1 / num2)   # Float division
print(num1 // num2)  # Floor division (drops decimal)
print(num1 % num2)   # Modulus (remainder)
print(num1 ** num2)  # Power (10 to the power of 3)

# --- Lists (mutable, ordered) ---
courses = ['Math', 'Physics', 'Python']
print(courses)
courses.append('Chemistry')  # Add to the end
print(courses)
print(courses[0])  # Access first item
print(courses[-1]) # Access last item
print(courses[1:3]) # Slicing

# --- Tuples (immutable, ordered) ---
coordinates = (10.5, 20.3)
print(coordinates)
# coordinates[0] = 11.0  # If you uncomment this, it will give an error! (Because tuples cannot be changed)

# --- Sets (unordered, no duplicates) ---
my_set = {1, 2, 3, 3, 3}
print(my_set)  # See how the duplicates are removed?
my_set.add(4)
print(my_set)