# from ipaddress import summarize_address_range
#
# data_structure = [
#
#   [1, 2, 3],
#
#   {'a': 4, 'b': 5},
#
#   (6, {'cube': 7, 'drum': 8}),
#
#   "Hello",
#
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
#
# ]
# def calculate_structure_sum (*args):
#     sum_= 0
#
#     for i in data_structure:
#         if isinstance (i,(int, float)):
#             sum_+=i
#
#         elif isinstance(i, (list, tuple, set)):
#             sum_ += i
#
#
#
# calculate_structure_sum()
# print(sum_)
# # result = calculate_structure_sum(data_structure)
# # print(result)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(data_structure, type(data_structure))

def calculate_structure_sum(*args):
    total_sum = 0

    for arg in args:
        if isinstance(arg, (int, float)):  # Если это число
            total_sum += arg
        if isinstance(arg, (list, tuple, set)):  # Если это список, кортеж или множество
            total_sum += calculate_structure_sum(*arg)  # Рекурсия для вложенных элементов
        if isinstance(arg, dict):  # Если это словарь
            total_sum += calculate_structure_sum(*arg.values())  # Рекурсия для значений словаря
        

    return total_sum


result = calculate_structure_sum(data_structure)
print(result)