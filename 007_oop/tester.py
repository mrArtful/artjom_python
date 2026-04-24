import datetime

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def pay_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day: datetime.datetime) -> bool:
        if day.weekday() in [5, 6]:
            return False
        return True



    

emp1 = Employee('Jack', 'Smith', 1200)
emp2 = Employee('Sarah', 'Jones', 2200)

# print(emp1.first)
# print(emp1.last)
# print(emp1.pay)
# print(emp1.email)

# print(emp1.fullname())
# print(Employee.fullname(emp1))

# print(emp1.__dict__)

# print(emp1.num_of_employees)
# print(Employee.num_of_employees)

# from pprint import pp

# print("OBJECT")
# pp(emp1.__dict__)
# print("CLASS")
# pp(Employee.__dict__)
# print("OBJECT2")
# pp(emp2.__dict__)
# emp2.set_raise_amount(1.10)
# print(emp1.pay)
# print(emp2.pay)
# emp1.pay_raise()
# print(emp1.pay)
# print(emp2.pay)
# emp3 = Employee.from_string('Bob-Green-5000')

# print(emp3.fullname())
# print(emp3.email)

# people = ['Roman-Kutselepa-1500', 'Simon-Summers-4000', 'Mary-Watson-3000']

# people_objects = []
# for person in people:
#     people_objects.append(Employee.from_string(person))

# print(people_objects[2].email)


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Starting')
#         result = func(*args, **kwargs)
#         print('Finished')
#         return result
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print('Hello', name + '!')

# say_hello('Roman')

# d = datetime.datetime(2025, 4, 19)

# print(Employee.is_workday(d))
# print(emp1.is_workday(d))

print(emp1.fullname)
print(emp1.email)
print(emp1.__dict__)