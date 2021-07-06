def triple_trouble(one, two, three):
    result_str = ''
    for char in range(0, len(one)):
        result_str += one[char] + two[char] + three[char]
    return result_str