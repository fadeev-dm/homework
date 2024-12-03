def print_params(a = 1, b = 'строка', c = True):
     print(a, b, c)


values_list = [2.5 , 'Dmitriy', False]
values_dict = {'a': 3, 'b': 'Pavel', 'c': 8.5}
values_list_2 = [True, 'Anton']

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)