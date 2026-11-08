class Contact:
    # The __init__ method runs automatically when we creat a new contact 
    def __init__(self, name, phone):
        self.name = name 
        self.phone = phone

    # A method  (a function inside a class)
    def display_info(self):
        print(f"Name: {self.name} | phone: {self.phone}")

# 1. Creating instances (objects) from the class
contact1 = Contact("Shajid", "1234567890")
contact2 = Contact("Ammi", "6281115114")

# 2. Accessing attributes directly
print(contact1.name)

# 3. calling methods
contact1.display_info()
contact2.display_info()