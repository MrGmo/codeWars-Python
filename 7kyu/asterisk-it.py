def asterisc_it(n):
    new_str = ""
    result = ""
    if type(n) == list:
        for num in n:
            new_str += str(num)
    elif type(n) == int:
        for num in str(n):
            new_str += str(num)
    else:
        for char in n:
            new_str += char
    for i in range(len(new_str) - 1):
        if int(new_str[i]) % 2 == 0 and int(new_str[i + 1]) % 2 == 0:
            result += new_str[i] + "*"
        else:
            result += new_str[i]
    return result + new_str[-1]
