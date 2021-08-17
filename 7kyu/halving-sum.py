def halving_sum(n):
    divs = [n]
    while n > 0:
        divs.append(n//2)
        n = n//2
    return sum(divs)