def spin_words(sent):
    s = sent.split()
    return ' '.join(map(lambda x: x[::-1] if len(x) > 4 else x, s))