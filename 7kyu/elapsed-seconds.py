def elapsed_seconds(start,end):
    total_seconds = 0
    diff = []
    e = list(end.timetuple())[:-3]
    s = list(start.timetuple())[:-3]
    for i in range(len(e)):
        diff.append(e[i]-s[i])
    for i in range(len(diff)):
        if i == 0:
            total_seconds += (diff[i]*31540000)
        if i == 1:
            total_seconds += (diff[i]*2628000)
        if i == 2:
            total_seconds += (diff[i]*86400)
        if i == 3:
            total_seconds += (diff[i]*3600)
        if i == 4:
            total_seconds += (diff[i]*60)
        if i == 5:
            total_seconds += (diff[i])
    return total_seconds