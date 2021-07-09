def to_freud(sentence =''):
    result = ''
    s = sentence.split()
    for word in s:
        result += 'sex '
    return result[:-1]