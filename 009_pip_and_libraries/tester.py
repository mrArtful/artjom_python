import questionary

# name = questionary.text('What is your name?', validate=lambda name: len(name) > 0, qmark='?', multiline=True, instruction='Hello').ask()
# print(f'Hello {name}')


# password = questionary.password('Enter password:').ask()
# print(password)

# file_path = questionary.path('Choose file: ', complete_style='READLINE_LIKE', only_directories=True).ask()
# print(file_path)

# newsletter = questionary.confirm('Would you like to get news?', auto_enter=False).ask()

# if newsletter:
#     print('You will recieve news!')
# else:
#     print('You will not recieve any news!')

# choice = questionary.select('Choose one: ',
#                             choices=[
#                                 'One',
#                                 'Two',
#                                 'Three',
#                                 'Four'
#                             ],
#                             qmark='😁',
#                             pointer='>>>',
#                             show_selected=True
#                             ).ask()

# print(choice)
# h - left
# j - up
# k - down
# l -right


# raw_select = questionary.rawselect(
#     message="Please choose one: ",
#     choices=[
#                 'One',
#                 'Two',
#                 'Three',
#                 'Four'
#             ],
# ).ask()

# print(raw_select)


# check = questionary.checkbox(
#     'Choose pizza toppings: ',
#     choices=[
#         'Pineapple',
#         'Salami',
#         'Mozarella',
#         'Mushrooms',
#         'Bacon',
#     ],
#     validate=lambda c: len(c) > 0,
#     initial_choice='Bacon'
#     ).ask()

# print(check)


from questionary import Style
import os


my_style = Style(
    [
        ('qmark', 'fg:#FF0000'),
        ('answer', 'bg:#FFFFFF fg:#000000')
    ]
)

cars = [
        'BMW',
        'Audi',
        'Mercedes-Benz',
        'Honda',
        'Toyota',
        'Subaru',
        'Skoda',
    ]
auto = questionary.autocomplete(
    'Choose one car brand: ',
    choices=cars,
    ignore_case=True,
    match_middle=True,
    validate=lambda c: c in cars,
    style=my_style
    ).ask()

os.system('cls' if os.name == 'nt' else 'clear')
print(auto)


