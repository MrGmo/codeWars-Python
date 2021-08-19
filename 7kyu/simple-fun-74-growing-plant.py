def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = upSpeed
    days = 1
    while height < desiredHeight:
        height += upSpeed
        height -= downSpeed
        days += 1
    return days