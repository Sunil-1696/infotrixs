import csv

CONTACTS_FILE = "contacts.csv"
CONTACTS_FIELDNAMES = ["Name", "Phone"]

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            reader = csv.DictReader(file)
            return [contact for contact in reader]
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CONTACTS_FIELDNAMES)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts, name, phone):
    for contact in contacts:
        if contact["Name"] == name:
            print("Contact already exists.")
            return

    new_contact = {"Name": name, "Phone": phone}
    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts, name):
    for contact in contacts:
        if contact["Name"] == name:
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            return

    print("Contact not found.")

def update_contact(contacts, name):
    for contact in contacts:
        if contact["Name"] == name:
            print("Enter new phone number (leave blank to keep existing):")
            new_phone = input()
            contact["Phone"] = new_phone if new_phone else contact["Phone"]
            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")

def menu():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter contact details:")
            name = input("Name: ")
            phone = input("Phone: ")
            add_contact(contacts, name, phone)
        elif choice == "2":
            name = input("Enter the name to search: ")
            search_contact(contacts, name)
        elif choice == "3":
            name = input("Enter the name to update: ")
            update_contact(contacts, name)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
