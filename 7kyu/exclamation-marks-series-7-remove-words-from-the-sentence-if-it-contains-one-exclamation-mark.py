def remove(s):
    result = ""
    for word in s.split():
        if word.count("!") == 1:
            pass
        else:
            result += word + " "
    return result[:-1]
