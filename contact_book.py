import json

# The name of the file where we will save our contacts
FILENAME = 'contacts.json'

# 1. Function to load contacts from the file 
def load_contacts():
    try: 
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # if the file doesn't exist yet, return an empty list
        return[]

# 2. Function to save contacts to the file
def save_contacts(contacts):
    with open(FILENAME, 'w') as f:
        json.dump(contacts, f, indent=4) # indent=4 makes the file readable

# 3. Function to add a contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    new_contact = {"name": name, "phone": phone}
    contacts.append(new_contact)
    save_contacts(contacts) # save it immidiately to the file!
    print(f"contact '{name}' added successfully")

# 4. function to view contacts
def view_contacts(contacts):
    if not contacts: # checks if the list is empty
        print("Your book is empty.")
    else:
        print("\n--- Your Contacts ---")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")


if __name__ == "__main__":
    # start by loadin the contacts 
    my_contacts = load_contacts()
    print(f"Loaded {len(my_contacts)} contacts.")

while True:
    print("\n--- Contact Book ---")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Quit")

    choice = input("Entre your choice (1-3)")

    if choice == '1':
        # We will write the view function next!
        view_contacts(my_contacts)
    elif choice == '2':
        # We will write te add function next!
        add_contact(my_contacts)
    elif choice == '3':
        print("Goodbye!")
        break 
    else: 
        print("Invalid choice. please try again.")
