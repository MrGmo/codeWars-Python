def riders(stations):
    distance = 0
    num_riders = 1
    for station in stations:
        distance += station
        if distance > 100:
            distance = station
            num_riders += 1
    return num_riders
