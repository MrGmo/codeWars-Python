def is_ruby_coming(lst):
    for elem in lst:
        dev = elem['language']
        if dev == 'Ruby':
            return True
    return False