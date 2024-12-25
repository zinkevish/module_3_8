data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "123",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(args):
    total_sum = 0

    for arg in args:
        if isinstance(arg, (int, float)):                       # Если это число
            total_sum += arg
        elif isinstance(arg, (list, tuple, set)):               # Если это список, кортеж или множество
            total_sum += calculate_structure_sum(arg)           # Рекурсия для вложенных элементов
        elif isinstance(arg, dict):                             # Если это словарь
            total_sum += calculate_structure_sum(arg.values())  # Рекурсия для значений словаря
        elif isinstance (arg, str):                             # Если это строка
            total_sum += len (arg)

    return total_sum

result = calculate_structure_sum(data_structure)
print(result)
