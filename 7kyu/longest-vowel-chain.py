def solve(s):
    total = 0
    temp = 0
    for char in s:
        if char in 'aeiou':
            temp += 1
            if temp > total:
                total = temp
        else:
            temp = 0
    return total