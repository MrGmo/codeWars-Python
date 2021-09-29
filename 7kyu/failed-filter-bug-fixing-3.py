def filter_numbers(string):
    return ''.join([x for x in list(string) if not x.isdigit()])