def number(lines):
    result = []
    for x in enumerate(lines,start=1):
        result.append(f'{x[0]}: {x[1]}')
    return result