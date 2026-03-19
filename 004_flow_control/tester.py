# x = 101

# if x < 100:
#     print('X is greater than 100')
# elif x < 200:
#     print('X is less than 200')
# else:
#     print('Else statement')



# print(ord("a"))
# print(chr(97))

# print(True and True)
# print(False or True)
# print(not False)

# x = None
# print(x is None)

# print(bool({}))

# x = [1]
# if x:
#     print('OK')


# isikukood = '38803160272'

# if len(isikukood) == 11:
#     print('OK')
# else:
#     if len(isikukood) < 11:
#         print('too short')
#     else:
#         print('too long')

# text = 'Hello world'

# if 'world' in text:
#     print('OK')

# x = [1, 2, 3]

# print(5 not in x)

# numbers = [0, 0, 0]

# print(any(numbers))
# print(not all(numbers))


# for num in [1, 2, 3, 4]:
#     print(num)

# x = range(-100, 100, 10)

# for num in x:
#     print(num)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mults = [6, 3, 2, 4, 1, 8, 6, 3, 4]

# for index in range(len(nums)):  # 0 - 9
#     print(nums[index] * mults[index])


# x = list(iter([1, 2, 3, 4, 5, 6]))

# for num in x:
#     print('1.', num)

# for num in x:
#     print('2.', num)


# numbers = [20, 30, 40, *range(1, 11)]
# print(numbers)


# people = [
#     ('Jack', 23, 1500),
#     ('Sarah', 32, 2500),
#     ('Martin', 40, 3500),
#     ('Simon', 18, 1200),
#     ('Mary', 25, 2000),
# ]

# for person in people:
#     print(f'{person[0]} is {person[1]} years old. Salary: {person[2]}')


# for name, age, salary in people:
#     print(f'{name} is {age} years old. Salary: {salary}')


# courses = ['English', 'Math', 'Physics', 'Estonian']

# for index, value in enumerate(courses, 1):
#     print(index, value)


# student = {
#     'name': 'Jack',
#     123: 'number',
#     (1, 2): 'tuple',
# }

# print(student[(1, 2)])

x = {
    'make': 'VW',
    'model': 'Golf',
    'info': {
        'mileage': 10000
    }
}

# print(x['info']['mileage'])
# print(x.get('phone', []))

# x['model'] = 'Passat'
# x['phone'] = '555-555-5555'
# print(x)

# x.update(make='BMW', phone='555-555-5555')
# x.update({'make': 'BMW', 'phone': '555-555-5555'})
# print(x)

# info = x.pop('info')
# print(info)
# print(x)

# del x['make']
# print(x)

# print(len(x))

# for key, val in x.items():
#     print(key, val)


# print(x.keys())
# print(x.values())
# print(x.items())

print(list(x.items()))