contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully!")

def view_contacts():
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(name):
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name of the contact to edit: ")
        edit_contact(name)
    elif choice == '4':
        name = input("Enter name of the contact to delete: ")
        delete_contact(name)
    elif choice == '5':
        break
    else:
        print("Invalid choice! Please try again.")
