# empty = {}
# empty = dict()

# print(type(empty))

# example = {
#     "name": "Jack",
#     "nickname": "Jack",
#     "courses": ['English', 'Math', 'Art'],
#     "number": 123,
#     "boolean": True,
#     "dictionary": {
#         "eye_color": "brown",
#         "height": 175
#     },
#     1: 'one',
#     0.5: 'half',
#     True: 'True value',
#     (1, 2, 3): 'set'
#     }

# print(example['courses'][1])
# print(example['dictionary']['eye_color'])
# print(example[(1, 2, 3)])

# print(example.get('name', []))
# example['name'] = 'Mary'
# example['phone'] = '555-555-5555'
# print(example)

# example.update({'name': 'Bob', 'surname': 'Smith'})
# print(example)

# surname = example.pop('name')
# print(surname)
# print(example)
# print(example.popitem())

# del example['name']
# print(len(example))


# print(dict([['one', 1], ['two', 2], ['three', 3]]))
# # print(list(example))
# print(example.keys())
# print(example.values())
# print(example.items())

# a = 7
# b = 10

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# print('123' == 123)
# print(ord('A'))
# print(chr(121))
# print('hello' > 'hellO')
# print([1, 2, 3] == [1, 2, 3])

# print(0 < a < 15)
# print(True and False)
# print(False or True)
# print(True and False or True)
# print(not False)

# print(4 not in [1, 2, 3])

# code = '3880316027'
# if len(code) == 11:
#     print(f'Your code is {code}')
# elif len(code) > 11:
#     print('Your code is too long')
# else:
#     print('Your code is too short')

# age = 26
# if age < 12 and age > 0:
#     print('Child')
# elif age <= 18:
#     print('Teenager')
# elif age <= 65:
#     print('Adult')
# elif age <= 120:
#     print('Senior')
# else:
#     print('Wrong input!')

# code = '38803160272'
# if len(code) == 11:
#     print(f'Your code is {code}')
# else:
#     if len(code) > 11:
#         print('Your code is too long')
#     else:
#         print('Your code is too short')

# name = input('Enter name: ')
# if name:
#     print(f'Hello {name}')
# else:
#     print('Hello stranger')


# print(list(range(1, 10)))
# print([*range(10)])
# print(*range(10, -10, -2))

# for num in range(10):
#     print(f'Number: {num}, Square: {num ** 2}')

# names = ['Jack', 'Mary', 'Bob', 'Jessica', 'Simon']
# for name in names:
#     if len(name) > 4:
#         print(f'Hello {name}. You have a long name')
#     else:
#         print(f'Hello {name}. You have a short name')

# people = [
#     {
#         'name': 'Jack',
#         'surname': 'Smith',
#         'salary': 2000
#     },
#     {
#         'name': 'Mary',
#         'surname': 'Gold',
#         'salary': 4000
#     },
#     {
#         'name': 'Bob',
#         'surname': 'Dylan',
#         'salary': 3000
#     }
# ]

# for person in people:
#     if person['name'] == 'Jack':
#         continue
#     elif person['name'] == 'Mary':
#         break
#     print(f'Hello {person['name']} {person['surname']}. Your salary is {person['salary']:.2f}$')

# print('Good bye!')

# for num1 in range(10):                  # 10
#     for num2 in range(10):              # 10 * 10 = 100
#         for num3 in range(10):          # 10 * 100 = 1000
#             for num4 in range(10):      # 10 * 1000 = 10000
#                 print(num1, num2, num3, num4)

# squares = []
# for x in range(1000000):
#     print(x ** 2)
#     # squares.append(x ** 2)


# print(99 % 2 == 0)


# sentence = 'Hello people of planet Earth'

# counts = {}

# for letter in set(sentence):
#     counts[letter] = sentence.count(letter)


# max_count = max(counts.values())

# result = []
# for key, value in counts.items():
#     if value == max_count:
#         result.append(key)


# print(result)
# condition = True

# while condition:
#     user_input = input("Enter your name: ")

#     if user_input:
#         print('Hello ' + user_input)
#         condition = False
#     else:
#         print('Name must not be empty')


# while True:
#     user_input = input("Enter your name: ")

#     if not user_input:
#         print('Name must not be empty')
#         continue

#     print(f'User entered name: {user_input}')
#     break

# for letter in 'python13':

#     if letter == 'h':
#         continue
#     elif letter == 'n':
#         break
#     print(letter)

import time

# while True:

#     user_choice = input('Choose number:\n' \
#                         '1.Say Hello\n' \
#                         '2.Joke\n' \
#                         '3.Exit\n' \
#                         '-> ')
    
#     if user_choice == '1':
#         while True:
#             user_name = input('Please enter name or X for exit: ')
#             if not user_name:
#                 print('Must enter something!')
#                 continue
#             elif user_name.lower() == 'x':
#                 exit()
#             print(f'Hello {user_name.title()}')
#             time.sleep(2)
#             break

# entering_name = True      
# while entering_name:

#     user_choice = input('Choose number:\n' \
#                         '1.Say Hello\n' \
#                         '2.Joke\n' \
#                         '3.Exit\n' \
#                         '-> ')
    
#     if user_choice == '1':
#         while entering_name:
#             user_name = input('Please enter name or X for exit: ')
#             if not user_name:
#                 print('Must enter something!')
#                 continue
#             elif user_name.lower() == 'x':
#                 entering_name = False
#                 break
#             print(f'Hello {user_name.title()}')
#             time.sleep(2)
#             break

# while True:
#     print('Enter Estonian national ID or type "exit" to quit.')
#     isikukood = input("-> ")
#     if isikukood.lower() == 'exit':
#         print('Good bye')
#         break
#     try:
#         int(isikukood)
#         # 1/0
#         if len(isikukood) != 11:
#             raise UserWarning
#     except ValueError:
#         print("Code you entered is not numeric")
#         continue
#     except UserWarning:
#         print(f'Isikukood is too {'long' if len(isikukood) > 11 else 'short'}')
#         continue
#     else:
#         print(f'{isikukood} is registered.')
#     finally:
#         print('finally block')
#     break

# for num in range(11):
#     print(num)
#     if num == 10:
#         print('OK')
#         break
# else:
#     print('Not found')

# users = ['alice', 'bob', 'mary', 'charlie']

# for user in users:
#     if user == 'mary':
#         print('Found')
#         break
# else:
#     print('Not found')

# n = 3

# while n > 0:
#     print(n)
#     n -= 1
# else:
#     print('Finished')


# n = 3
# while n > 0:
#     print(n)
#     if n == 2:
#         break
#     n -= 1
# else:
#     print('Finished')

import time

t = time.localtime()
# print(time.localtime())



# time.struct_time(tm_year=2026, tm_mon=3, tm_mday=22, tm_hour=18, tm_min=58, tm_sec=8, tm_wday=6, tm_yday=81, tm_isdst=0)