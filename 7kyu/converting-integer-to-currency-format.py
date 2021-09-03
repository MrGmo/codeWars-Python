import re

def to_currency(price):
    result = ''
    p = str(price)[::-1]
    comma = 0
    for i in range(len(p)):
        result += p[i]
        comma += 1
        if comma == 3:
            result += ','
            comma = 0
    return re.sub('^[,]', '', result[::-1])