import math

def strong_num(number):
    arr = []
    n = list(map(int,list(str(number))))
    for num in n:
        arr.append(math.factorial(num))
    return 'STRONG!!!!' if sum(arr) == number else 'Not Strong !!'