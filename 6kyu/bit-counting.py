def count_bits(n):
    binary = list(bin(n)[2:])
    numz = list(map(int, binary))
    return sum(numz)