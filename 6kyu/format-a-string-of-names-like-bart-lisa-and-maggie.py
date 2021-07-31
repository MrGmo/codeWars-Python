def namelist(names):
    name_list = []
    result = ''
    if len(names) == 0:
        return result
    if len(names) == 1:
        return names[0].get('name')
    for n in names:
        name_list.append(n.get('name'))
    while len(name_list) > 1:
        result += name_list.pop(0) + ', '
    return result[:-2] + ' & ' + name_list[-1]