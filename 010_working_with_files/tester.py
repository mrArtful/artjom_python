# r - read
# w - write (creates if don't exist)
# a - append (creates if don't exist)
# x - create
# r+ - read and write

# with open(r"./010_working_with_files/message.txt", "r", encoding="utf8") as file:
#     data = file.read()

# with open(r"./010_working_with_files/message.txt", "w", encoding="utf8") as file:
#     file.write(data.upper())


# with open(r"./010_working_with_files/message.txt", "r", encoding="utf8") as file:
#     data = file.read(10)
#     print(data)
#     file.seek(0)
#     data = file.read(10)
#     print(data)

# with open(r"./010_working_with_files/people.json", "r") as file:
#     data = file.read()
#     print(data)
#     print(type(data))

import json

# with open(r"./010_working_with_files/people.json", "r") as file:
#     data = json.load(file)

# new_data = list(filter(lambda p: p['has_licence'] == True, data['people']))
# print(new_data)

# with open(r"./010_working_with_files/new_people.json", "w") as file:
#     json.dump(new_data, file, indent=2)

# json_str = '''{
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false,
#       "salary": 1500
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true,
#       "salary": 1700
#     },
#     {
#       "name": "Steven Cooke",
#       "phone": null,
#       "emails": "stevencooke@example.com",
#       "has_licence": true,
#       "salary": 2500
#     }
#   ]
# }'''

# data = json.loads(json_str)
# print(data)
# print(type(data))

# new_json_str = json.dumps(data)
# print(new_json_str)
# print(type(new_json_str))



