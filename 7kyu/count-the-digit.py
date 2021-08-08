def nb_dig(i,d):
    sqrs = []
    count = 0
    for i in range(0,i+1):
        sqrs.append(str(i**2))
    for char in sqrs:
        if str(d) in char:
            count += char.count(str(d))
    return count