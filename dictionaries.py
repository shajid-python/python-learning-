# 1. Create a dictionary
car = {
    'brand': 'Toyota',
    'model': 'Hybrid',
    'year': 2026,
    'colors': ['Black', 'White', 'Red'],
}

# 2. Access values
print(car['brand'])
print(car.get('price', 'price not available'))

# 3. Add and update
car['year'] = 2023
car['price'] = 20000000
print(car)

# 4. Delete
del car['colors']
print(car)

# 5. Loop through it
for key, value in car.items():
    print(key, ':', value)