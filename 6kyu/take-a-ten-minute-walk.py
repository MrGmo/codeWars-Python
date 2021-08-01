def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    return walk.count('s') == walk.count('n') and walk.count('e') == walk.count('w')