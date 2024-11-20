# Работа со словарями
my_dict = {'Ford' : 1998, 'Nissan' : 2001, 'Opel' : 2003, 'Lada' : 2005}
print(my_dict)
print(my_dict.get('Opel')) # Вывод значения из словаря по ключу
print(my_dict.get('BMW')) # Вывод несуществующего значения из списка
my_dict.update({'Mercedes' : 1996, 'Porsche' : 1995}) # Добавление двух пар в словарь
deleted_valuemy = my_dict.pop('Lada') # Присвоение переменной удаленной пары
print(deleted_valuemy) # Вывод удаленного значения
print(my_dict)

# Работа со множествами
my_set = {True, 'Lada', 2.5, True, 'Lada', 3}
print(my_set)
my_set.update((False, 'Opel')) # Добавление значений во множество
my_set.remove('Lada') # Удаление элемента из множества
print(my_set)