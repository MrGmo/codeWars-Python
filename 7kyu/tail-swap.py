def tail_swap(s):
    result = []
    for char in s:
        char = char.split(':')
        result.append(char)
    return [''.join(result[0][0]+ ':' + result[1][1]),''.join(result[1][0]+ ':' + result[0][1])]