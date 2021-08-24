def name_value(my_list):
    result = []
    for i in range(len(my_list)):
        total = 0
        for j in range(len(my_list[i])):
            if my_list[i][j] == ' ':
                pass
            else:
                total += (ord(my_list[i][j])-96)
        result.append(total*(i+1))
    return result