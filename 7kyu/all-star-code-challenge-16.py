def no_repeat(string):
    for char in string:
        if string.count(char) == 1:
            return char
