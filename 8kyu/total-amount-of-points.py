def points(games):
    count = 0
    for game in games:
        x = game[0]
        y = game[2]
        
        if int(x) > int(y):
            count += 3
        if int(x) < int(y):
            count += 0
        if int(x) == int(y):
            count += 1
    return count