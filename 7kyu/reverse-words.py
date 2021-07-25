def reverse_words(text):
    text = text.replace(' ', '*')
    s = text.split('*')
    return '*'.join([x[::-1] for x in s]).replace('*', ' ')