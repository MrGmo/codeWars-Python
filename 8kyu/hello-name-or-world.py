def hello(name = ''):
    if len(name) > 0:
        return f'Hello, {name.capitalize()}!'
    return 'Hello, World!'