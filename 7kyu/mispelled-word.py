from itertools import zip_longest as zip

def mispelled(w1, w2):
    z1 = sum(a != b for a, b in zip(w1, w2))
    z2 = sum(a != b for a, b in zip(w1[::-1], w2[::-1]))
    return min([z1, z2]) < 2
