def generate_pairs(m, n):
    pairs = []
    for a in range(m, n+1):
        for b in range(a, n+1):
            pairs.append((a, b))
    return pairs