def cake(candles,debris):
    if not candles:
        return 'That was close!'
    count = 0
    for i in range(len(debris)):
        if i % 2 == 0:
            count += ord(debris[i])
        else:
            count += ord(debris[i])-96
    return 'Fire!' if candles*0.7 < count else 'That was close!'