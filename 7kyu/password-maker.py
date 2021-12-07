def make_password(phrase):
    p = ''.join([x[0] for x in phrase.split(' ')])
    result_str = ''
    word_dict = {
        'O': '0',
        'o': '0',
        'I': '1',
        'i': '1',
        'S': '5',
        's': '5'
    }
    for char in p:
        if char in word_dict:
            result_str += word_dict.get(char)
        else:
            result_str += char
    return result_str