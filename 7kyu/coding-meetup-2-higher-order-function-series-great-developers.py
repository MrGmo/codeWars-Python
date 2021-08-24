def greet_developers(lst):
    for elem in lst:
        name = elem['firstName']
        lang = elem['language']
        elem['greeting'] = f'Hi {name}, what do you like the most about {lang}?'
    return lst
    