def caffeine_buzz(n):
    result = ''
    if n % 12 == 0:
        result += 'Coffee'
    if n % 3 == 0 and not n % 4 == 0:
        result += 'Java'
    if (n % 12 == 0 or n % 3 == 0) and n % 2 == 0:
        result += 'Script'
    return result if len(result) > 0 else 'mocha_missing!'