def is_anagram(test, original):
    t = ''.join(sorted(list(test.lower())))
    o = ''.join(sorted(list(original.lower())))
    return t == o