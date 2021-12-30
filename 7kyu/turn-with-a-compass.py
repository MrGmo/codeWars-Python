def direction(facing, turn):
    compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return compass[(compass.index(facing) + turn // 45) % 8]
