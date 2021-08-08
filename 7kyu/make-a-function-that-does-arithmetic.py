def arithmetic(a,b,op):
    obj ={
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    return eval(f'{a}{obj.get(op)}{b}')