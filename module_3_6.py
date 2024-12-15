def wat(data_structure):
    summ = 0
    if isinstance(data_structure, dict):
        for k, v in data_structure.items():
            if isinstance(k, int):
                summ += k
            elif isinstance(k, str):
                summ += len(k)
            if isinstance(v, int):
                summ += v
            elif isinstance(v, str):
                summ += len(v)
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            summ += wat(i)
    elif isinstance(data_structure, (int, float)):
            summ += data_structure
    elif isinstance(data_structure, str):
            summ += len(data_structure)
    return summ

data_structure = [[1, 2, 3],
                {'a': 4, 'b': 5},
                 (6, {'cube': 7, 'drum': 8}),
                'Hello',
                ((), [{(2, 'Urban', ('Urban2', 35))}])]

print(wat(data_structure))