def count_char(s,char):
    count = 0
    s = s.lower()
    char = char.lower()
    for x in s:
        if x == char:
            count += 1
    return count