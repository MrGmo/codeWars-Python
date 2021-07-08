def evil(n):
    string = bin(n)[2:]
    count = string.count('1')
    return "It's Odious!" if count % 2 != 0 else "It's Evil!"