def arithmetic_sequence_elements(a,r,n):
    result = []
    for i in range(a,n+a):
        result.append(a)
        a += r
    return ', '.join(list(map(str,result)))