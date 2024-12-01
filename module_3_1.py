calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    len_string = len(string)
    string_upper = string.upper()
    string_lower = string.lower()
    return len_string, string_upper, string_lower


def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = []
    for i in list_to_search:
        list_lower.append(i.lower())
    return string_lower in list_lower


print(string_info('ДМИТРий'))
print(string_info('Павел'))
print(is_contains('Дмитрий', ['Трий', 'Дима', 'ДМИТРИЙ']))
print(is_contains('Павел', ['Паша', 'ПАШКА']))
print(calls)