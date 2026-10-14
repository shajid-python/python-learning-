# 1. importing the whole module 
import math
import random

#2. using math 
print(f"square root  of 64 is: {math.sqrt(64)}")
print(f"Value of pi is: {math.pi}")

#3. using random
print(f"Random number between 1 and 10: {random.randint(1, 10)}")
fruits = ['Apple', 'Banana', 'Mango']
print(f"Random fruit: {random.choice(fruits)}")

#4. importing specific functions
from datetime import datetime 
now = datetime.now()
print (f"current date and time: {now}") 