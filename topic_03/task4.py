def find_insert_position(sorted_list, value):
    for i, elem in enumerate(sorted_list):
        if value < elem:
            return i
    return len(sorted_list)

sorted_list = [1, 3, 5, 7, 9]
value = 6
position = find_insert_position(sorted_list, value)
print(f"Позиція для вставки {value}: {position}")
