def char_concat(word):
    result = ""
    for i in range(len(word) // 2):
        result += word[i] + word[-i - 1] + str(i + 1)
    return result
