def make_string(s):
    result = ''
    s = s.split()
    for word in s:
        result += word[0]
    return result