import functools

def numbers_with_digit_inside(x,d):
    temp1 = []
    temp2 = []
    for i in range(1,x+1):
        temp1.append(str(i))
    for elem in temp1:
        if str(d) in elem:
            temp2.append(int(elem))
    try:
        mul = functools.reduce(lambda x,y: x*y, temp2)
    except:
        mul = 0
    return [len(temp2), sum(temp2),mul]