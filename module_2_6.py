while True:
    number = int(input('Ведите число от 3 до 20: '))
    if number < 3 or number > 20:
        print('Введите число в заданном диапазоне!')
    else:
        result = []
        for i in range(1,21):
            for j in range(i+1,21):
                if number % (i + j) == 0:
                    result.append(i)
                    result.append(j)
        print(*result, sep = '')