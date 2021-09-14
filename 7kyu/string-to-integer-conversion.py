def my_parse_int(string):
    s = string.strip()
    if s.isdigit():
        return int(s)
    return 'NaN'