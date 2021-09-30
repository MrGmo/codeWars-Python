def scrabble_score(s):
    score = 0
    s = s.lower()
    for char in s:
        if char in 'aeioulnrst':
            score += 1
        if char in 'dg':
            score += 2
        if char in 'bcmp':
            score += 3
        if char in 'fhvwy':
            score += 4
        if char == 'k':
            score += 5
        if char in 'jx':
            score += 8
        if char in 'qz':
            score += 10
    return score