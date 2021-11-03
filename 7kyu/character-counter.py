def validate_word(word):
    word = word.lower()
    dict = {}
    for char in word:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    dict_values = list(dict.values())
    return all(x == dict_values[0] for x in dict_values)