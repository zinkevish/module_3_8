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
        if isinstance(arg, (int, float)):  # Если это число
            total_sum += arg
        elif isinstance(arg, (list, tuple, set)):                     # Если это список, кортеж или множество
            total_sum += calculate_structure_sum(arg)                 # Рекурсия для вложенных элементов
        elif isinstance(arg, dict):                                   # Если это словарь
            for key, value in arg.items():                            # Смотрим пары ключ-значение
                if isinstance(key, (int, float)):
                    total_sum += key                                 # Суммируем числовые ключи
                elif isinstance(key, str):
                    total_sum += len(key)                            # Суммируем  длину строки ключа

                if isinstance(value, (int, float)):
                    total_sum += value                               # Суммируем числовые значения
                elif isinstance(value, str):
                    total_sum += len(value)                         # Суммируем длину строки значения
                else:
                    total_sum += calculate_structure_sum([value])  # Рекурсивная обработка сложных значений
        elif isinstance(arg, str):
            total_sum += len(arg)

    return total_sum                                              # Возвращаем значение


result = calculate_structure_sum(data_structure)
print(result)
