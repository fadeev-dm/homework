grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny',
            'Bilbo',
            'Steve',
            'Khendrik',
            'Aaron'}
grades_average = [] # Создание пустого списка
for i in grades: # Добавление цикла
    grades_average.append(sum(i) / len(i)) # Добавление в новый список средних значений из списка списков grades
students_list = list (students) # Перевод множества в список
students_list_alphabet = sorted(students_list) # Отсортировка списка в алфовитном порядке
grades_students = dict(zip(students_list_alphabet, grades_average)) # Объединяем списки с помощью команды zip() и преобразовываем в словарь с помощью команды dict()
print(grades_students)
