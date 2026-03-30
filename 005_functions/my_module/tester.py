
# def say_hello():
#     print('Hello world!')


# print(say_hello())


# def say_hello():
#     return 'Hello world!'


# print(say_hello())

# x = say_hello()
# print(x)


# def say_hello(name):
#     if name:
#         print(f'Hello {name}')
#     else:
#         print('Hello stranger')

# say_hello('')
# say_hello('Roman')


# def create_greeting(name):
#     if not name:
#         return
#     return f'Hello {name}'


# print(create_greeting(''))
# print(create_greeting('Roman'))


# def more_params(fullname):
#     name, surname = fullname
#     print(f'Hello {name} {surname}')


# more_params(['Jack', 'Smith'])

# def default_values(a=0, b=0, c=0):  # a, b are required positional arguments, c - optional
#     print('A', a)
#     print('B', b)
#     print('C', c)
#     print(a + b + c)


# default_values()

# def args_func(*args, a, b, c=0):
#     result = 0
#     # for num in args:
#     #     result += num
#     print(args)

#     print('A', a)
#     print('B', b)
#     print('C', c)
#     print('Result:', result)


# x = [4, 5, 6, 7, 8, 9, 10, 1, 20, 32, 5423,]
# args_func(2, 3, *x, 10, 20, 30, 40, c=200, a=300, b=400,)


# def kwargs_func(a, b, c=0, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(a, b, c)

# kwargs_func(10, 20, 30, 40, 50, 60, 70, name='Jack', surname='Smith', age=15)

# a, b, c = 10, 20, 30

# def local_visibility():
#     global c
#     a, b = 1, 2
#     c = 10
#     print('Local', a, b, c)


# local_visibility()
# print('Global', a, b, c)


# def outer_func():

#     def inner_func():
#         print('Inner func: ')

#     print('Outer func: ')


# x, y = 10, 20

# def find_and_print_rect_area(a, b):
#     x, y = 100, 200
#     print('Outer', x, y)
#     def area():
#         x, y = 1000, 2000
#         print('Inner', x, y)
#         return a * b

#     print(f'Area of Rectangle with sides {a}mm and {b}mm:')
#     print(f'{area()}mm2')


# print('Global', x, y)
# find_and_print_rect_area(10, 20)


# def callback():
#     print('Hello world!')


# def logger(func):
#     print('Starting')
#     func()
#     print('Ending')


# logger(callback)

# def test():
#     callback()

# test()

# import my_module

# print(my_module.PI)
from .imports import PI, say_hello as greet
x = 10

print(PI)
greet('Jack')