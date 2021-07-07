def chromosome_check(s):
    result = "Congratulations! You're going to have a "
    if s[1] == 'Y':
        return result + 'son.'
    return result + 'daughter.'