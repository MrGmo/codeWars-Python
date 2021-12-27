def pak(s):
    s = s.split()
    result = []
    for word in s:
        result.append(word)
        result.append("pak")
    return " ".join(result)[:-4]
