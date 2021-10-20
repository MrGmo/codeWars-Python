def freq_seq(s, sep):
    result_str = ''
    s = list(s)
    for char in s:
        result_str += str(s.count(char)) + sep
    return result_str[:-1]