class Employee:
    #tis is a class variable! (shared by all employees)
    raise_amount = 1.04

    #  This is a class variable to keep count of employees
    num_of_emps = 0 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

        # Every time we create an employee, increase the count by 1
        Employee.num_of_emps += 1

    def apply_raise(self):
        # We use self.raise_amount so we can change it for specific employees later if needed
        self.pay = int(self.pay * self.raise_amount)


# 1. create some employees 
emp_1 = Employee('Sajid', 'Khan', 50000)
emp_2 = Employee('Ammi', 'Khan', 60000)
emp_3 = Employee('Rahul', 'Sharma', 70000)

# 2. Check the class variable
print(f"Total Employees: {Employee.num_of_emps}")


# 3. Check the instance variables 
print(f"Original pay for {emp_1.first}: {emp_1.pay}")


#4. Apply the raise 
emp_1.apply_raise()
print(f"New pay for {emp_1.first} after raise: {emp_1.pay}")


# 5. Change the class variable
Employee.raise_amount = 1.10 # Now everyone gets a 10% raise!
print(f"The new raise amount for the company is {Employee.raise_amount}")
