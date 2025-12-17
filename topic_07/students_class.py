class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

students = [
    Student("Steave", 20),
    Student("Alikse", 19),
    Student("Denys", 21)
]

sorted_by_name = sorted(students, key=lambda s: s.name)
print("Sorted by name:")
for s in sorted_by_name:
    print(s)

sorted_by_age = sorted(students, key=lambda s: s.age)
print("Sorted by age:")
for s in sorted_by_age:
    print(s)
