def calc(x):
    total = 0
    count1 = ''
    for char in x:
        count1 += str(ord(char))
    count2 = count1.replace('7','1')
    long_num = str(int(count1)-int(count2))
    for num in long_num:
        total += int(num)
    return total