numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # создаем пустой список для простых чисел
not_primes = [] # создаем пустой список для не простых чисел
for i in numbers: # перебираем список numbers
    if i == 1: # присваиваем число 1 для его исключения из списков
        continue # пропуск числа 1
    is_prime = True # флаг 1
    for j in range(2, i-1): # перебор делителей для числа i
        if i % j == 0: # условие деления числел без остатка
            is_prime = False # флаг 2
            break # выполнение команды прерывания
    if is_prime: # условие выполнение команды флаг 1
        primes.append(i) # добавление в новый список простых чисел
    else:
        not_primes.append(i) # добавление в новый список не простых чисел
print('Primes:', primes)
print('Not Primes:', not_primes)



