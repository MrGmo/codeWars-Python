def initials(name):
    result = ''
    name_list = name.title().split(' ')
    for i in range(len(name_list)):
        if name_list[i] != name_list[-1]:
            result += name_list[i][0] + '.'
        else:
            result += name_list[i]
    return result
   