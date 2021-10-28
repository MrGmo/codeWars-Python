def sabb(s, val, happiness):
    word_count = 0
    for char in s:
        if char in 'sabticl':
            word_count += 1
    total = word_count + val + happiness
    return 'Sabbatical! Boom!' if total > 22 else 'Back to your desk, boy.'