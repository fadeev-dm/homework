def get_matrix(n, m, value): # создаем функцию
    matrix = [] # создаем пустой список
    for i in range(n): # создаем цикл и повторяем n-повторов
        matrix.append([]) # добавляем пустой список в список matrix
        for j in range(m): # создаем цикл и повторяем m-повторов
            matrix[i].append(value) # пополняем пустой список значениями value
    print(matrix) # возвращаем значение переменной matrix
get_matrix(2, 2, 10) # вывод на экран функции




