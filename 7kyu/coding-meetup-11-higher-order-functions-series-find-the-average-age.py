def get_average(lst):
    total = 0
    for dev in lst:
        total += dev['age']
    return round(total/len(lst))