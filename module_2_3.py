my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start_list = 0
while start_list < len(my_list):
    if my_list[start_list] < 0:
        break
    if my_list[start_list] > 0:
        print(my_list[start_list])
    start_list += 1





