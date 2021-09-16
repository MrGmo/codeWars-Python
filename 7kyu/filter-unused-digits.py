def unused_digits(*n):
    n = sorted(list(map(int,list(set(sorted(list(''.join(list(map(str, n))))))))))
    result = ''
    for i in range(10):
        if i not in n:
            result += str(i)
    return result