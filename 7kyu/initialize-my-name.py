def initialize_names(name):
    result = ''
    n = name.split()
    if len(n) <= 2:
        return name
    for i in range(0,len(n)):
        if i == 0:
            result += n[i]
        elif i == len(n)-1:
            result += n[i]
        else:
            result += ' '+n[i][0]+'. '
    return result.replace('  ', ' ')