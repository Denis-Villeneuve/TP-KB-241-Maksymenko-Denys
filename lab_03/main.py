from student import Student
from student_list import StudentList

DATA_FILE = "students.json"

MENU = """
Меню:
1) Показати всіх студентів
2) Додати студента
3) Видалити студента за ім'ям
4) Оновити дані студента
5) Завантажити з файлу
6) Зберегти в файл
0) Вихід
"""


def main():
    sl = StudentList()
    # спробуємо завантажити, якщо файл є
    sl.load_from_file(DATA_FILE)

    while True:
        print(MENU)
        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            for s in sl.list_all():
                print(s)

        elif choice == "2":
            name = input("ПІБ: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            address = input("Адреса: ")
            st = Student(name=name, phone=phone, email=email, address=address)
            sl.add_student(st)
            print("Додано")

        elif choice == "3":
            name = input("Ім'я/ПІБ для видалення: ")
            ok = sl.remove_student_by_name(name)
            print("Видалено" if ok else "Студента не знайдено")

        elif choice == "4":
            name = input("Ім'я/ПІБ для оновлення: ")
            s = sl.find_by_name(name)
            if not s:
                print("Не знайдено")
                continue
            print("Залиште поле порожнім щоб не змінювати")
            phone = input(f"Телефон [{s.phone}]: ") or s.phone
            email = input(f"Email [{s.email}]: ") or s.email
            address = input(f"Адреса [{s.address}]: ") or s.address
            sl.update_student(name, phone, email, address)
            print("Оновлено")

        elif choice == "5":
            path = input(f"Шлях до файлу (за замовчуванням {DATA_FILE}): ") or DATA_FILE
            sl.load_from_file(path)
            print("Завантажено")

        elif choice == "6":
            path = input(f"Шлях до файлу (за замовчуванням {DATA_FILE}): ") or DATA_FILE
            sl.save_to_file(path)
            print("Збережено")

        elif choice == "0":
            print("До побачення")
            break

        else:
            print("Невірна команда")


if __name__ == "__main__":
    main()