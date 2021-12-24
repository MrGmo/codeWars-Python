def snail(col,day,night):
    if day >= col:
        return 1
    days = 0
    while col > 0:
        col -= (day-night)
        days += 1
        if col <= day:
            return days+1
    return days
    