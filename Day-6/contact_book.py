# Contact Book Storage System

import csv
import json
import os

TXT_FILE = "contacts.txt"
CSV_FILE = "contacts.csv"
JSON_FILE = "contacts.json"


def get_contact_details():
    print()
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    addr = input("Enter Address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": addr
    }
    return contact


# -- txt --

def save_to_txt(contact):
    with open(TXT_FILE, "a") as f:
        f.write(f"Name: {contact['name']}\n")
        f.write(f"Phone: {contact['phone']}\n")
        f.write(f"Email: {contact['email']}\n")
        f.write(f"Address: {contact['address']}\n")
        f.write("-" * 30 + "\n")
    print("Saved to txt.")


def read_txt():
    if not os.path.exists(TXT_FILE):
        print("No txt file found.")
        return

    with open(TXT_FILE, "r") as f:
        print(f.read())


# -- csv --

def save_to_csv(contact):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:
        # looked up DictWriter, this is how it works apparently
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "address"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(contact)

    print("Saved to csv.")


def read_csv():
    if not os.path.exists(CSV_FILE):
        print("No csv file found.")
        return

    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['name']} | {row['phone']} | {row['email']} | {row['address']}")


# -- json --

def save_to_json(contact):
    contacts = []

    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            contacts = json.load(f)

    contacts.append(contact)

    with open(JSON_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

    print("Saved to json.")


def read_json():
    if not os.path.exists(JSON_FILE):
        print("No json file found.")
        return

    with open(JSON_FILE, "r") as f:
        contacts = json.load(f)

    for c in contacts:
        print(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}")


# update only in json, easier to work with than txt or csv
def update_contact():
    if not os.path.exists(JSON_FILE):
        print("No contacts found.")
        return

    search = input("Enter name to update: ").strip().lower()

    with open(JSON_FILE, "r") as f:
        contacts = json.load(f)

    found = False
    for c in contacts:
        if c["name"].lower() == search:
            print("Found contact. Press Enter to keep existing value.")

            new_phone = input(f"New Phone [{c['phone']}]: ").strip()
            new_email = input(f"New Email [{c['email']}]: ").strip()
            new_addr  = input(f"New Address [{c['address']}]: ").strip()

            if new_phone:
                c["phone"] = new_phone
            if new_email:
                c["email"] = new_email
            if new_addr:
                c["address"] = new_addr

            found = True
            print("Updated!")
            break

    if not found:
        print("Contact not found.")
        return

    with open(JSON_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


# main menu
while True:
    print()
    print("=== Contact Book ===")
    print("1. Add contact")
    print("2. View TXT")
    print("3. View CSV")
    print("4. View JSON")
    print("5. Update contact")
    print("6. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        contact = get_contact_details()
        save_to_txt(contact)
        save_to_csv(contact)
        save_to_json(contact)

    elif choice == "2":
        read_txt()

    elif choice == "3":
        read_csv()

    elif choice == "4":
        read_json()

    elif choice == "5":
        update_contact()

    elif choice == "6":
        print("Bye!")
        break

    else:
        print("Invalid option.")