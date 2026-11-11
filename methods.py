import datetime

class Employee:
    # Class Variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

         # Regular Method (needs self)
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class Method (needs cls) - Changes the class variable
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Class Method (needs cls) - Alternative constructor!
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    # Static Method (needs neither self nor cls)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# --- TESTING THE CODE ---

# 1. Testing the Class Method (set_raise_amt)
Employee.set_raise_amt(1.05)
print(f"New raise amount: {Employee.raise_amount}")

# 2. Testing the Alternative Constructor (from_string)
emp_str_1 = 'Shajid-Khan-50000'
new_emp_1 = Employee.from_string(emp_str_1)

print(f"Created from string: {new_emp_1.fullname()} - Pay: {new_emp_1.pay}")

# 3. Testing the Static Method (is_workday)
my_date = datetime.date(2026, 11, 11) # November 11, 2026 (Wednesday)
print(f"Is {my_date} a workday? {Employee.is_workday(my_date)}")

weekend_date = datetime.date(2026, 11, 15) # November 15, 2026 (Sunday)
print(f"Is {weekend_date} a workday? {Employee.is_workday(weekend_date)}")