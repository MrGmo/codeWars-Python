def filter_long_words(sen,n):
    s = sen.split()
    return [x for x in s if len(x) > n]
    