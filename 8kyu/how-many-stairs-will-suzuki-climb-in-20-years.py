def stairs_in_20(stairs):
    total = 0
    for week in stairs:
        for day in week:
            total += day
    return total*20