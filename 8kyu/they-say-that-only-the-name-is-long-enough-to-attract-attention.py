def is_opposite(s1,s2):
    if len(s1) == 0 and len(s2) == 0:
        return False
    for char in range(0, len(s1)):
        if s1[char] == s2[char]:
            return False
    return True