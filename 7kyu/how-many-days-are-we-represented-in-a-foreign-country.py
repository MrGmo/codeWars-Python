def days_represented(trips):
    days = []
    for i in range(len(trips)):
        days = days + list(range(trips[i][0], trips[i][1] + 1))
    return len(set(days))
