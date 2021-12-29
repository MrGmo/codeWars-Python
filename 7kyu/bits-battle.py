def bits_battle(numbers):
    odds = []
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    ones = "".join(bin(x)[2:] for x in odds).count("1")
    zeros = "".join(bin(x)[2:] for x in evens).count("0")
    if ones > zeros:
        return "odds win"
    if ones < zeros:
        return "evens win"
    return "tie"
