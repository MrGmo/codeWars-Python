def complete_series(seq):
    if len(seq) != len(set(seq)):
        return [0]
    return list(range(0, max(seq) + 1))
