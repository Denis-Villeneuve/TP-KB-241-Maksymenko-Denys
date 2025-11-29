import csv
from sys import argv

students = []

def load_students_from_csv(file_name):
    global students
    students = []
    try:
        with open(file_name, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append({
                    "name": row["name"],
                    "phone": row["phone"],
                    "email": row["email"],
                    "address": row["address"]
                })
        print(f"Loaded {len(students)} students from {file_name}")
    except FileNotFoundError:
        print(f"File {file_name} not found, starting with empty list")
        students = []


def save_students_to_csv(file_name):
    fieldnames = ["name", "phone", "email", "address"]
    with open(file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            writer.writerow(s)
    print(f"Saved {len(students)} students to {file_name}")


def printAllList():
    for elem in students:
        strForPrint = (
            f"Name: {elem['name']}, "
            f"Phone: {elem['phone']}, "
            f"Email: {elem['email']}, "
            f"Address: {elem['address']}"
        )
        print(strForPrint)


def add_student(name, phone, email, address):
    global students
    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)


def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")

    add_student(name, phone, email, address)
    print("New element has been added")


def delete_student_by_name(name):
    global students
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        return False
    else:
        del students[deletePosition]
        return True


def deleteElement():
    name = input("Please enter name to be deleted: ")
    if delete_student_by_name(name):
        print(f"Element with name {name} deleted")
    else:
        print("Element was not found")


def update_student(name, new_phone=None, new_email=None, new_address=None):
    global students
    found = None
    for item in students:
        if name == item["name"]:
            found = item
            break
    if found is None:
        return False

    if new_phone is not None and new_phone.strip():
        found["phone"] = new_phone
    if new_email is not None and new_email.strip():
        found["email"] = new_email
    if new_address is not None and new_address.strip():
        found["address"] = new_address
    return True


def updateElement():
    name = input("Please enter name to be updated: ")
    found = None
    for item in students:
        if name == item["name"]:
            found = item
            break
    if found is None:
        print("Element was not found")
        return

    print("Leave field empty if you don’t want to change it.")
    new_phone = input(f"Enter new phone (current: {found['phone']}): ")
    new_email = input(f"Enter new email (current: {found['email']}): ")
    new_address = input(f"Enter new address (current: {found['address']}): ")

    update_student(
        name,
        new_phone if new_phone.strip() else None,
        new_email if new_email.strip() else None,
        new_address if new_address.strip() else None
    )

    print(f"Data for {name} updated successfully")


def main():
    if len(argv) < 2:
        print("Usage: python lab2.py csv_file")
        return

    file_name = argv[1]

    load_students_from_csv(file_name)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Saving data and exiting...")
                save_students_to_csv(file_name)
                break
            case _:
                print("Wrong choice")


if __name__ == "__main__":
    main()
