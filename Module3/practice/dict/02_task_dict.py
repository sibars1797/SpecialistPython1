# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]

# TODO: your code here
print(dict(zip(keys, values)))
# Нужно получить словарь:
# {'name': 'Петр', 'surname': 'Первый', 'age': 42, 'rate': 1300}
