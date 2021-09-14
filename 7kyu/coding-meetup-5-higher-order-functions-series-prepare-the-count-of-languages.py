def count_languages(lst):
    obj = {}
    for elem in lst:
        lang = elem['language']
        if lang in obj:
            obj[lang] += 1
        else:
            obj[lang] = 1
    return obj