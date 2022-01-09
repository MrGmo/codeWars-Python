def first_non_repeated(s):
    appears_once = [num for num in s if s.count(num) == 1]
    if len(appears_once) == 0:
        return None
    return appears_once[0]
