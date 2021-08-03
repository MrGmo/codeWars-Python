def high(s):
    s = s.split()
    max_count = 0
    max_word = ''
    for word in s:
        temp = 0
        for char in word:
            temp += (ord(char)-96)
        if temp > max_count:
            max_count = temp
            max_word = word
        else:
            pass
    return max_word