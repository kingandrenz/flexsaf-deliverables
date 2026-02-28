#!/usr/bin/python3
import re

# Student Contact Manager

contacts = {}
emails_set = set()
phones_set = set()

# -------------------------------
# Validation Functions
# -------------------------------
def validate_email(email):
    # Improved regex to allow proper domains like example@gmail.com
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email.strip())

def validate_phone(phone):
    return phone.isdigit() and 11 <= len(phone) <= 14

# -------------------------------
# Contact Management Functions
# -------------------------------
def add_contact():
    uuid = input("Enter Student ID or unique Email (ID): ").strip()
    if uuid in contacts:
        print("A contact with this ID already exists.\n")
        return

    full_name = input("Enter Full Name: ").strip()
    phone = input("Enter Phone number: ").strip()
    email = input("Enter Email: ").strip()
    role = input("Enter Role (Student/Parent/Teacher): ").strip()

    if not validate_email(email):
        print("Invalid email format.\n")
        return

    if not validate_phone(phone):
        print("Invalid phone number.\n")
        return

    if email in emails_set:
        print("This email is already used by another contact.\n")
        return

    if phone in phones_set:
        print("This phone number is already in use by another contact.\n")
        return

    contacts[uuid] = {
        "Full Name": full_name,
        "Email": email,
        "Phone": phone,
        "Role": role
    }
    emails_set.add(email)
    phones_set.add(phone)

    print("\nContact added successfully!\n")

def update_contact():
    uuid = input("Enter ID of a contact to update: ").strip()

    if uuid not in contacts:
        print("Contact not found.\n")
        return

    contact = contacts[uuid]
    print("Leave blank to keep current value.\n")

    new_name = input(f"Full Name ({contact['Full Name']}): ").strip()
    new_email = input(f"Email ({contact['Email']}): ").strip()
    new_phone = input(f"Phone ({contact['Phone']}): ").strip()
    new_role = input(f"Role ({contact['Role']}): ").strip()

    if new_name:
        contact["Full Name"] = new_name

    if new_email:
        if not validate_email(new_email):
            print("Invalid email format.\n")
            return
        if new_email != contact["Email"] and new_email in emails_set:
            print("Email already exists.\n")
            return
        emails_set.discard(contact["Email"])
        emails_set.add(new_email)
        contact["Email"] = new_email

    if new_phone:
        if not validate_phone(new_phone):
            print("Invalid phone number.\n")
            return
        if new_phone != contact["Phone"] and new_phone in phones_set:
            print("Phone number already exists.\n")
            return
        phones_set.discard(contact["Phone"])
        phones_set.add(new_phone)
        contact["Phone"] = new_phone

    if new_role:
        contact["Role"] = new_role

    print("Contact updated successfully!\n")

def delete_contact():
    uuid = input("Enter ID of the contact you want to delete: ").strip()

    if uuid not in contacts:
        print("Contact not found.\n")
        return

    email = contacts[uuid]["Email"]
    phone = contacts[uuid]["Phone"]

    emails_set.discard(email)
    phones_set.discard(phone)

    del contacts[uuid]

    print("Contact deleted successfully!\n")

def search_contact():
    uuid = input("Enter ID to search: ").strip()

    if uuid in contacts:
        contact = contacts[uuid]
        print("\n--- Contact Found ---")
        for key, value in contact.items():
            print(f"{key}: {value}")
        print()
    else:
        print("Contact not found.\n")

def list_contacts():
    if not contacts:
        print("No available contacts.\n")
        return

    print("\n--- All Contacts ---")
    for uuid, details in contacts.items():
        print(f"\nID: {uuid}")
        for key, value in details.items():
            print(f"{key}: {value}")
    print()

def show_set_operations():
    print("\n--- Set Operation Demo ---")
    example_emails = {"example1@gmail.com", "example2@gmail.com"}

    print("Union:", emails_set.union(example_emails))
    print("Intersection:", emails_set.intersection(example_emails))
    print("Difference:", emails_set.difference(example_emails))
    print()

# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("========= Student Contact Manager =========")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. List All Contacts")
        print("6. Set Operation Demo")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            list_contacts()
        elif choice == "6":
            show_set_operations()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()
