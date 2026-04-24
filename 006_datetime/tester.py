import datetime as dt


# d = dt.date(2022, 4, 5)

# # print(d)
# # print(repr(d))
# # print(type(d))

# today = dt.date.today()

# # print(today.year)

# # print(today.weekday())  # mon-0, sun-6
# # print(today.isoweekday())

# # if today.weekday() in [5, 6]:
# #     print('It is a weekend')

# # diff = today - d
# # print(diff)
# # print(type(diff))

# # # date1 - date2 = timedelta
# # # date2 + timedelta = date1
# # # date1 - timedelta = date2


# # print(diff.total_seconds())

# # print(126230400 / 60 / 60 / 24)

# tdelta = dt.timedelta(days=3, hours=12)

# print(today + tdelta)

# t = dt.time(14, 23, 10)
# print(t)
# print(type(t))

# t2 = dt.time(21, 13, 56)
# print(t2 + dt.timedelta(hours=10))


dtime = dt.datetime(2024, 10, 6, 14, 31, 25)
print(dtime)
print(type(dtime))

# date_obj = dtime.date()
# time_obj = dtime.time()

# print(date_obj)
# print(type(date_obj))
# print(time_obj)
# print(type(time_obj))

now = dt.datetime.now()
# print(now)
# print(now - dtime)

# tdelta = dt.timedelta(days=4, hours=7)
# print(now + tdelta)

# print(now.timestamp())

# ts = 1775398607.437432

# print(dt.datetime.fromtimestamp(ts))

# d = '2027-03-16'

# bday = dt.datetime.strptime(d, '%Y-%m-%d')
# print(bday)

# now_str = now.strftime('%H:%M:%S')
# print(now_str)

# date_str = "7 June 2026"
# print(dt.datetime.strptime(date_str, '%d %B %Y'))


# def translate_date(date_str: str) -> str:
#     translation = {
#         'Января': 'January',
#         'Марта': 'March',
#     }
#     for val in translation.keys():
#         if val in date_str:
#             date_str = date_str.replace(val, translation[val])
#     return date_str

# cyrillic_str = "24 Марта 2021"
# print(dt.datetime.strptime(translate_date(cyrillic_str), '%d %B %Y'))

# print(translate_date(cyrillic_str))


people = [
    {
        'name': 'Jack',
        'surname': 'Smith',
        'dob': '01.11.1990',
    },
        {
        'name': 'Mary',
        'surname': 'Gold',
        'dob': '22.05.1998',
    }
]

def convert_to_date(date_str):
    result = dt.datetime.strptime(date_str, '%d.%m.%Y')
    return result


def till_next_bday(bdt):
    now = dt.datetime.now()
    day, month, year = bdt.day, bdt.month, bdt.year
    next = dt.datetime(now.year, month, day)
    if now > next:
        next = dt.datetime(now.year + 1, month, day)
    print(f'Next birthday in {(next - now).days} days.')
    print(f'You will turn {next.year - year} years')

# till_next_bday(dt.datetime(1988, 3, 16))
for person in people:
    till_next_bday(convert_to_date(person['dob']))


actors = [
    ('1', 'PENELOPE', 'GUINESS', datetime.datetime(2006, 4, 30))
]