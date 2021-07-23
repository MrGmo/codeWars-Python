def to_jaden_case(string):
    new_list = string.split()
    return ' '.join(list(map(lambda x: x[0].upper() + x[1:], new_list)))