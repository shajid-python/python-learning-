#1. Basic function (no inputs ,no outputs)
def greet():
    print("Hello, Shajid welcome to functions")

greet()


# 2. functions with parameters (inputs)
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet_person("Shajid", 25)

#3. Function with a return value (output)
def add_numbers(num1, num2):
    return num1 + num2


result = add_numbers(10, 5)
print(f"The sume is:{result}")