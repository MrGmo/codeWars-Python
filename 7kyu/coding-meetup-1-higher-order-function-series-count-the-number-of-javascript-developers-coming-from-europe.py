def count_developers(lst):
    js_devs = 0
    for elem in lst:
        if elem['continent'] == 'Europe' and elem['language'] == 'JavaScript':
            js_devs += 1
    return js_devs