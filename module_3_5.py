def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        next_number = int(str_number[1:])
        if next_number != 0:
            return first*get_multiplied_digits(next_number)
        else:
            return first
    else:
        return first

print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))
