def even_or_odd(s):
    even = 0
    odd = 0
    s = list(map(int,list(s)))
    for num in s:
        if num % 2 == 0:
            even += num
        else:
            odd += num
    if even == odd:
        return 'Even and Odd are the same'
    return 'Even is greater than Odd' if even > odd else 'Odd is greater than Even'