students = [
    {"name": "Bob",  "phone": "0631234567", "email": "bob@gmail.com",  "address": "Kyiv"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@gmail.com", "address": "Lviv"},
    {"name": "Jon",  "phone": "0631234567", "email": "jon@gmail.com",  "address": "Odesa"},
    {"name": "Zak",  "phone": "0631234567", "email": "zak@gmail.com",  "address": "Dnipro"}
]

def printAllList():
    for elem in students:
        strForPrint = f"Name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Address: {elem['address']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")

    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del students[deletePosition]
        print(f"Element with name {name} deleted")
    return

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

    if new_phone.strip():
        found["phone"] = new_phone
    if new_email.strip():
        found["email"] = new_email
    if new_address.strip():
        found["address"] = new_address

    print(f"Data for {name} updated successfully")
    return


def main():
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
                print("Exit()")
                break
            case _:
                print("Wrong choice")


main()
