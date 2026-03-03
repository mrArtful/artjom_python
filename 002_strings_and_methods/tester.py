string_sample = "Hello world world"
                #0123456789......
                        # -4-3-2-1
string_sample2 = "first letteR is lowErcase"
string_sample3 = "   ***!!!    extra whitespace string  !!!***    "
german_sample = "der Fluß"

# [START:END:STEP]
# print(string_sample[0:5])
# print(string_sample[-6:-2])

# print(string_sample[-5:-1])

# print(string_sample[-5:])
# print(string_sample[:5])

# print(string_sample[::2])
# print(string_sample[::-1])


# print(len(string_sample))

# print(german_sample.upper())

# print(german_sample.lower())
# print(german_sample.casefold())

# print(string_sample2.capitalize())
# print("anna-maria".title())

# print(string_sample.replace('world', 'planet', 1))

print(string_sample3.strip(' *!'))

# print(string_sample.count('world', 7, 8))
# print(string_sample.find('world', 7))

# a = 'Hello'
# b = "World" \
#     "Hello again!"

# b = """Hello
# People
# Of
#         Planet
#                         Earth"""

# print(b)

# if True:
#     a = """Hello
#         People
#         Of
#         Planet
#         Earth"""
#     print(a)

# print('Th\nat\'s\\')

# print("Johns salary is " + str(3000))
# print("*" * 30)

# print('Hello', 123, False, 13.213, sep=" - ", end=" ")
# print("Second line")
# print("Second line")

# print("hello world".find(start=0, end=-1, sub="world"))

# print("menu".center(16, "*"))
# print("Hello world".endswith("worlt"))
# print("Hello world".startswith("Hello"))

# print("\u0030²".isdecimal())

# print(string_sample2)
# print(string_sample2.swapcase())

# print("12315678".zfill(8))

# print("123".rjust(8, "0"))

# salary = 1000
# name = 'John'
# string = '{0}s salary is {1}, {0} {0}, {1} {1}'

# print(string.format(name, salary))

# price = 1000
# product = "computer"

# string = "This {product} costs {price:.2f}$."

# print(string.format(product=product, price=price))

# x = 12231.3456789
# y = 131.1314
# print('The value of x is %.4f' % x)
# print('The value of y is %.2f' % y)

# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500

# emp_string = 'Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' % {'name': emp_name, 'salary': emp_salary, 'age': emp_age}
# print(emp_string)

name = "jack"
salary = 2000
age = 30

# print(f'{name.title()}s salary is {salary:.2f}$. {name.title()} is {age} years old!')
print(r'\n\t\\\'')

print(r'C:\Users\new folder\ ')