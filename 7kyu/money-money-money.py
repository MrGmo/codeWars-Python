def calculate_years(p,i,x,d):
    if p == d:
        return 0
    
    final = p
    count = 0
    
    while final <= d:
        money_per_year = (final*i)-(final*i*x)
        final += money_per_year
        count += 1
    return count