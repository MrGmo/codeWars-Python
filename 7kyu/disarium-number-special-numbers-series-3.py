def disarium_number(num):
    n = list(map(int,list(str(num))))
    total = 0
    for i in range(len(n)):
        total += n[i]**(i+1)
    return 'Disarium !!' if total == num else 'Not !!'