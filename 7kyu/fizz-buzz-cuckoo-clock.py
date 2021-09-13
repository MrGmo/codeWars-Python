def fizz_buzz_cuckoo_clock(time):
    hr = list(map(int, time.split(':')))[0]
    min = list(map(int, time.split(':')))[1]
    if time == '00:00':
        s = 'Cuckoo ' * 12
        return s[:-1]
    if min == 0:
        if hr <= 12:
            s = 'Cuckoo '* hr
            return s[:-1]
        else:
            s = 'Cuckoo '*(hr-12)
            return s[:-1]
    if min == 30:
        return 'Cuckoo'
    if min % 15 == 0:
        return 'Fizz Buzz'
    if min % 5 == 0:
        return 'Buzz'
    if min % 3 == 0:
        return 'Fizz'
    return 'tick'