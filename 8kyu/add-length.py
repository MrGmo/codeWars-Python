def add_length(s):
    result = []
    arr = s.split()
    for word in arr:
        result.append(word + ' ' + str(len(word)))
    return result