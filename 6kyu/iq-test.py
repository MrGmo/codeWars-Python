def iq_test(numbers):
    s = [int(x) for x in numbers.split()]
    odds = []
    evens = []
    for i in range(0,len(s)):
        if s[i] % 2 == 0:
            evens.append(i+1)
        else:
            odds.append(i+1)
    return odds[0] if len(odds) < len(evens) else evens[0]