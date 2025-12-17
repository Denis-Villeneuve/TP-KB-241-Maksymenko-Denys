students = [
    {"name": "ssteave", "grade": 90},
    {"name": "Alikse", "grade": 95},
    {"name": "Denys", "grade": 80}
]

print("Original list:")
print(students)

sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Sorted by name:")
print(sorted_by_name)

sorted_by_grade = sorted(students, key=lambda x: x["grade"])
print("Sorted by grade:")
print(sorted_by_grade)
