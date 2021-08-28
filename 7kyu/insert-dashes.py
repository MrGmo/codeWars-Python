def insert_dash(num):
    n = str(num)
    result = ''
    for i in range(len(n)-1):
        if int(n[i]) % 2 != 0 and int(n[i+1]) % 2 != 0:
            result += n[i] + '-'
        else:
            result += n[i]
    return result + n[-1]