#--- Numbers ---
num1 = 10
num2 = 3
print(num1 / num2) #float division
print(num1 // num2) #floor division
print(num1 % num2) #modulus (remainder)
print(num1 ** num2) #power(10 to the power of 3)


 #--- lists(mutable,ordered) ---
courses = ['Math', 'Physics', 'Python']
print(courses)
courses.append('chemistry') #add to the end 
print(courses)
print(courses[0]) #access first item
print(courses[-1]) #access last item
print(courses[1:3]) #slicing


# --- tupels (immutable,ordered) ---
coordinates = (10.5,20.3)
print(coordinates) 
# coordinates[0] = 11.0 # if you uncomment this, it will give an error! (because tupels cannot be changed)

# --- sets (unordered,no dupilicates) ---
my_set = {1, 2, 3, 3, 3}
print(my_set)  #see how the dupilicates are removed?
my_set.add(4)
print(my_set)