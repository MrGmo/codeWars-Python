def vowel_2_index(st):
    result = ''
    for i in range(len(st)):
        if st[i] in 'aeiouAEIOU':
            result += str(i+1)
        else:
            result += st[i]
    return result