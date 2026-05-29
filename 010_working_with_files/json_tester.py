import json

# Read json file
# Write json file
# Add contact
# Remove contact
# View contact
# Update contact
# View contact list

def load_json():
    global contact_book
    try:
        with open("./010_working_with_files/contacts.json", "x") as contact_data:
            contact_data.write("{}")
    except:
        with open("./010_working_with_files/contacts.json", "r") as contact_data:
            contact_book = json.load(contact_data)


def save_json():
    with open("./010_working_with_files/contacts.json", "w") as contact_data:
        json.dump(contact_book, contact_data, indent=4)


def add_contact(name, phone, email=None):
    if name.title() not in contact_book:
        contact_book[name.title()] = {'phone': phone, 'email': email}
        save_json()
        print(f"Contact {name.title()} was added.")
    else:
        print(f"Contact {name.title()} already exists!")


def remove_contact(name):
    if name.title() in contact_book:
        del contact_book[name.title()]
        save_json()
        print(f"Contact {name} was deleted.")
    else:
        print(f"Contact {name} does not exist!")


def update_contact(name, phone=None, email=None):
    data = {}
    if name.title() in contact_book:
        if phone:
            data['phone'] = phone
        if email:
            data['email'] = email
        if data:
            contact_book[name.title()].update(data)
            save_json()
            print(f"Contact {name.title()} was updated.")
        else:
            print("Nothing to update!")
    else:
        print(f"Contact {name.title()} does not exist.")


contact_book = {}

if __name__ == '__main__':
    load_json()

    add_contact('Jack', '555-555-5555', 'jack@example.com')
    add_contact('Mary', '555-444-5555')

    update_contact('Mary')
    update_contact('jack', phone="555-333-1122", email="jack@gmail.com")
    update_contact('bob')