def split_in_parts(s,part):
    result = ''
    for i in range(0,len(s),part):
        result += s[i:i+part] + ' '
    return result[:-1]