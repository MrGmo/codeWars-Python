def word_pattern(word):
    result = "0"
    word = word.lower()
    a = list(set(word))
    a.sort(key=word.index)
    if len(word) == 0:
        return ""
    else:
        for i in range(1, len(word)):
            result += "." + str(a.index(word[i]))
    return result
