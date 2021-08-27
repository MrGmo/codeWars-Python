def jumping_number(num):
    n = list(map(int,list(str(num))))
    if len(n) == 1:
        return 'Jumping!!'
    for i in range(len(n)-1):
        if n[i]+1 == n[i+1] or n[i]-1 == n[i+1]:
            pass
        else:
            return 'Not!!'
    return 'Jumping!!'