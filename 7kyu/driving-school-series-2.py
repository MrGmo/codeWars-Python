def cost(mins):
    if mins < 66:
        return 30
    total = 30
    while mins - 60 > 5:
        mins -= 30
        total += 10
    return total
